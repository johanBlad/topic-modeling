from gensim.models.coherencemodel import CoherenceModel
import numpy as np

def get_metric_cv(topics, texts, gensim_dict):
    cm = CoherenceModel(topics=topics, texts=texts, dictionary=gensim_dict, coherence='c_v', topn=12)
    coherence = cm.get_coherence_per_topic(with_std=True)
    # Return format list of coherences for each topic
    return coherence

def get_metric_umass(topics, gensim_dict, gensim_corpus):
    cm = CoherenceModel(topics=topics, corpus=gensim_corpus, dictionary=gensim_dict, coherence='u_mass', topn=12)
    coherence = cm.get_coherence_per_topic(with_std=True)
    # Return format list of coherences for each topic
    return coherence

def aggregate_metrics(metric_for_topics):
    '''Input: list of floats'''
    m = sorted(metric_for_topics)
    return {
        'avg' : round(np.mean(m), 4),
        'med' : get_median(m),
        'top' : get_top(m),
        'bot' : get_bot(m),
    }

def get_median(m):
    '''Input: list of sorted floats'''
    if len(m) == 0:
        return 0
    else:
        return round(m[len(m) // 2], 4)

def get_top(m):
    '''Input: list of sorted floats'''
    if len(m) == 0:
        return 0
    elif len(m) <= 10:
        return round(np.mean(m[-2:]), 4)
    elif len(m) <= 40:
        return round(np.mean(m[-4:]), 4)
    else:
        return round(np.mean(m[-(round(len(m)*0.1)):]), 4)


def get_bot(m):
    '''Input: list of sorted floats'''
    if len(m) == 0:
        return 0
    elif len(m) <= 10:
        return round(np.mean(m[:2]), 4)
    elif len(m) <= 40:
        return round(np.mean(m[:4]), 4)
    else:
        return round(np.mean(m[:(round(len(m)*0.1))]), 4)