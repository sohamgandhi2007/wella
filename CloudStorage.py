import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_file(self, file_from,file_to):

        dbx =dropbox.Dropbox(self.access_token)

        f=open(file_from, "rb")
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.Amr54wqvWvRtFDFa0CGFu4piXpm6bJ-BULIf112l3mxq6PAfHcC1_vdNXbv6kxS_a-_rGaOBD6ArBLP_eePc6zR8RfejT99aoLURC8SNImFIdhk0Txa6_VHcF_BSxsWSnShrjbk'
    transferData = TransferData(access_token)

    file_from = input("enter the file name you want to transfer")
    file_to=input("enter the full path on dropbox where you want to enter your file")

    transferData.upload_file(file_from,file_to)
    print("File has been moved")

main()
