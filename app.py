# app.py
import streamlit as st
import random

st.set_page_config(page_title="SoloSync", page_icon="🌸", layout="wide")

# ---- COLOR THEME ----
primary_color = "#F4C2C2"  # pastel pink
secondary_color = "#FAD6A5"  # soft gold
accent_color = "#D8B4A6"  # dusty rose

st.markdown(f"""
    <style>
    .stApp {{ background-color: {secondary_color}; }}
    .stButton>button {{ background-color: {primary_color}; border-radius:10px; color: black; font-weight:bold; padding:10px 20px; }}
    .stTextArea>textarea {{ border-radius:10px; }}
    </style>
""", unsafe_allow_html=True)

# ---- HEADER ----
st.title("🌸 SoloSync: Empowering Solo Women")
st.subheader("Your companion for safe and fun solo adventures!")
st.write("Explore destinations, track your mood, complete challenges, and stay safe while traveling.")

# ---- DUMMY LOGIN ----
st.sidebar.header("Login")

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "username" not in st.session_state:
    st.session_state["username"] = ""

# Input fields
st.session_state["username"] = st.sidebar.text_input("Username", value=st.session_state["username"])
password_input = st.sidebar.text_input("Password", type="password")  # dummy, not checked

# Dummy login button
if st.sidebar.button("Login"):
    st.session_state["logged_in"] = True
    st.success(f"Welcome, {st.session_state['username']}!")

# ---- MAIN APP ----
if st.session_state["logged_in"]:

    # ---- LOGOUT BUTTON ----
    if st.sidebar.button("Logout"):
        st.session_state["logged_in"] = False
        st.experimental_rerun()

    # ---- SIDEBAR MENU ----
    st.sidebar.header("Menu")
    page = st.sidebar.radio("Go to", ["Home", "Mood Explorer", "Challenges", "Micro Connect", "Safety Hub", "Travel Journal", "Destinations"])

    # ---- HOME PAGE ----
    if page == "Home":
        st.image("https://images.unsplash.com/photo-1507525428034-b723cf961d3e", use_column_width=True)
        st.write("Welcome! Choose a section from the sidebar to explore your solo travel journey.")

    # ---- MOOD EXPLORER ----
    if page == "Mood Explorer":
        st.header("🌈 Mood Explorer")
        mood = st.selectbox("Select your mood today:", ["Happy 😄", "Adventurous 🏞️", "Excited ✈️", "Relaxed 🧘‍♀️", "Anxious 😟"])
        
        activities = {
            "Happy 😄": ["Visit a local museum", "Try a cafe nearby", "Join a dance class"],
            "Adventurous 🏞️": ["Go hiking", "Try a water sport", "Explore a nearby park"],
            "Excited ✈️": ["Check local events", "Go city hopping", "Take a guided tour"],
            "Relaxed 🧘‍♀️": ["Beach walk", "Yoga session", "Spa visit"],
            "Anxious 😟": ["Visit a safe popular spot", "Attend a workshop", "Go to a coffee shop with good reviews"]
        }
        
        st.write(f"Based on your mood **{mood}**, here are activities you can explore nearby:")
        for act in activities[mood]:
            st.markdown(f"- {act}")

    # ---- CHALLENGES ----
    if page == "Challenges":
        st.header("🎯 Solo Challenges")
        challenges = [
            {"task": "Talk to a local today", "points": 10, "badge": "Social Butterfly"},
            {"task": "Try a new dish", "points": 5, "badge": "Food Explorer"},
            {"task": "Take a photo of a landmark", "points": 8, "badge": "Photographer"},
            {"task": "Write a travel journal entry", "points": 5, "badge": "Writer"},
            {"task": "Share a tip with another traveler", "points": 7, "badge": "Helper"}
        ]
        
        total_points = 0
        earned_badges = []
        confetti_triggered = False
        
        for c in challenges:
            if st.checkbox(c["task"]):
                total_points += c["points"]
                earned_badges.append(c["badge"])
                confetti_triggered = True
        
        st.write(f"🏆 Total Points Earned: {total_points}")
        if earned_badges:
            st.write(f"🎖️ Badges Earned: {', '.join(earned_badges)}")
        
        if confetti_triggered:
            st.balloons()

    # ---- MICRO CONNECT ----
    if page == "Micro Connect":
        st.header("🤝 Micro Connect")
        st.write("Post your activity request and meet safely with other travelers!")
        
        activity_request = st.text_input("What would you like to do?")
        if st.button("Post Request"):
            if activity_request.strip() != "":
                st.success(f"Your request '{activity_request}' has been posted! 🚀")
                st.balloons()
            else:
                st.warning("Please write something before posting.")

    # ---- SAFETY HUB ----
    if page == "Safety Hub":
        st.header("🛡️ Safety Hub")
        st.subheader("Emergency Contacts")
        st.write("- Local police: 100")
        st.write("- Women Helpline: 1091")
        
        if st.button("Panic Alert 🚨"):
            st.error("Panic alert sent! Help is on the way!")
            st.balloons()
        
        if st.button("SOS 🆘"):
            st.error("SOS activated! Authorities notified!")
            st.balloons()

    # ---- TRAVEL JOURNAL ----
    if page == "Travel Journal":
        st.header("📓 Travel Journal")
        journal_entry = st.text_area("Write your travel experience:")
        if st.button("Post Entry"):
            if journal_entry.strip() != "":
                st.success("Your entry has been posted! 🌸")
                st.balloons()
            else:
                st.warning("Please write something before posting.")

        st.subheader("Read entries from other travelers")
        sample_entries = [
            "Visited Kyoto last month, loved the temples! 🏯",
            "Tried surfing in Bali, so much fun! 🏄‍♀️",
            "Explored Reykjavik, very safe and welcoming. ❄️"
        ]
        for e in sample_entries:
            st.markdown(f"- {e}")

    # ---- DESTINATIONS ----
    if page == "Destinations":
        st.header("🌍 Solo-Friendly Destinations")
        
        destinations = [
            {"name": "Kyoto, Japan", "type": "Cultural", "tip": "Safe public transport and friendly locals.", "image":"https://images.unsplash.com/photo-1551024709-8f23befc6e24"},
            {"name": "Reykjavik, Iceland", "type": "Adventure", "tip": "Very safe for solo women travelers.", "image":"https://images.unsplash.com/photo-1549887535-51dbdf0f2e59"},
            {"name": "Barcelona, Spain", "type": "City", "tip": "Stay in central areas and explore safely.", "image":"https://images.unsplash.com/photo-1507525428034-b723cf961d3e"},
            {"name": "Bali, Indonesia", "type": "Beach", "tip": "Popular with solo travelers; stay in well-reviewed hotels.", "image":"https://images.unsplash.com/photo-1507525428034-b723cf961d3e"},
        ]
        
        if st.button("🎲 Surprise Me!"):
            dest = random.choice(destinations)
            st.subheader(dest["name"])
            st.image(dest["image"], use_column_width=True)
            st.write(dest["tip"])
        
        for dest in destinations:
            with st.container():
                st.image(dest["image"], width=300)
                st.subheader(dest["name"])
                st.write(f"Type: {dest['type']}")
                st.info(dest["tip"])

else:
    st.warning("Please login to access SoloSync.")
