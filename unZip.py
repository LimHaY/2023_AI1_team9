
import os
import zipfile


directories = [
    'D:/AI1/family_dataset/1.Training/label',
    'D:/AI1/family_dataset/1.Training/original',
    'D:/AI1/family_dataset/2.Validation/label',
    'D:/AI1/family_dataset/2.Validation/original'
]

for directory in directories:
    for current in os.listdir(directory):
        # 전체 경로(.zip까지)
        path = os.path.join(directory, current)
        # path = "./family_dataset/2.Validation/original\VS0900.zip"
        if path[-4:] == '.zip': # 압축 파일(.zip)인 경우
            if not os.path.isdir(path[:-4]):
                print(path)
                compressed = zipfile.ZipFile(path)
                # 동일한 위치에 압축 해제(압축 파일의 이름으로 폴더 생성)
                compressed.extractall(path[:-4])
                compressed.close()