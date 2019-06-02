import os
basedir = 'D:\\Downloads\\Torrent\\Séries\\Nine-NineS06\\'


'''for fn in os.listdir(basedir):
    if not os.path.isdir(os.path.join(basedir, fn)):
        continue   # Not a directory
    if '.' not in fn:
        continue   # Invalid format
    firstname, _, surname = fn.rpartition('E')
    os.rename(os.path.join(basedir, fn), os.path.join(basedir, 'S05' + fn[0:3]))'''

for i in range(1, 18):
    os.mkdir(basedir + 'E0' + str(i))
