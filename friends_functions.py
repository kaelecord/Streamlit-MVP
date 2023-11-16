# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 15:24:12 2023

@author: kaele
"""
import pandas as pd
import plotly.express as px
import numpy as np

full_data = pd.read_csv('C:\\Users\\kaele\\OneDrive\\Documents\\IUPUI\\Fall 2023\\I501 - Intro to Informatics\\Final Project\\data\\friends_transcript_data.csv')
plots = pd.read_csv('C:\\Users\\kaele\\OneDrive\\Documents\\IUPUI\\Fall 2023\\I501 - Intro to Informatics\\Final Project\\data\\friends_plots_cleaned_data.csv') 
speaker = pd.read_csv('C:\\Users\\kaele\\OneDrive\\Documents\\IUPUI\\Fall 2023\\I501 - Intro to Informatics\\Final Project\\data\\speaker_cleaned_data.csv')

def get_seasons():
    season_ = list(full_data['season_id'].unique())
    season_.insert(0,"ALL")
    return season_

def get_episodes(season = 'ALL'):
    if season == "ALL":
        episode_ = list(full_data['episode_id'].unique())
    else:
        episode_ = list(full_data['episode_id'][full_data['season_id'] == season].unique())
    episode_.insert(0,"ALL")
    return episode_

def get_scenes(season = 'ALL', episode = 'ALL'):
    if season == "ALL" and episode == "ALL":
        scene_ = list(full_data['scene_id'].unique())
    elif season != "ALL" and episode == "ALL":
        scene_ = list(full_data['scene_id'][full_data['season_id'] == season].unique())
    elif season == "ALL" and episode != "ALL":
        scene_ = list(full_data['scene_id'][full_data['episode_id'] == episode].unique())
    else:
        scene_ = list(full_data['scene_id'][(full_data['season_id'] == season) & (full_data['episode_id'] == episode)].unique())
    scene_.insert(0, "ALL")
    return scene_

def get_plot(season, episode, scene):
    if (season == "ALL" or episode == "ALL"):
        return "Please refine search to at least 1 episode."
    if scene == "ALL":
        temp = plots[(plots['season_id'] == season) & (plots['episode_id'] == episode) & (plots['plot'] != 'No plot availble for scene')]
        temp['scene_plot'] = "SCENE(" + temp['scene_id'] + ") " + temp['plot']
        plots_joined = ' ' .join(temp['scene_plot'])
        return plots_joined
    else:
        temp = plots[(plots['season_id'] == season) & (plots['episode_id'] == episode) & (plots['scene_id'] == scene)]
    if len(temp) == 0:
        return "No plot information for selected filters. Sorry :("
    else:
        plots_joined = ' ' .join(temp['plot'])
        return plots_joined
    
def get_speakers(season, episode):
    if season == "ALL" and episode == "ALL":
        temp = speaker.groupby(['speaker']).agg({'speaker': ['count']}).reset_index()
        temp.columns = ["".join(col).strip() for col in temp.columns.values]
        temp = temp[temp['speakercount']>10]
        temp = temp.sort_values(['speakercount', 'speaker'], ascending = False).reset_index()
        return list(temp['speaker'])
    elif season != "ALL" and episode == "ALL":
        temp = speaker.groupby(['season_id', 'speaker']).agg({'speaker': ['count']}).reset_index()
        temp.columns = ["".join(col).strip() for col in temp.columns.values]
        temp = temp[(temp['speakercount']>5) & (temp['season_id'] == season)]
        temp = temp.sort_values(['speakercount', 'speaker'], ascending = False).reset_index()
    else:
        temp = speaker.groupby(['season_id','episode_id', 'speaker']).agg({'speaker': ['count']}).reset_index()
        temp.columns = ["".join(col).strip() for col in temp.columns.values]
        temp = temp[(temp['speakercount']>1) & (temp['season_id'] == season) & (temp['episode_id'] == episode)]
        temp = temp.sort_values(['speakercount', 'speaker'], ascending = False).reset_index()
    return list(temp['speaker'])

def create_speaker_plot(speaker_list):
    speaker_grouped = speaker.groupby(['season_id','episode_id','speaker']).agg({'speaker': ['count']}).reset_index()
    speaker_grouped.columns = ["".join(col).strip() for col in speaker_grouped.columns.values]
    speaker_grouped['season_ep'] = speaker_grouped['season_id'] + '_' +speaker_grouped['episode_id']
    if len(speaker_list) == 0:
        return "Select character to see plot"
    else:
        speaker_data = speaker_grouped[speaker_grouped['speaker'].isin(speaker_list)].reset_index()
        fig = px.line(speaker_data, x="season_ep", y="speakercount", hover_name="speaker",color = 'speaker',
                      line_shape="spline", render_mode="svg", color_discrete_sequence=px.colors.qualitative.G10).update_layout(
                      xaxis_title="Season_Episode", yaxis_title="Speaker Count", title = "Speaker Count by Episode")
        fig.update_xaxes(categoryorder='array', categoryarray= list(speaker_data['season_ep']))

        return fig