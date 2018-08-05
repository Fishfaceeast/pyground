import os
import time

source = ['/Users/yuqian/git/core']
target_dir = '/Users/yuqian/git/core_bak'

sub_dir = target_dir + os.sep + time.strftime('%Y%m%d')
target = sub_dir + os.sep + time.strftime('%H%M%S') + '.zip'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

if not os.path.exists(sub_dir):
    os.mkdir(sub_dir)

zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))

print('Zip command is:')
print(zip_command)
print('Running')
if os.system(zip_command) == 0:
    print('successfully backup to ', target)
else:
    print('backup failed')


