# Tasks

Task no. 2 was prepared in the main.py file
It has been tested and for it to work you need to set the access key ID and access key:
```
set AWS_ACCESS_KEY_ID=your-access-key-id
set AWS_SECRET_ACCESS_KEY=your-secret-access-key
set AWS_DEFAULT_REGION=us-east-1
``` 
If this doesn't work, you should put the id and access key directly in the main.py file, it wasn't placed there directly for security reasons

You can use commands in the CLI
```
python main.py --list  
(Lists all files in the S3 container)

python main.py --upload {path to file} test_file.txt 
(Upload a local file to a defined location in the bucket, sample file added in the repository)

python main.py --filter ".*\.txt" 
(List an AWS buckets files that match a "filter" regex)

python main.py --delete ".*\.txt"  
(Delete all files matching a regex from a bucket)
```

Task no. 3
The 'touch.env' configuration file containing the SDK configuration was sent by e-mail to protect your data, and support for it was added in the mail.py file