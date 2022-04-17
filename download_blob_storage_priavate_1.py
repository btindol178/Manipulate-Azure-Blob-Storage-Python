from datetime import datetime, timedelta
import pandas as pd
from azure.storage.blob import BlobSasPermissions, generate_blob_sas
import azure.functions as func # pip install azure-functions


# def main(req: func.HttpRequest) -> func.HttpResponse:
account_name = '<account name>'
account_key = '<account key>'
container_name = '<container name and sub folder if have it '
blob_name="Sample.xlsx"
sas=generate_blob_sas(
      account_name=account_name,
      container_name=container_name,
      blob_name=blob_name,
      account_key=account_key,
      permission=BlobSasPermissions(read=True),
      expiry=datetime.utcnow() + timedelta(hours=1)
)
print(sas)
blob_url = f'https://{account_name}.blob.core.windows.net/{container_name}/{blob_name}?{sas}'
print(blob_url)
df=pd.read_excel(blob_url)
print(df)
