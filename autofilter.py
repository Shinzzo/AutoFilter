"""@Author: Shinzzo"""
   
#   Useful Modules
import os,collections

#   Some Useful File Extensions.
audio = ('mp3', 'wav', 'midi')
video = ('mp4', 'mpg', 'mpeg', 'avi', 'mov', 'flv', 'mkv', 'm4v', 'h264')
images  = ('png', 'jpg', 'jpeg', 'gif', 'svg', 'bmp', 'svg',)
documents  = ('txt', 'pdf', 'doc', 'docx', 'html', 'ppt', 'pptx', 'log')
compressed = ('zip', '7z', 'rar', 'tar', 'gz', 'rpm', 'pkg', 'deb')
executables = ('dmg', 'exe', 'iso')

def main():
    BASE_PATH = os.path.expanduser('~')
    DEST_DIRS = ('Music', 'Movies', 'Pictures', 'Documents', 'Applications', 'Other')

    for d in DEST_DIRS:
        dir_path = os.path.join(BASE_PATH, d)
        if not os.path.isdir(dir_path):
            os.mkdir(dir_path)
if __name__=="__main__":
    main()