# Upload To AWS-S3
## (Python Script to compress and upload to S3)


[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

## Description

Nowadays, it's quite common in taking the backups and storing in a separate space as a DR plan. Here I have built a python script that will take these kinds of backups(the script will compress the directory or a file) and upload the same to S3 Bucket. Only the requirements needs from the client-side are just specifying the folder and the name of the bucket to which its needs to be updated



## Features

- Easy to configure
- Script will automate compress and upload to S3

## Modules Used

- boto3
- posixpath
- os
- tarfile

## Pre-Requests

- Basic Knowledge in Python
- Basic Knowledge in AWS Services includes IAM, S3
- IAM User needs to be created 
> [IAM User Creation Steps](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html) 
- S3 Bucket needs to be created and configured
> [S3 Bucket Creation Steps](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html)



## Behind the code

```sh
import boto3
import posixpath
import os
import tarfile
import var
from boto3.s3.transfer import S3Transfer

def tardir(path, tar_name):
    print("Compressing the File")
    with tarfile.open(tar_name, "w:gz") as tar_handle:
        for root, dirs, files in os.walk(path):
            for file in files:
              tar_handle.add(os.path.join(root, file))


def upload():
    BUCKET_NAME = input("Enter the Bucket Name: ")
    print("Uploading the File")
    client = boto3.client('s3', aws_access_key_id=var.ACCESS_KEY,aws_secret_access_key=var.SECRET_KEY)
    transfer = S3Transfer(client)
    transfer.upload_file(tarname, BUCKET_NAME, 'backup/{}.tar.gz'.format(tarname))
    print("uploading has been completed")

directory = input("Enter the Directory/File path : ")
tarname = input("Enter the Name for tar file: ")
tardir(directory, tarname)
upload()

print("Removing the locally compressed file")
os.remove(tarname)
print("All the Process Have been Completed!!")
```

## User Instructions

Update the Access key and Secret key in the file "var.py"

```sh
sudo yum install git -y
sudo yum install python3
git clone https://github.com/ajish-antony/python-s3-upload.git
cd python-s3-upload
$ python3 upload.py
```

## Script running Demonstration

```sh
python3 upload.py
Enter the Directory/File path : myproject
Enter a name for the compressed file: project-bak
Compressing...
Enter the Bucket Name: new-ajish
Uploading...
Uploading have been completed
Removing the compressed file stored in local end ...
All the process have been Completed!!
```
## Conclusion

Here I have made use of the python script for uploading into the S3 bucket, which is commonly used for backup procedures and in different projects.


### ⚙️ Connect with Me

<p align="center">
<a href="mailto:ajishantony95@gmail.com"><img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white"/></a>
<a href="https://www.linkedin.com/in/ajish-antony/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
