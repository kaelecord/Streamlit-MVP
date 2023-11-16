# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 12:25:31 2023

@author: kaele
"""

import pandas as pd
import numpy as np
import plotly.express as px
import networkx as nx
import streamlit as st
from friends_functions import * 

st.sidebar.success("Select a page above")

speakers = st.container()

with speakers:
    st.title("Project MVP - Kael Ecord 11/13/2023")
    st.subheader("Filter to get characters from specific episodes")
    col_1, col_2 = st.columns(2)
    season_choice = col_1.selectbox('Season:', options = get_seasons(), index = 0)
    episode_choice = col_2.selectbox('Episode:', options = get_episodes(season=season_choice), index = 0)
    
    st.subheader("Select a character to see their speaking history throughout the show")
    speaker_choice = st.multiselect('Character:', options= get_speakers(season_choice, episode_choice))
    
    fig = create_speaker_plot(speaker_choice)
    
    st.write(fig)