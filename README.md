# 191122~191128 종합 프로젝트

##  영화 추천 서비스 구현

서울 3반 박준영, 최솔지

---

### 11.22 day1

### 프로젝트 진행 계획

#### 1. 추천 알고리즘

- 접속 날짜별로 해당 날짜의 1년 전, 5년 전 박스오피스 순위 보여주기
- 처음은 랜덤으로 보여주고, 유저가 평점을 매기기 시작하면서 협업 필터링으로 영화 추천

#### 2. 영화 데이터

- 영화진흥위원회 주간 박스오피스 (10년치 정도)
- 위의 영화 코드를 가지고 상세정보 조회하여 장르 데이터
- 위의 영화 이름과 개봉일을 가지고 네이버 API 에서 image url 데이터 가져오기
- SQLite 로 임시로 쓰고, 서버 돌릴 땐 postgreSQL 로 이식

#### 3. 프로젝트 구현

- Django 만 쓰는 걸 기본으로,
- 시간이 남으면 Vue 로 eventlistener 할 때만 사용
- CSS 에 시간을 좀 더 투자할 생각

### 프로젝트 진행

#### 1. 데이터

- 영진위에서 테스트로 20주 간의 박스오피스 데이터 받음

### 생각할 것 

#### 1. 데이터

- 영진위 데이터 긁을때 (영화이름, 개봉일) 튜플로 따로 넣어버리고 이거 돌리면서 네이버 api로 이미지 url 가져와서 csv 한줄 만들고 두개 csv 합쳐버리기
- 같은 방법으로 코드 따로 빼서 영화상세정보>장르 가져오기

- db 에서 랜덤 어떻게 뽑지? 찾아보기 > postgresql
- 장르는 네이버랑 영진위랑 다르니까 영진위로 id 값 생각할것
- 값이 아니고 장르 json형태 생각하기 많지 않으니까 그냥 써야할수도

#### 2. Django

- 로그인할 때 접속일 어떻게 가져올지 찾아보고 테스트해보기

- raiting 은 별도 app 인가? 모델링 구상하기

---

### 11.23 day2

### 프로젝트 진행

#### 1. 데이터

- 테스트 데이터 크롤링 추가, csv 세 개로 만들어서 영화코드, 이름을 별도로 저장
- 영화 코드로 영진위>영화 상세정보에서 장르를 저장
- 영화 이름, 연도로 네이버API>영화 이미지 url 을 저장
- 테스트 후, 원하는 만큼의 (10년분) 데이터 크롤링
  - 영화 기본 정보 (520주) 끝
  - 장르는 내일 더
  - 네이버 API 에서 image url 끝 (빈 것 많음)

#### 2. Django

- project 생성
- app 생성
  - 일단 accounts 만
    - 모델링; follower 추가
    - form; 회원가입은 일단 id/password/email/firstname/lastname
    - views
    - templates 러프
  - movies app 생성

### 생각할 것

#### 1. 데이터

#### 2. Django

- 박스오피스 기간&순위  <-> movie 관계 설정
- 마이페이지 설정 (유저 상세 페이지와 별도로)
- movies 모델링

---

### 11.24 day3

### 프로젝트 진행

#### 1. 데이터 

- 남은 데이터 받기
  - genre 끝

#### 2. Django

- movies
  - model
    - rating
    - boxoffice 는 기간, 순위를 전부 받고, movie 를 FK 로 갖는다
  - templates 구상
  - views 
    - movie_list 빼고 대충

### 생각할 것

#### 1. 데이터

- 데이터 db 에 넣기
- csv 그대로, json 파싱하지 않고
- 네이버에서 poster_url 다시 체크

#### 2. Django

- movie list
  - 추천 알고리즘
  - 유저 평점 기반으로 다른 영화 가져오기, id 어떻게?
  - 현재 날짜 찍기
    - 찍은 날짜로 박스오피스 > 영화 가져오기

---

### 11.25 day4

### 프로젝트 진행

#### 1. 데이터

- db 에 넣을 수 있게 가공하기
  - 샘플 데이터 200개로 테스트
- 네이버 html 크롤링해서 decription 추가

#### 2. Django

- accounts
  - views, model 출력 확인
- movies
  - rating 출력 확인
  - genre 는 따로 빼기로 결정

### 생각할 것

#### 1. 데이터

- 데이터를 몇개까지 넣을지

#### 2. Django

- 추천 알고리즘..언제....

#### 3. CSS

- 부트스트랩말고 다른거 쓰고 싶은데 찾아보기

#### 4. Vue

- 할까말까....

팀명이랑 페이지명 정하자!!

---

### 11.26 day5

### 프로젝트 진행

#### 1. 데이터

- db 에 다 넣었음!
  - boxoffice `movie = Movie.objects.get(codes=mv['movieCd'])` 로 movie 찾아서 넣기
  - 모두 `classmethod`를 사용해 `shell_plus` 에서 `objects.create()` 썼음
- poster url 화질구지
- 이미지 없는 것 해결할 것

#### 2. Django

- movie list 에 랜덤으로 출력 ( 새로고침 할 때마다 )
- 접속 날짜 기준 과거 박스오피스 출력

#### 3. Templates

- 왜 카드가 정렬이 안될까..

### 생각할 것

#### 1. 데이터

#### 2. Django

- 알고리즘 좀 더 깔끔하게 할 수 없을까?
- 협업 필터링 + 랜덤 구현

#### 4. Templates

- CSS 라이브러리 선택 ( tailwind, materialize, semantic, ... )
- 아무튼 꾸미기

---

### 11.27 day 6

### 프로젝트 진행

#### 1. 데이터

- 화질구지 해결 필요(시간 남으면)

#### 2. Django

- accounts form 새로 만들기 (template 적용하기 위해)

#### 3. Templates

- semantic ui 적용
- mainpage 나누기

---

### 11.28 day 7

### 프로젝트 진행

#### 1. 데이터

#### 2. Django

- 유저 평점 기반 추천 알고리즘
- 추천 모자라면 랜덤으로 채워 넣는걸로 변경
- accounts form 제대로 작동 (user.set_password)
- rating form 다시 만들기

#### 3. Templates

- sematic ui 적용하여 CSS 완성