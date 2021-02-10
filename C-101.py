import dropbox
import os.walk
import os.path

class TransferData:
   def __init__(self,access_token):
        self.access_token = access_token

    def upload_file(self, file_from,file_to):
        dbx =dropbox.Dropbox(self.access_token)

     with open(local_path, "rb") as f:
        dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))
    
for root,dirs,files in os.walk(file_from):

relative_path = os.path.relpath(local_path, file_from)
dropbox_path = os.path.join(file_to.ralative_path)

def local():
    access_token = 'YdRQz4iQUxMAAAAAAAAAAbtRw8k-gJqFz_CCZViJia_DhNRyWV7AuZfNC94KKwmr'
    transferData = TransferData(access_token)

    file_from = input("enter the file name you want to transfer")
    file_to=input("enter the full path on dropbox where you want to enter your file")

    transferData.upload_file(file_from,file_to)
    print("File has been moved")

local()