# backup_to_s3

### Python app to backup folders to a single zip file and upload to S3.

###### How to run the app:
    1. Copy app.py, backup_to_zip.py, config.py & s3_upload.py to a single directory 
    2. In app.py, enter the following:
        a. folders to be zipped and backed-up (folders)
        b. destination S3 bucket to which compressed zip file will be uploaded (s3_bucket)
        c. location to store temp local zip file (config.temp_backup_zip)
    3. Either schedule the app to run using Cron/Task Scheduler or execute python app.py 

**Note:** be sure to have installed and configured the AWS CLI with an IAM user or role that has S3 privileges.