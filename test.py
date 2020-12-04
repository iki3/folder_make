import os
import numpy as np
from shutil import copy2
moto_path='../font_datasets_gray_yoko_copy/'
folder=os.listdir('../font_datasets_gray_yoko_copy')

print(folder)
print('----------------')
arr = np.random.randint(0, 103, 13)
print(arr)
folder=np.array(folder)
val=folder[arr]
print(len(val))
np.random.shuffle(folder)

test_data  = folder[0:13]
train_data = folder[13:103]



make_dir_path='../katakana_datasets/Capitals64/test'
print(len(test_data))
for file in test_data:
    copy2(moto_path+file,'{}/{}'.format(make_dir_path,file))

make_dir_path='../katakana_datasets/Capitals64/train'
print(len(train_data))
for file in train_data:
    copy2(moto_path+file,'{}/{}'.format(make_dir_path,file))

make_dir_path = '../katakana_datasets/Capitals64/val'
print(len(val))
for file in val:
    copy2(moto_path+file,'{}/{}'.format(make_dir_path,file))

# dore=np.random.choice(folder,13,False)
# print(dore)
# make_dir_path='koko'
# for file in dore:
#     copy2(moto_path+file,'{}/{}.png'.format(make_dir_path,file))
