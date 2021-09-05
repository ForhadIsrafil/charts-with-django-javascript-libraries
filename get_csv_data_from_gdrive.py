import pandas as pd
from googleapiclient.http import MediaIoBaseDownload
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
import io


# pattern 1
from google.oauth2 import service_account
from googleapiclient.discovery import build

service_account_file = 'client_cred.json'
SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = service_account_file
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('drive', 'v3', credentials=credentials)

topFolderId = '1LCLNvi_udMgPNx2gfAMc-YKLEWG08RBD'  # Please set the folder of the top folder ID.

items = []
pageToken = ""
while pageToken is not None:
    response = service.files().list(q="'" + topFolderId + "' in parents", pageSize=1000, pageToken=pageToken,
                                    fields="nextPageToken, files(id, name)").execute()
    items.extend(response.get('files', []))
    pageToken = response.get('nextPageToken')

print(items)

file_id = '1mBysFNU1MfOsjnsh9qqW6o_GEww1jApR'
request = service.files().get_media(fileId=file_id)

fh = io.BytesIO()
downloader = MediaIoBaseDownload(fh, request)
done = False
while done is False:
    status, done = downloader.next_chunk()
    print("Download %d%%." % int(status.progress() * 100))

with open('haha.csv', 'wb') as img_file:
    img_file.write(fh.getbuffer())
# pattern 1 end


# pattern 2
# from google.oauth2 import service_account
# from getfilelistpy import getfilelist
#
# SCOPES = ['https://www.googleapis.com/auth/drive']
# SERVICE_ACCOUNT_FILE = service_account_file
# credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
#
# topFolderId = '1LCLNvi_udMgPNx2gfAMc-YKLEWG08RBD'  # Please set the folder of the top folder ID.
# resource = {
#     "service_account": credentials,
#     "id": topFolderId,
#     "fields": "files(name,id)",
# }
# res = getfilelist.GetFileList(resource)
# # print(dict(res))
#
#
# from getfilelistpy import getfilelist
#
# resource = {
#     "api_key": "AIzaSyAl-oB2vb0N15RoNou2_lsPPrPBz8opwTk",
#     "id": topFolderId,
#     "fields": "files(*)",
# }
# res = getfilelist.GetFileList(resource)  # or r = getfilelist.GetFolderTree(resource)
# print(dict(res))
# pattern 2 end
# api-key: 'AIzaSyAl-oB2vb0N15RoNou2_lsPPrPBz8opwTk'

# # URL = 'https://drive.google.com/file/d/1m0mAGzpeMR0W-BDL5BtKrs0HOZsPIAbX/view?usp=sharing'
# URL = 'https://drive.google.com/file/d/1nikVbuzuJd4sD0yIJvEyh7hk0EBYm-ro/view?usp=sharing'
# path = 'https://drive.google.com/uc?export=download&id='+URL.split('/')[-2]
# #df = pd.read_pickle(path)
# df = pd.read_csv(path)
# print(df.head())
