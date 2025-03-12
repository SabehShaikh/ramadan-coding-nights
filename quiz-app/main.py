import streamlit as st

st.set_page_config(layout="wide" , page_title="Pakistan Quiz App", page_icon="🇵🇰")

# Title
st.title("📝 Quiz Application")


# Quiz questions
questions = [
    {
        "question": "What is the capital of Pakistan?", 
        "options": ["Lahore", "Karachi", "Islamabad", "Peshawar"], 
        "answer": "Islamabad"
    },
    {
        "question": "Who is the founder of Pakistan?", 
        "options": ["Allama Iqbal", "Liaquat Ali Khan", "Muhammad Ali Jinnah", "Benazir Bhutto"], 
        "answer": "Muhammad Ali Jinnah"
    },
    {
        "question": "Which is the national language of Pakistan?", 
        "options": ["Punjabi", "Urdu", "Sindhi", "Pashto"],
        "answer": "Urdu"
    },
    {
        "question": "What is the currency of Pakistan?",
        "options": ["Rupee", "Dollar", "Taka", "Riyal"], 
        "answer": "Rupee"
    },
    {
        "question": "Which city is known as the City of Lights in Pakistan?", 
        "options": ["Lahore", "Islamabad", "Faisalabad", "Karachi"], 
        "answer": "Karachi"
    },
    {
        "question": "Which river is the longest in Pakistan?",
        "options": ["Indus", "Jhelum", "Chenab", "Ravi"], 
        "answer": "Indus"
    },
    {
        "question": "Which is the highest mountain in Pakistan?",
        "options": ["Nanga Parbat", "K2", "Broad Peak", "Gasherbrum"], 
        "answer": "K2"
    },
    {
        "question": "Which city is famous for producing sports goods in Pakistan?",
        "options": ["Sialkot", "Lahore", "Karachi", "Multan"],
        "answer": "Sialkot"
    }
]

if "current_index" not in st.session_state:
    st.session_state.current_index = 0
    st.session_state.score = 0
    st.session_state.show_feedback = False
    st.session_state.feedback = ""


def show_question():
    question = questions[st.session_state.current_index]
    
    st.progress((st.session_state.current_index + 1) / len(questions))


    st.subheader(f"Question {st.session_state.current_index + 1}: {question['question']}")
    selected_option = st.radio("Choose your answer", question["options"], key=st.session_state.current_index)

    if st.button("Submit Answer"):
        if selected_option:
            if selected_option == question["answer"]:
                st.session_state.feedback = "✅ Correct!"
                st.session_state.score += 1
            else:
                st.session_state.feedback = f"❌ Incorrect! The correct answer is {question['answer']}"
            st.session_state.show_feedback = True
        else:
            st.warning("Please select an option.")     



    if st.session_state.show_feedback:
        st.write(st.session_state.feedback)
        st.write(f"📊 Current Score: **{st.session_state.score}** / **{len(questions)}**")

        if st.button("Next Question"):
            st.session_state.current_index += 1
            st.session_state.show_feedback = False
            st.session_state.feedback = ""
            st.rerun()

def show_result():
    st.success(f"🎉 Quiz Completed! Your score is {st.session_state.score} out of {len(questions)}.")

    # Feedback based on results
    if st.session_state.score == len(questions): # all answered correctly
        st.balloons()
        st.write("🏆 Excellent! You're a quiz master!")
    elif st.session_state.score >= len(questions) / 2: # at least half correct
        st.write("👍 Good job! But there's room for improvement.")
    else:
        st.write("😔 Better luck next time! Keep learning.")

    if st.button("Restart Quiz"):
        st.session_state.current_index = 0
        st.session_state.score = 0
        st.session_state.show_feedback = False
        st.session_state.feedback = ""
        st.rerun()

if st.session_state.current_index < len(questions):
    show_question()
else:
    show_result()

# Footer
st.markdown("""
    <hr>
    <p style='text-align: center;'>
        Quiz App by <a href='https://github.com/sabehshaikh'>Sabeh Shaikh</a>
    </p>
""", unsafe_allow_html=True)
