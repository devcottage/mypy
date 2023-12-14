import augment_sys_path as augment
import sys, subprocess

wd = subprocess.run('pwd', stdout=subprocess.PIPE).stdout.decode().strip()
orig = tuple(sys.path)
print(orig)

augmented = augment.augment_sys_path(wd + "/**", recursive=True)
print(augmented)
print(f"augmentation: {set(augmented) - set(orig)}")
assert(len(augmented) > 0)

print("DONE testing path augmentation")
