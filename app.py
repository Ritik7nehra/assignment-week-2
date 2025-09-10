import streamlit as st
import numpy as np
from apputil import ways, lowest_score, sort_names

st.title("Week 2 Exercises")

exercise = st.selectbox("Choose an exercise:", ["Coins (ways)", "Student Scores"])

if exercise == "Coins (ways)":
    amount = st.number_input("Enter an amount (in cents):", min_value=0, step=1)
    if amount is not None:
        result = ways(amount)
        st.success(f"There are {result} different ways to make {amount} cents using pennies and nickels.")

elif exercise == "Student Scores":
    st.write("### Add student names and scores")

    # Initialize session state for names and scores
    if 'names' not in st.session_state:
        st.session_state.names = []
    if 'scores' not in st.session_state:
        st.session_state.scores = []

    # Input fields
    name_input = st.text_input("Student Name")
    score_input = st.number_input("Student Score", min_value=0, max_value=100, step=1)

    # Add student button
    if st.button("Add Student"):
        if name_input and score_input >= 0:
            st.session_state.names.append(name_input)
            st.session_state.scores.append(score_input)
            st.success(f"Added {name_input} with score {score_input}")

    # Display current dataset
    if st.session_state.names:
        st.write("### Current Dataset")
        st.write({"Names": st.session_state.names, "Scores": st.session_state.scores})

    # Analysis buttons
    if st.button("Find Lowest Score") and st.session_state.names:
        names_array = np.array(st.session_state.names)
        scores_array = np.array(st.session_state.scores)
        st.info(f"Lowest score student: {lowest_score(names_array, scores_array)}")

    if st.button("Sort by Scores") and st.session_state.names:
        names_array = np.array(st.session_state.names)
        scores_array = np.array(st.session_state.scores)
        sorted_names = sort_names(names_array, scores_array)
        st.success(f"Students sorted by score: {sorted_names}")
