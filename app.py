import config
from backup_to_zip import backupToZip
from s3_upload import upload_to_aws
from backup_to_zip import remove_local_backupZip

# Enter folders to be backed up:
folders = ["D:\Office\Documents", "D:\Office\Videos", "D:\Office\Pictures"]
#folders = ["D:\Backups", "D:\Backups2", "D:\Backups3"] # test folders

# Enter destination bucket to which compressed zip file will be uploaded:
#s3_bucket = 'test-bucket-sokolich.com'
s3_bucket = 'backup-archive-sokolich.com'

# Enter location to store temp local zip file.
config.temp_backup_zip = "D:\Local Backups"


# Funtion calls that run the program:

# This function call zips backup data and uploads it to S3 bucket defined above.
upload_to_aws(backupToZip(folders), s3_bucket)

# This function call deletes zip file after upload:
remove_local_backupZip(config.zipFilename)