import argparse
import boto3
from botocore.exceptions import ClientError
from dotenv import load_dotenv
import logging
import os
import re

load_dotenv('touch.env')

s3 = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    region_name=os.getenv('AWS_DEFAULT_REGION')
)

bucket_name = 'developer-task'
prefix_name = 'x-wing/'

def list_files():
    response = s3.list_objects_v2(Bucket = bucket_name, Prefix = prefix_name)
    if 'Contents' in response:
        for obj in response['Contents']:
            print(obj['Key'])

    else:
        print(f'No Contents in the bucket {bucket_name} + {prefix_name}')

def upload_file(file_path, upload_file_key):
    try:
        s3.upload_file(file_path, bucket_name, prefix_name + upload_file_key)
        print(f'Przesłano plik {file_path} jako {prefix_name + upload_file_key}')
    except ClientError as e:
        logging.error(e)
        return False
    return True

def filter_files(regex):
    pattern = re.compile(regex)
    response = s3.list_objects_v2(Bucket = bucket_name, Prefix = prefix_name)
    if 'Contents' in response:
        for obj in response['Contents']:
            if pattern.search(obj['Key']):
                print(obj['Key'])
    else:
        print("There are no files matching the pattern '" + regex + "'")

def delete_files(regex):
    pattern = re.compile(regex)
    response = s3.list_objects_v2(Bucket = bucket_name, Prefix = prefix_name)
    if 'Contents' in response:
        for obj in response['Contents']:
            if pattern.search(obj['Key']):
                key = obj['Key']
                s3.delete_object(Bucket = bucket_name, Key = key)
                print(f'Deleted {key}')
    else:
        print("There are no files to be deleted that matching the pattern '" + regex + "'")


def main():
    parser = argparse.ArgumentParser(description='CLI do zarządzania kontenerem S3')
    parser.add_argument('--list', action='store_true', help='Wyświetl wszystkie pliki kontenera S3')
    parser.add_argument('--upload', nargs=2, metavar=('file_path', 's3_key'), help='Prześlij plik do kontenera S3')
    parser.add_argument('--filter', metavar='regex', help = "regex do plik do kontenera")
    parser.add_argument('--delete', metavar='regex', help = "regex do plików do usunięcia")

    args = parser.parse_args()

    if args.list:
        list_files()
    elif args.upload:
        file_path = args.upload[0]
        upload_file_key = args.upload[1]
        upload_file(file_path, upload_file_key)
    elif args.filter:
        filter_files(args.filter)
    elif args.delete:
        delete_files(args.delete)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
