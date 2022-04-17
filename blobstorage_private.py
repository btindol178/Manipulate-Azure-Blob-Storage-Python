from distutils.command.upload import upload
import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__


try:
    print("Azure Blob Storage v" + __version__ + " - Python quickstart sample")

    # Quick start code goes here

except Exception as ex:
    print('Exception:')
    print(ex)
    # DO THIS IN THE CMD
    #set AZURE_STORAGE_CONNECTION_STRING = <connection string>

# pip install azure-storage-blob
# Might not need os.getenv
connect_str = "<connection string>"

print("The connection string is: ",connect_str)

# Create the BlobServiceClient object which will be used to create a container client
blob_service_client = BlobServiceClient.from_connection_string(connect_str)
print("The blob service client is: ",blob_service_client)

#############################################################################################################################################################################
##############################################################################################################################################################################
# Create a container
##############################################################################################################################################################################
# # Create a unique name for the container
# container_name = str(uuid.uuid4())
# print("The container name is: ",container_name)

# # Create the container
# container_client = blob_service_client.create_container(container_name)
# print("The container client is: ",container_client)

#############################################################################################################################################################################
#############################################################################################################################################################################
# UPLOAD BLOBS TO CONTAINER
#############################################################################################################################################################################
# Create a local directory to hold blob data
local_path = "./data" # make new folder
os.mkdir(local_path)

#Try to get the current working directory without creating new folder (not that that matters too much!! )
# upload_file_path = os.getcwd()
# upload_file_path =os.path.abspath(os.getcwd())
# print("New upload",upload_file_path)

# Create a file in the local data directory to upload and download
local_file_name = "blake.txt" #str(uuid.uuid4()) + ".txt"
print("Local file name is :",local_file_name)

upload_file_path = os.path.join(local_path, local_file_name)
print("Upload file path is: ",upload_file_path)

# Write text to the file
file = open(upload_file_path, 'w')
file.write("Hello, World!")
file.close()

# Pick container name 
container_name = "form-recognizer/forms"
print("Container name is :",container_name)

# Create a blob client using the local file name as the name for the blob
blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)
print("The blob client is: ",blob_client)

print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)

# Upload the created file
with open(upload_file_path, "rb") as data:
    blob_client.upload_blob(data)



#############################################################################################################################################################################
#############################################################################################################################################################################
# List Blobs in Container
#############################################################################################################################################################################
# Create the container connection

connect_str = " <connection string>"

from azure.storage.blob import ContainerClient

container = ContainerClient.from_connection_string(conn_str=connect_str, container_name="form-recognizer")

blob_list = container.list_blobs()
for blob in blob_list:
    print(blob.name + '\n')
#############################################################################################################################################################################
#############################################################################################################################################################################
# Downloading a file from the blob
#############################################################################################################################################################################
blob = BlobClient.from_connection_string(conn_str=connect_str, container_name="form-recognizer/forms", blob_name="blake.txt")

with open("./DownloadBlob.txt", "wb") as my_blob:
    blob_data = blob.download_blob()
    blob_data.readinto(my_blob)


#############################################################################################################################################################################
# NEXT FIGURE OUT HOW TO DELETE A BLOB IN THE CONTAINER!!!!!!!!!!!!!!!!!!!!!!!!!!!!! LEFT OFF!! 
#############################################################################################################################################################################
#DELETE A SPECIFIC BLOB FROM THE CONTAINER (name from uuid line 53)
#container.delete_blob(container_name,"sample.txt")


#############################################################################################################################################################################
#############################################################################################################################################################################
# Delete a Blob container
#############################################################################################################################################################################
import time
time.sleep(10) # Allow the blob to show up in the folder 


# Make sure you change the container client to the forms directory!!!! 
container_delete = ContainerClient.from_connection_string(conn_str=connect_str, container_name="form-recognizer/forms")
container_delete.delete_blob(blob="blake.txt")
print("Deleted blake blob!! ")
