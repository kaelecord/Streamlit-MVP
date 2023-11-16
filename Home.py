# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 12:44:23 2023

@author: kaele
"""

import pandas as pd
import streamlit as st
import plotly.graph_objects as go
from friends_functions import * 

st.sidebar.success("Select a page above")

header = st.container()
dataset = st.container()
plot_info = st.container()
speakers = st.container()

with header:
    st.title("Project MVP - Kael Ecord 11/13/2023")
    st.header("Home")

with dataset:
    st.subheader("Data")
    st.markdown("""The data used to create all aspects of this project comes from the Emory NLP Character Mining Prpject. The dataset is based on the popular TV show, Friends, that aired from September 22, 1994 through May 6, 2004. All data used was extracted from a collection of json files that can be found [here](https://github.com/emorynlp/character-mining/tree/master/json).""")
    st.markdown("Below is an example of the full data set that this project will be working with.")
    
    friends_data = pd.read_csv('C:\\Users\\kaele\\OneDrive\\Documents\\IUPUI\\Fall 2023\\I501 - Intro to Informatics\\Final Project\\data\\friends_transcript_data.csv')
    st.write(friends_data.sample(10))
    st.caption("Note: the num_talked_about is not in the original dataset.")
    
    st.subheader("Column Descriptions")
    st.markdown('''- season_id: Unique ID for season number  
- episode_id: Unique ID for episode number within a season
- scene_id: Unique ID for scene number within an epsiode  
- utterace_id: Unique ID for an utterance number within an scene  
- speaker: name of character who speaks the line   
- tokens: list of lists - outer list for each sentence within a line - inner list for each word or punction within a sentence.  
- transcript: tokens joined to form line spoken by speaker for the utterance  
- emotion: emotion of line determined by results of [Emory NLP Project](https://github.com/emorynlp/emotion-detection)  
- character_entities: characters spoken about within the utterance as determined by [Emory NLP Project](https://github.com/emorynlp/character-identification)  
- num_talked_about: integer corresponding to number length of character_entities list''')
    
    st.subheader("Data Description")
    fig = go.Figure()
    fig.add_trace(go.Indicator(
        mode = "number",
        domain = {'x': [0,0.5], 'y': [0.5,1]},
        value = len(list(friends_data['season_id'].unique())),
        title = {"text": "Seasons"}))
    fig.add_trace(go.Indicator(
        mode = "number",
        domain = {'x': [0.5,1], 'y': [0.5,1]},
        value = len(friends_data.groupby(['season_id','episode_id'])),
        title = {"text": "Episodes"}))
    fig.add_trace(go.Indicator(
        mode = "number",
        domain = {'x': [0,0.5], 'y': [0,0.5]},
        value = len(friends_data.groupby(['season_id','episode_id', 'scene_id'])),
        title = {"text": "Scenes"}))
    fig.add_trace(go.Indicator(
        mode = "number",
        domain = {'x': [0.5,1], 'y': [0,0.5]},
        value = len(friends_data.groupby(['season_id','episode_id', 'scene_id', 'utterance_id'])),
        title = {"text": "Utterances"}))
    fig.update_layout(height = 450, width = 400)
    st.write(fig)
    
   
    
