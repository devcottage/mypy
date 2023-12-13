import glob, sys, os


# example:
#   import subprocess
#   wd = subprocess.run('pwd', stdout=subprocess.PIPE).stdout.decode().strip()
#   augment_sys_path(wd, True)
#
def augment_sys_path(path, recursive = False):
    if not path in set(sys.path) and os.path.isdir(path) and os.path.exists(path):
        sys.path.append(path)

    if recursive:
        for filename in glob.iglob(path, recursive=True):
            if os.path.isdir(filename) and os.path.exists(filename) and not filename in sys.path: 
                sys.path.append(filename)

    return sys.path

