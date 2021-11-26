import boto3
import posixpath
import os
import tarfile
import var
from boto3.s3.transfer import S3Transfer

def tardir(path, tar_name):
    print("Compressing...")
    with tarfile.open(tar_name, "w:gz") as tar_handle:
        for root, dirs, files in os.walk(path):
            for file in files:
              tar_handle.add(os.path.join(root, file))
              
def upload():
    BUCKET_NAME = input("Enter the Bucket Name: ")
    print("Uploading...")
    client = boto3.client('s3', aws_access_key_id=var.ACCESS_KEY,aws_secret_access_key=var.SECRET_KEY)
    transfer = S3Transfer(client)
    transfer.upload_file(tarname, BUCKET_NAME, 'backup/{}.tar.gz'.format(tarname))
    print("Uploading have been completed")

directory = input("Enter the Directory/File path : ")
tarname = input("Enter a name for the compressed file: ")
tardir(directory, tarname)
upload()

print("Removing the compressed file stored in local end ...")
os.remove(tarname)
print("All the process have been Completed!!")
