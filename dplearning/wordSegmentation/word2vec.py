# -*- coding: utf-8 -*-

import tensorflow as tf
import numpy as np
import math
import collections  # 计算词频
import jieba
import re
import pickle as pkl
import os
import os.path as path

if __name__ == '__main__':
    stop_words = []
    with open("D:\\python-study\\stop_word.txt", encoding="utf-8") as f:
        line = f.readline()
        while line:
            stop_words.append(line[:-1]) # 最后一个为换行符号，不取出
            line = f.readline()
        stop_words = set(stop_words) #去除重复值