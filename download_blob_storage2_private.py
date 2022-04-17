from datetime import datetime, timedelta
import pandas as pd
from azure.storage.blob import BlobSasPermissions, generate_blob_sas
import azure.functions as func # pip install azure-functions
from azure.storage.blob import  BlobServiceClient

account_name = '<account name>'
account_key = '<account key>'

blob_service_client = BlobServiceClient(account_url=f'https://{account_name }.blob.core.windows.net/', credential=account_key)
blob_client = blob_service_client.get_blob_client(container='form-recognizer/forms', blob='Sample.xlsx')
downloader =blob_client.download_blob()
df=pd.read_excel(downloader.readall())
print(df)