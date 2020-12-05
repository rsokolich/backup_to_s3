#! python3
# program to zip files to disk

import os, zipfile, datetime
import config

def backupToZip (folders):
    # Change the directory to the destination of the Zipped backup file
    os.chdir(config.temp_backup_zip)
    #Backup the entire contents of "folders" into a single zip file.
    backup_date = datetime.datetime.now().strftime("%m-%d-%Y.%H.%M")
    while True:
        config.zipFilename = 'Backup_' + str(backup_date) + '.zip'
        if not os.path.exists(config.zipFilename):
            break

    # Create Zip file.
    print('Creating %s...' % (config.zipFilename))
    backupZip = zipfile.ZipFile(config.zipFilename, 'w')

#   Walk the entire tree and compress the files in folders.
    for folder in folders:
        for foldername, subfolders, filenames in os.walk(folder):
            print('Adding files in %s...' % (foldername))
            # Add the current folder to the zip file.
            backupZip.write(foldername)
            # Add all the files in the current folder to the zip file.
            for filename in filenames:
                newBase = os.path.basename(folder) + '_'
                if filename.startswith(newBase) and filename.endswith('.zip'):
                    continue # don't backup the backup zip files.
                backupZip.write(os.path.join(foldername, filename))
    backupZip.close
    print('Done with Backups.')
    return config.zipFilename

# Delete the local zip file. 
def remove_local_backupZip(zipFilename):
    os.chdir(config.temp_backup_zip)
    try:
        if os.path.exists(zipFilename):
            os.remove(zipFilename)
            print('Temp Zip file ' + str(zipFilename) + ' deleted successfully.')
    except:
        print("Error removing local backup Zip file")
