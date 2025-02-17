import torch
import numpy as np
from scipy.optimize import minimize
from transformers import BertForSequenceClassification, BertTokenizer, BertConfig


class HintRank:
    def __init__(self):
        self.tokenizer = BertTokenizer.from_pretrained('JamshidJDMY/HintRank_AnswerAware')
        self.answer_aware = BertForSequenceClassification.from_pretrained('JamshidJDMY/HintRank_AnswerAware',
                                                                          num_labels=2)
        self.answer_agnostic = BertForSequenceClassification.from_pretrained('JamshidJDMY/HintRank_AnswerAgnostic',
                                                                             num_labels=2)
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.answer_aware.to(self.device)
        self.answer_agnostic.to(self.device)

    def pairwise_compare(self, question: str, hint_1: str, hint_2: str, answer: str = None):
        """
        Compares two hints using the given question and answer (if available).
        Returns 1 if hint_1 is better, 0 if hint_2 is better.
        """
        if answer:
            # Answer-aware format
            text_1 = f"{question}? {hint_1}. Answer is {answer}"
            text_2 = f"{question}? {hint_2}. Answer is {answer}"
            model = self.answer_aware
        else:
            # Answer-agnostic format
            text_1 = f"{question}? {hint_1}."
            text_2 = f"{question}? {hint_2}."
            model = self.answer_agnostic

        # Tokenize a single input pair
        encoded = self.tokenizer(
            text_1, text_2,
            return_tensors="pt", padding=True, truncation=True, max_length=128
        ).to(self.device)

        # Get prediction
        with torch.no_grad():
            logits = model(**encoded).logits

        # Determine which hint is better (0 = hint_2, 1 = hint_1)
        model_output = torch.argmax(logits, dim=1).item()
        if model_output == 0:
            return 0, hint_2
        else:
            return 1, hint_1

    def _bradley_terry_ranking(self, comparison_matrix):
        """
        Applies the Bradley-Terry model to convert the pairwise comparison matrix into a ranked list.
        """
        num_hints = len(comparison_matrix)

        # Compute win counts for each hint
        win_counts = np.sum(comparison_matrix, axis=1)

        # Define the Bradley-Terry likelihood function
        def likelihood(params):
            scores = np.exp(params)  # Convert to positive values (scale-free)
            likelihood_sum = 0

            for i in range(num_hints):
                for j in range(num_hints):
                    if i != j:
                        likelihood_sum += comparison_matrix[i, j] * np.log(scores[i] / (scores[i] + scores[j]))

            return -likelihood_sum  # Negative log-likelihood for minimization

        # Initialize scores and optimize
        initial_params = np.zeros(num_hints)
        result = minimize(likelihood, initial_params, method="L-BFGS-B")
        final_scores = np.exp(result.x)  # Convert back to ranking scores

        # Rank hints based on their estimated strength
        ranked_indices = np.argsort(-final_scores)  # Sort in descending order

        return ranked_indices, final_scores

    def listwise_compare(self, question: str, hints: list, answer: str = None):
        """
        Compares all pairs of hints independently and returns a comparison matrix.

        Returns:
        - A NxN matrix where entry (i, j) is:
          * 1 if hint i is preferred over hint j
          * 0 if hint j is preferred over hint i
        """
        num_hints = len(hints)
        comparison_matrix = np.zeros((num_hints, num_hints), dtype=int)

        for i in range(num_hints):
            for j in range(num_hints):  # Compare ALL pairs, including lower triangle
                if i == j:
                    comparison_matrix[i, j] = 1  # Self-comparison is always 1
                else:
                    result = self.pairwise_compare(question, hints[i], hints[j], answer)[0]
                    comparison_matrix[i, j] = result  # Directly assign result

        ranked_indices, final_scores = self._bradley_terry_ranking(comparison_matrix)

        ranked_hints = [hints[i] for i in ranked_indices]
        ranked_scores = [final_scores[i] for i in ranked_indices]

        return list(zip(ranked_hints, ranked_scores))

if __name__ == '__main__':
    from hint_rank import HintRank

    # Initialize the HintRank model
    ranker = HintRank()

    # Define question, answer, and hints
    question = "What is the capital of Austria?"
    answer = "Vienna"
    hints = [
        "Mozart and Beethoven once lived here.",
        "It is a big city in Europe.",
        "Austria’s largest city and capital."
    ]

    # Pairwise Comparison Example
    print("Pairwise Hint Comparison")
    better_hint_answer_aware = ranker.pairwise_compare(question, hints[1], hints[2], answer)
    better_hint_answer_agnostic = ranker.pairwise_compare(question, hints[0], hints[1])

    print(
        f"\tAnswer-Aware: Hint {2 if better_hint_answer_aware == 1 else 3} is better than Hint {3 if better_hint_answer_aware == 0 else 2}.")
    print(
        f"\tAnswer-Agnostic: Hint {1 if better_hint_answer_agnostic == 1 else 2} is better than Hint {2 if better_hint_answer_agnostic == 0 else 1}.")

    print("\nListwise Hint Ranking")

    # Answer-Aware Ranking
    print("\tAnswer-Aware Ranked Hints:")
    ranked_hints_answer_aware = ranker.listwise_compare(question, hints, answer)
    for i, (hint, _) in enumerate(ranked_hints_answer_aware):
        print(f"\t\tRank {i + 1}: {hint}")

    # Answer-Agnostic Ranking
    print("\n\tAnswer-Agnostic Ranked Hints:")
    ranked_hints_answer_agnostic = ranker.listwise_compare(question, hints)
    for i, (hint, _) in enumerate(ranked_hints_answer_agnostic):
        print(f"\t\tRank {i + 1}: {hint}")
