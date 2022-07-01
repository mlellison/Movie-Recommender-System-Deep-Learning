# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 16:16:53 2022

@author: indra
"""
import streamlit as st
import pandas as pd
import numpy as np

#tlts = st.text_input('Input your movie name here and press enter')

tf = pd.read_csv('./data/tf14-18.csv')
tf.shape

cosine_sim = np.load('./data/movieMatrix14-18.npy')
cosine_sim.shape

tf = tf.reset_index()
titles = tf['movieName']
indices = pd.Series(tf.index, index=tf['movieName'])

def get_recommendations(searchItem):
    any((title := s).startswith(searchItem) for s in tf.movieName)
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:31]
    movie_indices = [i[0] for i in sim_scores]
    topTen = [i for i in (titles.iloc[movie_indices]).head(10)]
    return topTen

def get_scores(searchItem):
    any((title := s).startswith(searchItem) for s in tf.movieName)
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:31]
    movie_indices = [i[0] for i in sim_scores]
    scores = [i[1] for i in sim_scores]
    topTen = [i for i in (titles.iloc[movie_indices]).head(10)]
    return scores
#move_recs = get_recommendations(tlts)
