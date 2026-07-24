import requests
from config import API_URL


# # for multiple file upload :
# def upload_pdfs_api(files):
#     # Creates a list of tuples, one for each uploaded PDF.
#     # Each tuple contains:
#     # ("files", (filename, file_object, MIME type))
#     files_payload = [("files", (f.name, f.read(), "application/pdf")) for f in files]
#
#     # Sends a POST request with multipart/form-data containing all PDFs.
#     return requests.post(f"{API_URL}/upload_pdfs/", files=files_payload)


# for single file :
def upload_pdf_api(file):
    # Creates the payload required for multipart/form-data.
    # Format:
    # {
    #     "file": (filename, file_object, content_type)
    # }
    # "file" must match the UploadFile parameter name in the FastAPI endpoint.
    file_payload = {"file": (file.name, file, "application/pdf")}

    # Sends the uploaded PDF to the backend upload endpoint.
    return requests.post(f"{API_URL}/upload_pdf/", files=file_payload)


def ask_question(question):
    # Sends the user's question as form data to the backend.
    # The backend receives it as:
    # question: str = Form(...)
    return requests.post(
        f"{API_URL}/ask/",
        data={"question": question}
    )