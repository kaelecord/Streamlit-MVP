# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 12:13:56 2023

@author: kaele
"""

import streamlit as st
from friends_functions import * 

st.sidebar.success("Select a page above")

header = st.container()
plot_info = st.container()


with header:
    st.title("Project MVP - Kael Ecord 11/13/2023")
    
with plot_info:
    st.subheader("Select an episode or scene to see its plot!")
    col_1, col_2, col_3 = st.columns(3)
    season_choice = col_1.selectbox('Season:', options = get_seasons(), index = 0)
    episode_choice = col_2.selectbox('Episode:', options = get_episodes(season=season_choice), index = 0)
    scene_choice = col_3.selectbox('Scene(s):', options = get_scenes(season=season_choice, episode=episode_choice), index = 0)
    
    st.write(get_plot(season_choice, episode_choice, scene_choice))