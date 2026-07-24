import streamlit as st


def render_history_download():

    # Check whether any chat messages exist in the current session.
    # Only display the download button if chat history is available.
    if st.session_state.get("messages"):

        # Convert the chat history into a readable text format.
        # Example:
        # USER: What is diabetes?
        #
        # ASSISTANT: Diabetes is a chronic disease...
        chat_text = "\n\n".join(
            [
                f"{m['role'].upper()}: {m['content']}"
                for m in st.session_state.messages
            ]
        )

        # Display a button that allows the user to download
        # the chat history as a plain text (.txt) file.
        st.download_button(
            "Download Chat History",
            chat_text,
            file_name="chat_history.txt",
            mime="text/plain"
        )