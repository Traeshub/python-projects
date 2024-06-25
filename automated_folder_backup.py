import os 
import shutil
import datetime
import schedule
import time

"""specifying the source directory to backup and
and the destination the back up is going"""

source_dir = "/custom/file/path"
destination_dir = "/custom/destination/path"

# Creating the function

def copy_folder_to_directory(source, dest):
    """Copying a backup to a folder"""
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))

    try:
        shutil.copytree(source, dest_dir)
        print(f"Folder was copied to: {dest_dir}")
    except FileExistsError:
        print(f"Folder already exists in: {dest}")

# Scheduling the backup task to happen at desired time & frequency
        
schedule.every().day.at("whatever time needed").do(lambda: copy_folder_to_directory(source_dir, destination_dir))

while True:
    schedule.run_pending()  #this command looks for any schedules tasks that haven't ran
    time.sleep(60)