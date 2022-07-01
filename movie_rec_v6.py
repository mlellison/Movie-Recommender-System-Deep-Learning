# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 15:51:12 2022

@author: indra
"""
#final working version 22:08
import streamlit as st
import requests
from find_movie_v4 import get_recommendations, get_scores
st.set_page_config(layout="wide")
st.text("""
▀█▀ █▀▀ ▄▀█ █▀▄▀█   █▄▀ █ █▀▄▀█
░█░ ██▄ █▀█ █░▀░█   █░█ █ █░▀░█""")
st.title("Movie Recommender")

# user input movie name here
mov_title = st.text_input('Input your movie name here and press enter')
if mov_title:
    try: 
        url = f"http://www.omdbapi.com/?t={mov_title}&apikey=167850cf"
        re = requests.get(url)
        re=re.json()
        col3, col4 =st.columns([1,2])
        with col3:
            st.subheader(re['Title'])
            st.image(re['Poster'])
        with col4:
            st.caption(f"Genre:{re['Genre']} Year: {re['Year']}")
            st.write(re['Plot'])
            st.text(f"Rating:{re['imdbRating']}")
            #st.progress(float(re['imdbRating'])/10)
        with st.container():
            st.title('Recommended For You')
            col1, col2 =st.columns([1,2])
            lsmov = get_recommendations(mov_title)
            score = get_scores(mov_title)
            with col1:
                for i, mov in enumerate(lsmov):
                    try:
                        url = f"http://www.omdbapi.com/?t={mov}&apikey=167850cf"
                        re2 = requests.get(url)
                        re2 = re2.json()
                        col6 = st.subheader(re2['Title'])
                        col7 = st.image(re2['Poster'])
                        st.text(f"Rating:{re2['imdbRating']}")
                        #st.progress(float(re2['imdbRating'])/10)
                        st.write(f"Match: {round(score[i],2)*100}","%")
                        st.progress(round(score[i],2))
                    except:
                        pass
  
    except:
        st.error("No Movie with that name")
