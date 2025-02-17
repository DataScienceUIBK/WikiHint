import json
import os.path
from tqdm  import tqdm
from hinteval import Dataset


def download_wikihint():
    if not os.path.exists('./entire.json'):
        wikihint = Dataset.download_and_load_dataset('wikihint', force_download=True)
        wikihint.store_json('./entire.json')


def cleaning():
    with open('./entire.json', 'r') as f:
        entire = json.load(f)
    for subset in tqdm(entire['subsets']):
        new_subset = []
        for q_key in entire['subsets'][subset]['instances']:
            instance = entire['subsets'][subset]['instances'][q_key]
            new_instance = {'id': q_key, 'question': dict(), 'answer': dict(), 'hints': list()}
            #####################################
            question = dict()
            question['question'] = instance['question']['question']
            question['question_type'] = instance['question']['question_type']
            question['difficulty'] = instance['question']['metadata']['difficulty']
            entities = []
            for ent in instance['question']['entities']:
                entity = dict()
                entity['entity'] = ent['entity']
                entity['ent_type'] = ent['ent_type']
                entity['start_index'] = ent['start_index']
                entity['end_index'] = ent['end_index']
                entity['wikipedia_page_title'] = ent['metadata']['wikipedia_page_title']
                entity['wiki_views_per_month'] = ent['metadata']['wiki_views_per_month']
                entity['normalized_views'] = ent['metadata']['normalized_views']
                entities.append(entity)
            question['entities'] = entities
            question['candidate_answers'] = instance['question']['metadata']['candidate_answers-llama-3-70b']
            metrics = dict()
            metrics['readability'] = \
                instance['question']['metrics']['readability-llm-meta-llama_Meta-Llama-3.1-8B-Instruct-Turbo']['value']
            metrics['familiarity'] = instance['question']['metrics']['familiarity-wikipedia-trf']['value']
            question['metrics'] = metrics
            new_instance['question'] = question
            #####################################
            answer = dict()
            answer['answer'] = instance['answers'][0]['answer']
            entities = []
            for ent in instance['answers'][0]['entities']:
                entity = dict()
                entity['entity'] = ent['entity']
                entity['ent_type'] = ent['ent_type']
                entity['start_index'] = ent['start_index']
                entity['end_index'] = ent['end_index']
                entity['wikipedia_page_title'] = ent['metadata']['wikipedia_page_title']
                entity['wiki_views_per_month'] = ent['metadata']['wiki_views_per_month']
                entity['normalized_views'] = ent['metadata']['normalized_views']
                entities.append(entity)
            answer['entities'] = entities
            metrics = dict()
            metrics['familiarity'] = instance['answers'][0]['metrics']['familiarity-wikipedia-trf']['value']
            answer['metrics'] = metrics
            new_instance['answer'] = answer
            #####################################
            for hint_instance in instance['hints']:
                hint = dict()
                hint['hint'] = hint_instance['hint']
                hint['source'] = hint_instance['source']
                if 'rank' in hint_instance['metadata']:
                    hint['rank'] = hint_instance['metadata']['rank']
                entities = []
                for ent in hint_instance['entities']:
                    entity = dict()
                    entity['entity'] = ent['entity']
                    entity['ent_type'] = ent['ent_type']
                    entity['start_index'] = ent['start_index']
                    entity['end_index'] = ent['end_index']
                    entity['wikipedia_page_title'] = ent['metadata']['wikipedia_page_title']
                    entity['wiki_views_per_month'] = ent['metadata']['wiki_views_per_month']
                    entity['normalized_views'] = ent['metadata']['normalized_views']
                    entities.append(entity)
                hint['entities'] = entities
                metrics = dict()
                metrics['relevance'] = hint_instance['metrics']['relevance-llm-meta-llama_Meta-Llama-3.1-8B-Instruct-Turbo'][
                        'value']
                metrics['readability'] = \
                    hint_instance['metrics']['readability-llm-meta-llama_Meta-Llama-3.1-8B-Instruct-Turbo'][
                        'value']
                metrics['convergence'] = hint_instance['metrics']['convergence-llm-llama-3-70b'][
                        'value']
                metrics['familiarity'] = hint_instance['metrics']['familiarity-wikipedia-trf']['value']
                metrics['answer_leakage'] = hint_instance['metrics']['answer-leakage-contextual-include_stop_words-trf']['value']
                hint['metrics'] = metrics
                new_instance['hints'].append(hint)
            #####################################
            new_subset.append(new_instance)
        os.makedirs('./subsets', exist_ok=True)
        with open(f'./subsets/{subset}.json', 'w') as f:
            json.dump(new_subset, f, indent=4)


if __name__ == '__main__':
    download_wikihint()
    cleaning()
