import os

class TransferData:

    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
    dbx = dropbox.Dropbox(self.access_token)

    with open(local_path, 'rb')as f:
        dbx.files_upload(f.read(),dropbox_path, mode=WriteMode('overwrite'))

    relative_path = os.path.relpath(local_path, file_from)
    dropbox_path = os.path.join(file_to, relative_path)

    for root, dirs, files in os.walk(file_from):
        for name in files:
            print(os.path.join(root, name))
        for name in dirs:
            print(os.path.join(root, name))

def main():
    access_token='sl.BKLXSbxKtjcaParvilEjWRxir_DWcBI76-JL966p64PAH3SEEAs-LoB9y9y83rv-rxa1__9mhyUB8QYaLsZgauqo1sSt-_qbhhdUJMWVszD-WbYijWfV5wajzH5scC49T7dsvOtDXaA'
    transferData=TransferData(access_token)

    file_from=input('Enter the file path to transfer')
    file_to=input('Enter the full path to upload to the dropbox')

    transferData.upload_file(file_from, file_to)

main()  

