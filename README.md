# 논문 요약 및 중요단어 NLP

### 1. 프로젝트 개요
+ 논문을 읽는것에 어려움을 느껴 해당 프로젝트를 기획
+ 논문에서 이해하기 힘들거나 새로운 단어가 keypoint 일 경우가 다수
+ 논문의 핵심 내용이 제목에 표현됨으로 논문의 내용의 핵심내용이 제목을 담당할 것이라고 가정
+ 논문의 내용을 토대로 타겟값을 논문의 제목으로 설정

### 2. 데이터셋
+ train data : 29개의 deep Learning 및 machine learning 논문
+ test data : 7개의 deep Learning 및 machine learning 논문
+ title : 논문의 제목
+ detail : 논문의 내용

### 2. 모델
+ tokenizer
+ Bahdanau Attention

### 3. 프로젝트 설명
+ title과 detail을 각각 token화 진행
+ 전체 단어 빈도수 파악

![image](https://user-images.githubusercontent.com/74826174/189719881-54733074-fe1f-40d1-9bf4-cc1a80dc43dd.png)

![image](https://user-images.githubusercontent.com/74826174/189719903-9c246753-8c3f-4277-b50f-8d213ae89742.png)

+ 전체 논문의 텍스트 평균길이 파악

![image](https://user-images.githubusercontent.com/74826174/189720008-36d229d5-52dd-420e-9558-86dfc4dd2a40.png)

![image](https://user-images.githubusercontent.com/74826174/189719958-2bc0599e-27cb-4b45-9381-ceddae9d61ec.png)

+ 3개의 인코더 층과 1개의 디코더 층 1개의 어텐션 층으로 모델 구성

![image](https://user-images.githubusercontent.com/74826174/189720049-506dc206-7d9b-456c-bad5-52854b25389b.png)


### 4. 문제점과 개선방안
+ 일단 기본적인 바다나우 어텐션을 적용해 보았는데 BERT를 사용하여 사전학습 된 데이터를 이용하였으면 더 좋은 결과가 나왔을 것 같다라고 생각함
+ 데이터가 너무 부족하였는데 구입을 해야 볼 수 있는 논문들도 상당하여 논문데이터가 많았다면 더 좋은 성능이 나왔을 것 같아 아쉬움이 남음
