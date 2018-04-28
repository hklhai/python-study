# -*- coding: utf-8 -*-
from gensim.models import Word2Vec
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')

en_wiki_word2vec_model = Word2Vec.load(r'D:\Program\opencc-1.0.1-win64\word_segment.model')

test_words = ['苹果', '数学', '学术', '白痴', '篮球']
for i in range(5):
    res = en_wiki_word2vec_model.most_similar(test_words[i])
    print(test_words[i])
    print(res)
