import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

df = pd.read_csv("spotify")
l = list(["Select Graph","Energy vs Danceability","Year vs Energy","Top 10 Genres (Hit Song)","Popularity vs Instrumental Song","BPM Distribution","Artists vs Most Songs","Happy Songs vs Popularity"])


st.title("The Spotify Music Trend - 📊Visualiser")
st.sidebar.title("Choose The Appropriate Option")
info = st.sidebar.selectbox("Select Graph" , l)
btn = st.sidebar.button("Plot The Selected Graph")

if btn:
    if info == "Select Graph":
        st.sidebar.error("Please Choose any one of these!")
    else:
        st.subheader("The Selected Graph is Shown Below: ")
        if info == "Energy vs Danceability":
            fig = px.scatter(df , x = "Energy" , y = "Danceability" , hover_name="Top Genre")
            st.plotly_chart(fig)

            st.markdown("### To identify which genre of songs are high in :point_up_2:***energy*** and ***danceability***")

        elif info == "Year vs Energy":
            fig = px.bar(df  ,x = "Year" , y = "Avg_Energy" , color = "Artist")
            st.plotly_chart(fig)

            st.markdown("### To identify which Artist of songs are high in :point_up_2:(Stacked Bar Graph) ***Average Energy*** and ***Year***")

        elif info == "Top 10 Genres (Hit Song)":
            final = df["Top Genre"].value_counts().head(10).reset_index()
            final.columns = ["Top Genre", "Count"]

            fig = px.bar(final,x = "Top Genre" , y = "Count")
            st.plotly_chart(fig)

            st.markdown("### To identify which Genre of songs is popular :point_up_2:(Bar Graph) ***Top Genres*** and ***Counts***")

        elif info == "Popularity vs Instrumental Song":
            fig = px.scatter(df, x='Acousticness', y='Popularity', color='Top Genre')
            st.plotly_chart(fig)

            st.markdown("### To identify which Genres of songs are popular in Instrumental Music :point_up_2:***Popularity*** and ***Acousticness(Instrumental Music)***")
        elif info == "BPM Distribution":
            fig = px.histogram(df,x= "Beats Per Minute (BPM)", hover_name="Artist")
            st.plotly_chart(fig)

            st.markdown("### To identify which Artist songs have high BPM is :point_up_2:(Histogram) ***BPM*** and ***Counts***")

        elif info == "Artists vs Most Songs":
            top_artists = df['Artist'].value_counts().nlargest(10).reset_index()
            top_artists.columns = ['Artist', 'Count']

            fig = px.bar(top_artists, x='Count', y='Artist', orientation='h', title='Top 10 Artists by Song Count' )
            st.plotly_chart(fig)

            st.markdown("### To identify which Artist songs have most Hit song :point_up_2:(Horizontal Bar Graph) ***Artist*** and ***Counts***")

        else:
            fig = px.scatter(df, x='Valence', y='Popularity', color='Top Genre')
            st.plotly_chart(fig)

            st.markdown("### To identify which genre of songs are Popular in Happy Song :point_up_2:***Valence*** and ***Popularity***")
        


