import streamlit as st # for creating a web app
import pandas as pd # for data manipulation
import datetime # for working with dates
import csv # for reading and writing csv files
import os # for file operations


MOOD_FILE = "mood_log.csv"


def load_mood_data():
    if not os.path.exists(MOOD_FILE):
        return pd.DataFrame(columns=["Date", "Mood"])
    
    return pd.read_csv(MOOD_FILE)


def save_mood_data(date, mood):
    with open(MOOD_FILE , "a") as file:
        writer = csv.writer(file)
        writer.writerow([date, mood])

    

st.title("Mood Tracker")

today = datetime.date.today()

st.subheader("How are you feeling today?")

mood = st.selectbox("Select your mood", ["Happy", "Sad", "Angry" , "Neutral"])


if st.button("Log Mood"):
    save_mood_data(today, mood)

    st.success(f"Mood logged for {today} as {mood}")

data = load_mood_data()


# if data variable is not empty
if not data.empty: 
    st.subheader("Mood Trends Over Time")  
    # converting the date column to datetime
    data["Date"] = pd.to_datetime(data["Date"])

    mood_counts = data.groupby("Mood").count().reset_index()
