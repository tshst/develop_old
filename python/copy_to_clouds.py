# this program does copy of local file from local storage to multiple cloud storages.

import os
import sys
import shutil
from datetime import datetime

src_target_file = sys.argv[1]
dst_target_dir = ['/Users/tshst/OneDrive/書籍/', '/Users/tshst/Library/Mobile Documents/com~apple~CloudDocs/Books/']
filename = os.path.basename(src_target_file)

if os.path.isfile(src_target_file):
    for dst_dir in dst_target_dir:
        if not os.path.exists(dst_dir + filename):
            #print('copy file' + src_target_file, dst_dir)
            shutil.copy(src_target_file, dst_dir)
        else:
            #print('rename file' + src_target_file, dst_dir)
            os.rename(src_target_file, str(dst_target_dir) + str(datetime.now()))
    

