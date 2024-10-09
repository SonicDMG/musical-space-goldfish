# app.py

import streamlit as st
from api import get_bot_response

def main():
    st.title("Basic Chatbot App")

    if 'messages' not in st.session_state:
        st.session_state['messages'] = []

    user_input = st.text_input("You: ", key="input")

    if st.button("Send"):
        if user_input:
            st.session_state['messages'].append(f"You: {user_input}")
            with st.spinner('Waiting for bot response...'):
                bot_response = get_bot_response(user_input)
            st.session_state['messages'].append(f"Bot: {bot_response}")

    # Display the latest bot response in a persistent location
    if st.session_state['messages']:
        st.subheader("Latest Response")
        st.write(st.session_state['messages'][-1])

    # Display chat history with a limit to scroll away older messages
    st.subheader("Chat History")
    for message in st.session_state['messages'][-10:]:  # Display only the last 10 messages
        st.write(message)

if __name__ == "__main__":
    main()
