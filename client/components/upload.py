import streamlit as st
from utils.api import upload_pdf_api


def render_uploader():

    # Display a heading in the sidebar for the document upload section.
    st.sidebar.header("Upload a Medical document (.PDFs)")

    # Display a file uploader that accepts only PDF files.
    # accept_multiple_files=False means the user can upload
    # only one PDF at a time.
    # The uploaded file is returned as a single UploadedFile object.
    uploaded_file = st.sidebar.file_uploader(
        "Upload Medical PDF",
        type="pdf",
        accept_multiple_files=False
    )

    # Upload the selected PDF only when:
    # 1. The user clicks the "Upload DB" button.
    # 2. A PDF has been selected.
    if st.sidebar.button("Upload DB") and uploaded_file:

        # Send the uploaded PDF to the FastAPI backend,
        # where it will be processed, embedded, and stored
        # in the Pinecone vector database.
        response = upload_pdf_api(uploaded_file)

        # Check whether the backend successfully processed
        # the uploaded document.
        if response.status_code == 200:

            # Display a success message in the sidebar.
            st.sidebar.success("Uploaded successfully")

        else:

            # Display the error message returned by the backend.
            st.sidebar.error(f"Error:{response.text}")