import itertools
import os
import random
import sys

import nltk

import kenlm

import arpa

MAX_ORDER = 5
N_QUERIES = 10
N_SENTENCES = 10

TEST_ARPA = os.path.join(os.path.dirname(__file__), "data/test.arpa")
WORDS = list(nltk.corpus.PlaintextCorpusReader("/usr/share/dict", "words").words())


def test_log_p_random():
    random_queries = list(_random_queries())
    _test_log_p(random_queries)


def _test_log_p(queries):
    lm_me = arpa.loadf(TEST_ARPA)[0]
    lm_ken = kenlm.LanguageModel(TEST_ARPA)
    results_me = []
    results_ken = []
    for ngram in queries:
        prob_me = lm_me.log_p(ngram)
        prob_ken = list(lm_ken.full_scores(" ".join(ngram), False, False))[-1][0]
        results_me.append(prob_me)
        results_ken.append(prob_ken)
    assert all(round(m - k, 4) == 0 for m, k in zip(results_me, results_ken))


def _random_ngram(length):
    return tuple(random.sample(WORDS, length))


def _random_queries():
    for order in range(1, MAX_ORDER + 1):
        for _ in range(N_QUERIES):
            yield _random_ngram(order)


def test_log_s_random_no_tags():
    _test_log_s(_random_sentences(), None, None)


def test_log_s_random_sos():
    _test_log_s(_random_sentences(), "<s>", None)


def test_log_s_random_eos():
    _test_log_s(_random_sentences(), None, "</s>")


def test_log_s_random_sos_eos():
    _test_log_s(_random_sentences(), "<s>", "</s>")


def _test_log_s(sentences, sos, eos):
    lm_me = arpa.loadf(TEST_ARPA)[0]
    lm_ken = kenlm.LanguageModel(TEST_ARPA)
    results_me = []
    results_ken = []
    for sentence in sentences:
        prob_me = lm_me.log_s(sentence, sos=sos, eos=eos)
        scores_ken = lm_ken.full_scores(sentence, bool(sos), bool(eos))
        prob_ken = sum(prob for prob, _, _ in scores_ken)
        results_me.append(prob_me)
        results_ken.append(prob_ken)
    assert all(round(m - k, 4) == 0 for m, k in zip(results_me, results_ken))


def _random_sentences():
    sample = [" ".join(words) for words in nltk.corpus.udhr2.sents("eng.txt")]
    return random.sample(sample, N_SENTENCES)
