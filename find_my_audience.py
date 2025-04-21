import streamlit as st

st.set_page_config(page_title="Find My Audience", layout="centered")

st.title("📣 Find My Audience Agent")
st.write("This app helps you identify your ideal audience for books, courses, or products.")

# Basic Inputs
platform = st.selectbox("Where are you trying to sell?", ["Amazon", "Redbubble", "BentBox", "Patreon", "Other"])
genre = st.text_input("What genre or topic are your creations in?")
audience_type = st.selectbox("Who's your ideal customer?", ["Teens", "Adults", "Seniors", "Niche Hobbyists", "General Readers", "Other"])
goal = st.text_area("What's your goal? (e.g., grow email list, drive sales, get reviews, etc.)")

# Audience Finder Logic
if st.button("🔍 Find My Audience"):
    st.subheader("🔎 Suggested Audience Strategy")
    st.write(f"**Platform:** {platform}")
    st.write(f"**Genre/Topic:** {genre}")
    st.write(f"**Ideal Audience:** {audience_type}")
    st.write(f"**Goal:** {goal}")

    st.markdown("---")
    st.markdown("### 💡 Tips & Strategy")
    
    st.markdown("- Use keyword tools (e.g., Google Trends, Amazon Suggest, or Reddit search) to find what your audience is searching for.")
    st.markdown("- Join Facebook groups, Discord servers, and subreddits where your audience hangs out.")
    st.markdown("- Create short-form videos (TikTok, Reels, YouTube Shorts) speaking to your audience.")
    st.markdown("- Offer a lead magnet (like a free chapter or mini ebook) to collect email addresses.")
    st.markdown("- Use hashtags related to your genre and audience on social platforms.")