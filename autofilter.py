"""@Author: Shinzzo"""
   
#   Useful Modules.
import os,collections

#   Some Useful File Extensions.
audio = ('mp3', 'wav', 'midi')
video = ('mp4', 'mpg', 'mpeg', 'avi', 'mov', 'flv', 'mkv', 'm4v', 'h264')
images  = ('png', 'jpg', 'jpeg', 'gif', 'svg', 'bmp', 'svg',)
documents  = ('txt', 'pdf', 'doc', 'docx', 'html', 'ppt', 'pptx', 'log')
compressed = ('zip', '7z', 'rar', 'tar', 'gz', 'rpm', 'pkg', 'deb')
executables = ('dmg', 'exe', 'iso')



    

#   Main Function that creates directories.
def main():
    cwd = os.path.expanduser('~')
    DEST_DIRS = ('Music', 'Movies', 'Pictures', 'Documents', 'Applications', 'Other')

    for d in DEST_DIRS:
        dir_path = os.path.join(cwd, d)
        if not os.path.isdir(dir_path):
            os.mkdir(dir_path)

    DOWNLOADS_PATH = os.path.join(cwd, 'Downloads')
    files_mapping = collections.defaultdict(list)
    files_list = os.listdir(DOWNLOADS_PATH)

    for file_name in files_list:
        if file_name[0] != '.':
            file_ext = file_name.split('.')[-1]
            files_mapping[file_ext].append(file_name)

#   Starts the script.            
if __name__=="__main__":
    main()