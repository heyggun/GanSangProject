# -*- coding: utf-8 -*-
"""ChainCode

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hlKvv7Y8hYOyGf7bl_Rghb3iCgNwpGlZ
"""

import numpy as np

# chain_code 하나하나가 얼굴을 뜻함 animation 데이터의 경우 5개였음
np.random.seed(0)
chain_code1 = np.random.randn(68,2)
chain_code2 = np.random.randn(68,2)
chain_code3 = np.random.randn(68,2)
chain_code_lst = [chain_code1, chain_code2, chain_code3]

# chain_code로 구한 값의 무게중심 구하기
def centroid(c):
  return c.mean(axis=0)

# index별로 무게중심으로부터의 거리 구하기
def l2_norm(a, b):
  return np.sqrt(np.sum((a-b) ** 2))

def distance_vector(c):
  lst = []
  cent = centroid(c)
  for i in c:
    lst.append(l2_norm(i, cent))
  return lst

distance_vectors = []

# 구해진 거리들로 68차원 vector 만들기
for chain_code in chain_code_lst:
  distance_vectors.append(distance_vector(chain_code))

import pandas as pd

df = pd.DataFrame(np.array(distance_vectors))

# pca로 차원 축소하기

from sklearn.decomposition import PCA

pca = PCA(n_components= 2)

pca_df = pca.fit_transform(df)

# 차원 축소된 애들 2차원 plotting 하기
import matplotlib.pyplot as plt
plt.scatter(pca_df[:,0], pca_df[:,1])