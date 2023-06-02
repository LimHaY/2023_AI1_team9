### 폴더 규칙 맞지 않는 폴더 정리
import shutil

directories = [
    'D:/AI1/family_dataset/1.Training/label',
    'D:/AI1/family_dataset/1.Training/original',
]

for directory in directories:
    for i in os.listdir(directory):
        if 'to' in i and i[-4:] != '.zip':
            path = os.path.join(directory,i)
            for j in os.listdir(path):
                shutil.move(os.path.join(path,j),os.path.join(directory,j))
#                 print(os.path.join(path,j))
#                 print(os.path.join(directory,j))
            if len(os.listdir(path)) == 0 :
                print(path)
                os.rmdir(path)
        