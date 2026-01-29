# functions for uploading a pdf to NCBA Google Drive

import os
import io
import googleapiclient.discovery
import googleapiclient.http
import google_auth_oauthlib.flow
import google.auth.transport.requests
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle

# Define the scopes needed for the Drive API
SCOPES = ['https://www.googleapis.com/auth/drive.file']
# CLIENT_ID = "347399865297-3dufh19maj35b26bou3h7n243r5idi5q.apps.googleusercontent.com"
# API_KEY = "AIzaSyDpv1PG9ASm_cyQ1vci2E_mDwxt1Pjr8xg"

file_path = 'ADVANCE-SE_Status.pdf'  # Replace with your local file path
file_name = 'ADVANCE-SE_Status.pdf' # Desired name of the file in Google Drive
mime_type = 'application/pdf'  # Replace with the correct MIME type for your file
folder_id = '1WIDSsWddPqbxuDbWjBj7Z8cIzL2v8vdq' # Optional: Specify a folder ID to upload to a specific folder

# def main():
def upload_file_to_drive(
        file_path,
        file_name,
        mime_type = mime_type,
        folder_id = folder_id
        ):
    creds = None
    token_path = 'token.pickle'

    if os.path.exists(token_path):
        with open(token_path, 'rb') as token:
            creds = pickle.load(token)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret_347399865297-3dufh19maj35b26bou3h7n243r5idi5q.apps.googleusercontent.com.json', SCOPES)
            creds = flow.run_local_server(port=61383)
        
        with open(token_path, 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)

    file_metadata = {'name': file_name}
    if folder_id:
        file_metadata['parents'] = [folder_id]

    media = MediaIoBaseUpload(io.FileIO(file_path, 'rb'), mimetype=mime_type, resumable=True)
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print(f'File ID: "{file.get("id")}". File "{file_name}" has been uploaded to Google Drive')
    # https://drive.google.com/file/d/1O60rHXZgM85p3A-ZU3pKL6ljYeFUqhLS/view?usp=sharing

    # file_url = upload_file_to_drive(file_path, file_name, mime_type, folder_id)
    return f'https://drive.google.com/file/d/{file.get("id")}/view?usp=sharing'

# def main():
def delete_file_from_drive(
        file_id,
        ):
    creds = None
    token_path = 'token.pickle'

    if os.path.exists(token_path):
        with open(token_path, 'rb') as token:
            creds = pickle.load(token)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret_347399865297-3dufh19maj35b26bou3h7n243r5idi5q.apps.googleusercontent.com.json', SCOPES)
            creds = flow.run_local_server(port=61383)
        
        with open(token_path, 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)

    body_value = {'trashed' : True}

    file = service.files().update(fileId = file_id, body=body_value).execute()

    return f'https://drive.google.com/file/d/{file.get("id")}/view?usp=sharing'