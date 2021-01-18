from gensim.models.phrases import Phrases, Phraser
import os

def apply_ngrams(corpus, phraser, level=3):
    if level == 2:
        return [[clean_hyphens(term) for term in phraser[doc]] for doc in corpus]
    elif level == 3:
        return [[clean_hyphens(term) for term in phraser[phraser[doc]]] for doc in corpus]

def clean_hyphens(term):
    return term.strip('-').replace('-', '_')

def flatten_to_bigram(bigrams, trigrams):
    return bigrams + [gram[0:2] for gram in trigrams if gram[0:2] not in bigrams] + \
            [['_'.join(gram[0:2]), gram[2]] for gram in trigrams] + \
            [[gram[0], '_'.join(gram[1:3])] for gram in trigrams] 

def build_ne_gold_phraser(ne_ngrams, gold_ngrams):
    # 1. Merge
    merged_bigrams = [list(gram) for gram in set(ne_ngrams['bigrams'] + gold_ngrams['bigrams'])]
    merged_trigrams = [list(gram) for gram in set(ne_ngrams['trigrams'] + gold_ngrams['trigrams'])]
    
    # 2. Flatten
    flat_ngrams = flatten_to_bigram(merged_bigrams, merged_trigrams)

    # 3. Model
    EPS = 0.000001
    phrases = Phrases(flat_ngrams, min_count=EPS, threshold=EPS, delimiter=b'_')
    phraser = Phraser(phrases)
    return phraser


def get_gold_ngrams():
    ngrams = []
    path = os.getcwd() + '/ngrams_gold_saved/'
    for filename in os.listdir(path):
        with open(os.path.join(path, filename), 'r') as f: # open in readonly mode
            lines = f.readlines()
            for line in lines:
                ngrams.append(line.strip())
    ngrams_unique = sorted(list(set(ngrams)))

    gold_ngrams = {
        'bigrams': [],
        'trigrams': [],
    }

    for ngram in ngrams_unique:
        ngram_split = ngram.split('_')
        if len(ngram_split) == 2:
            gold_ngrams['bigrams'].append(tuple(ngram_split))
        if len(ngram_split) == 3:
            gold_ngrams['trigrams'].append(tuple((ngram_split)))
    return gold_ngrams
