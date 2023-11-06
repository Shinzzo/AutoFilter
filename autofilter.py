#
#   @Author: Shinzzo
#

#   Useful Modules.
import os,collections

#   Some Useful File Extensions.
audio = ('mp3', 'wav', 'midi')
video = ('mp4', 'mpg', 'mpeg', 'avi', 'mov', 'flv', 'mkv', 'm4v', 'h264')
images  = ('png', 'jpg', 'jpeg', 'gif', 'svg', 'bmp', 'svg',)
documents  = ('txt', 'pdf', 'doc', 'docx', 'html', 'ppt', 'pptx', 'log')
compressed = ('zip', '7z', 'rar', 'tar', 'gz', 'rpm', 'pkg', 'deb')
executables = ('dmg', 'exe', 'iso')
    
#   Main Function that creates directories & maps files from downloads folder based on their file extensions.
def main():
    cwd = os.path.expanduser('~')
    destindirs = ('Music', 'Movies', 'Pictures', 'Documents', 'Applications', 'Other')
    for d in destindirs:
        dir_path = os.path.join(cwd, d)
        if not os.path.isdir(dir_path):
            os.mkdir(dir_path)
    #--------------------------------------------------------#
    downloads_path = os.path.join(cwd, 'Downloads')
    files_mapping = collections.defaultdict(list)
    files_list = os.listdir(downloads_path)
    for file_name in files_list:
        if file_name[0] != '.':
            file_ext = file_name.split('.')[-1]
            files_mapping[file_ext].append(file_name)
    #--------------------------------------------------------#
    for f_ext, f_list in files_mapping.items():
        if f_ext in executables:
            for file in f_list:
                os.rename(os.path.join(downloads_path, file), os.path.join(cwd, 'Applications', file))
        elif f_ext in audio:
            for file in f_list:
                os.rename(os.path.join(downloads_path, file), os.path.join(cwd, 'Music', file))
        elif f_ext in video:
            for file in f_list:
                os.rename(os.path.join(downloads_path, file), os.path.join(cwd, 'Movies', file))
        elif f_ext in images:
            for file in f_list:
                os.rename(os.path.join(downloads_path, file), os.path.join(cwd, 'Pictures', file))
        elif f_ext in documents or f_ext in compressed:
            for file in f_list:
                os.rename(os.path.join(downloads_path, file), os.path.join(cwd, 'Documents', file))
        else:
            for file in f_list:
                os.rename(os.path.join(downloads_path, file), os.path.join(cwd, 'Other', file))

#   Starts the script.            
if __name__=="__main__":
    main()