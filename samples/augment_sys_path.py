import glob, sys, os


# example:
#   import subprocess
#   wd = subprocess.run('pwd', stdout=subprocess.PIPE).stdout.decode().strip()
#   augment_sys_path(wd, True)
#
def augment_sys_path(path, recursive = False):
    current_paths = tuple(set(filter(lambda x :not x == '', sys.path)))

    if (not path in current_paths and not path.rstrip('/') in current_paths and os.path.isdir(path) and os.path.exists(path)):
        sys.path.append(path)

    if recursive:
        for filename in glob.iglob(path, recursive=True):
            if (os.path.isdir(filename) and os.path.exists(filename) 
                    and not (filename in current_paths or filename.rstrip('/') in current_paths) and not os.path.basename(filename).startswith(tuple(["_","."]))):
                sys.path.append(filename)

    return sys.path

