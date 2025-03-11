import streamlit as st # For creating web interface
import pandas as pd # For data manipulation
import datetime # For handling dates
import csv # For reading and writing CSV file
import os # For file operations

MOOD_FILE = "mood_log.csv"

def load_mood_data():
    # Load existing mood data or create an empty DataFrame
    if not os.path.exists(MOOD_FILE) or os.stat(MOOD_FILE).st_size == 0:
        return pd.DataFrame(columns=["Date", "Mood"])
    return pd.read_csv(MOOD_FILE, encoding="utf-8") # encoding cuz we have emojis

def save_mood_data(date, mood):
    data = load_mood_data()
    
    # Check if today's mood is already logged
    if date in data["Date"].values:
        data.loc[data["Date"] == date, "Mood"] = mood
        data.to_csv(MOOD_FILE, index=False, encoding="utf-8")
        return "updated"
    else:
        # Add a new mood entry
        with open(MOOD_FILE, "a", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            if os.stat(MOOD_FILE).st_size == 0:
                writer.writerow(["Date", "Mood"])  # Write header if file is empty
            writer.writerow([date, mood])
        return "added"

st.title("🧠 Mood Tracker")  

today = datetime.date.today()

st.subheader("💭 How are you feeling today?")

mood = st.selectbox("🧐 Select your mood", ["😊 Happy", "😢 Sad", "😡 Angry", "😐 Neutral"])

if st.button("📝 Log Mood"):
    result = save_mood_data(str(today), mood)
    if result == "updated":
        st.info(f"🔄 Mood for {today} updated to {mood}.")
    else:
        st.success(f"✅ Mood logged for {today} as {mood}.")


data = load_mood_data()

if not data.empty:
    st.subheader("📈 Mood Trends Over Time")
    data["Date"] = pd.to_datetime(data["Date"])
    mood_counts = data.groupby("Mood").count()["Date"]
    st.bar_chart(mood_counts)
else:
    st.info("ℹ️ No mood data available. Start by logging today's mood.")

# Footer
st.markdown("""
    <hr>
    <p style='text-align: center;'>
        Mood Tracker by <a href='https://github.com/sabehshaikh'>Sabeh Shaikh</a>
    </p>
""", unsafe_allow_html=True)