import streamlit as st
from utils.api import ask_question


def render_chat():
    # Display the chat section heading.
    st.subheader("💬 Chat with your assistant")

    # Initialize chat history in the session state if it doesn't already exist.
    # Session state preserves data across Streamlit reruns.
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Render the existing chat history stored in the session.
    # Each message contains:
    # {
    #     "role": "user" or "assistant",
    #     "content": "Message text"
    # }
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).markdown(msg["content"])

    # Display a chat input box and wait for the user to enter a question.
    user_input = st.chat_input("Type your question....")

    # Execute only after the user submits a question.
    if user_input:

        # Immediately display the user's message in the chat interface.
        st.chat_message("user").markdown(user_input)

        # Save the user's message so it persists after the page reruns.
        st.session_state.messages.append(
            {
                "role": "user",
                "content": user_input
            }
        )

        # Send the user's question to the FastAPI backend.
        response = ask_question(user_input)

        # Check if the backend processed the request successfully.
        if response.status_code == 200:

            # Convert the JSON response into a Python dictionary.
            data = response.json()

            # Extract the generated answer from the response.
            answer = data["response"]

            # Extract the source documents if available.
            # If the "sources" key doesn't exist, return an empty list.
            sources = data.get("sources", [])

            # Display the assistant's answer in the chat window.
            st.chat_message("assistant").markdown(answer)

            # Uncomment this block if you want to display
            # the source documents used to generate the answer.
            # if sources:
            #     st.markdown("📄 **Sources:**")
            #     for src in sources:
            #         st.markdown(f"- `{src}`")

            # Save the assistant's response in the chat history.
            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": answer
                }
            )

        # Display an error message if the backend request fails.
        else:
            st.error(f"Error: {response.text}")