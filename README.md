# 2023_AI1_team9
#### 2023년 1학기 인공지능1 team9 기말과제
#### "가족관계가 알려진 얼굴 이미지 데이터 세트" 활용하기

## 데이터 전처리

#### 1. 모든 zip 파일 압축해제
- [소스코드](https://github.com/LimHaY/2023_AI1_team9/blob/main/unZip.py)

```
# ai hub 원본 데이터 폴더구조
  /family_dataset
    /1.Training
      /label
        TL0001to0020.zip
        TL0021to0040.zip
        ......
        TL0701to0800.zip
      /original
        TL0001to0020.zip
        TL0021to0040.zip
        ......
        TL0701to0800.zip
    /2.Validation
      /label
        VL0801.zip
        VL0802.zip
        ......
        VL0900.zip
      /original
        VL0801.zip
        VL0802.zip
        ......
        VL0900.zip
```

#### 2. 폴더 규칙 정리
- [소스코드](https://github.com/LimHaY/2023_AI1_team9/blob/main/folder_Rule.py)
- 각 친족마다 하나의 폴더로 구성됨
```
# 예시 폴더 구조
/1.Training
  /label
    TL0001
    TL0002
    ......
  /original
    TL0001
    TL0002
    ......
```
#### 3. 파일 검증
- [소스코드](https://github.com/LimHaY/2023_AI1_team9/blob/main/kinship_type.py)
- 각 폴더 내에는 친가(A) 또는 외가(B) 폴더만 존재함
```
# 예시 폴더 구조
/VS0801
  /A(친가)
    /1.Family
    /2.Individuals
    /3.Age
  /B(외가)
    /1.Family
    /2.Individuals
    /3.Age
```
#### 4. /3.Age 폴더 내 이미지만 사용하여 데이터세트 구축
- [소스코드](https://github.com/LimHaY/2023_AI1_team9/blob/main/select_used_files.py)
- /3.Age 폴더에는 인물의 나이대별 얼굴 이미지가 포함됨
- 이미지 파일명 : (가족고유번호) _ AGE _ (가족내지위) _ (나이유형).jpg
- custom_dataset.csv 는 27809개의 이미지에 대한 메타정보를 가진다
  - 속성 : 'family_id', 'person_id', 'age_class', 'image_path'
#### 5. 이미지 크기 줄이기
- [소스코드](https://github.com/LimHaY/2023_AI1_team9/blob/main/resize_image.py)
- 256 * 256 크기로 사이즈 줄이기
#### 6. 학습 데이터 세트 만들기
- [소스코드](https://github.com/LimHaY/2023_AI1_team9/blob/main/make_fixed_test_dataset.py)
- train group : F0001 ~ F0727 , 22,427개 이미지
- validataion group : F0728 ~ F0812 , 2712 개 이미지
- test group : F0813 ~ F0900 , 2670 개 이미지
- 평가를 위하여 validataion group과 test group은 각 5000쌍의 가족(positive)과 5000쌍의 비가족(negative)으로 구성됨

### 최종적으로 전처리된 데이터 세트
custom_family_dataset.zip
```
/custom_family_dataset
  /fixed_test_dataset
    /negative
      /0
        F0818_AGE_S_35_a1.jpg
        F0819_AGE_F_57_e1.jpg
      /1
      ......
      /5000
    /positive
      /0
        F0856_AGE_D_50_e2.jpg
        F0856_AGE_M_75_g3.JPG
      /1
      ......
      /5000
  /fixed_val_dataset
    /negative
    /positive
  /train_images
    F0001_AGE_D_18_a1.jpg
    F0001_AGE_D_18_a2.jpg
    ......
  custom_dataset.csv
  custom_test_dataset.csv
  custom_train_dataset.csv
  custom_val_dataset.csv
```

## 가족관계 예측 모델 구축
- [weighted_kinship_verification_12epoch.ipynb](https://github.com/LimHaY/2023_AI1_team9/blob/main/weighted_kinship_verification_12epoch.ipynb) accuracy : 0.61
- siamese network 활용
- 가족 내 지위에 따른 가중치 부여
- 지위: "GF", "GM", "F", "M", "S", "D", "S2", "S3", "S4", "D2", "D3", "D4"
```
GF: 할아버지
GM: 할머니
F: 아버지
M: 어머니
S: 아들
D: 딸
```


