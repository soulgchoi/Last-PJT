

![lastpjt1](.\pjt_images\lastpjt1.JPG)



# 191122~191128 종합 프로젝트

## 영화 추천 서비스 구현

수난이대 | 서울 3반 박준영, 최솔지

---

### 1. 목표 서비스 & 실제 구현 정도

|    **일자**    | **목표**                                                     | **구현 정도**                                                |
| :------------: | ------------------------------------------------------------ | :----------------------------------------------------------- |
| **11/22 day1** | 프로젝트 설계                                                | 1. 추천 알고리즘 구상<br />2. 데이터 API 결정<br />  - 영화진흥위원회 주간 박스오피스 10년<br />  - 영화 코드로 상세정보 조회 > 장르 데이터 추출<br />  - 네이버 API 로 poster_url 및 description 추출<br />3. 프로젝트 목표 설정<br />  - Python, Django 를 사용해 구현 (JS, Vue :x: )<br />4. 데이터 크롤링 진행<br />  - 영화진흥위원회 20주 데이터 요청하여 테스트 |
| **11/23 day2** | 1. 데이터 크롤링 완료<br />2. Django 모델링                  | 1. 데이터 크롤링<br />  - 주간 박스오피스 완료<br />  - 장르 데이터 :x:<br />  - poster_url :o:<br />2. Django<br />  - form 을 제외한 accounts app 구성 완료 |
| **11/24 day3** | 1. 데이터 크롤링 및 db 입력 완료<br />2. movies app 모델링<br />3. 마이페이지 구현<br />4. 박스오피스 데이터 관계 구상 | 1. 데이터 크롤링 완료, db :x:<br />2. views 구성             |
| **11/25 day4** | 1. 데이터 db 넣기<br />2. 영화 description 추가<br />3. 추천 알고리즘 구현 | 1. django 로컬호스트 구동 확인                               |
| **11/26 day5** | 1. db 완료<br />2. poster url 화질 해결<br />3. 추천 알고리즘<br />4. CSS 시작 | 1. db 완료<br />2. movie list 추천 알고리즘<br />  - 랜덤 출력<br />  - 접속 날짜 기준 박스오피스 |
| **11/27 day6** | 1. form 에 css 적용<br />2. semantic ui 로 css 완성          | 1. accounts form 새로 만들기<br />2. css 진행중<br />  - mainpage 구성 |
| **11/28 day7** | 1. css 완료<br />2. 추천 알고리즘 완료<br />3. 서버 배포<br />4. review form | :star:완성:star:                                             |

---

### 2. 데이터베이스 모델링

명세의 모델링을 참고하여 구성하되, 

접속 날짜별 영화 추천 알고리즘을 위해 `Boxoffice` 라는 이름의 모델을 추가로 구성했다.

``````python
class Boxoffice(models.Model):
    term = models.CharField(max_length=17)
    rank = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
``````

기간과 순위로 구성되며, movie 를 `ForeignKey` 로 가진다.

이후 해당 기간의 박스오피스+순위에 해당하는 영화 정보를 불러올 것이다.

---

### 3. 핵심 기능

#### 1. 추천 알고리즘 및 영화 목록

- 접속 날짜 기준 박스오피스 정보

  ``````python
  ![lastpjt2](C:\Users\student\Last_PJT_backup\LAST_PJT\pjt_images\lastpjt2.JPG)from datetime import datetime  
  def movie_list(request):
  	boxoffices = Boxoffice.objects.all()  # boxoffice 에 저장된 objects를 모두 가져온다.
      now = datetime.now()  # datetime 모듈을 사용하여 현재 시간을 받는다.
      date = str(now.month) + str(now.day)
      year = str(now.year)
      y1_term, y5_term, y10_term = '', '', ''
      for boxoffice in boxoffices:
          term_s = int(boxoffice.term[4:8])  # 기간이 str 으로 저장되어 있기 때문에
          term_e = int(boxoffice.term[13:])  # 앞뒤로 슬라이싱하여 int 로 변환한다.
          term_y = int(boxoffice.term[:4])
          if term_s <= int(date) <= term_e:  # 현재 날짜가 속한 기간을 찾고
              if int(year) - 1 == term_y:  # 1년 전, 
                  y1_term = boxoffice.term
              elif int(year) - 5 == term_y:  # 5년 전 boxoffice 정보를 가져온다.
                  y5_term = boxoffice.term
  
      y1_movies = Boxoffice.objects.filter(term=y1_term)[:5]  # 필터링한 queryset
      y5_movies = Boxoffice.objects.filter(term=y5_term)[:5]
  ``````

  ![lastpjt2](.\pjt_images\lastpjt2.JPG)

  - 위와 같은 모습으로 출력된다.

- 평점 기반 추천 알고리즘

  ``````python
  ![lastpjt3](C:\Users\student\Last_PJT_backup\LAST_PJT\pjt_images\lastpjt3.JPG)def movie_list(request):
  	user = request.user  # 유저가
      recommend_movies = ''
      rcmmd_movies = []
      if user.like_movies.all().exists():  # 좋아하는 영화가 있으면
          user_likes = user.like_movies.all()  # 그 영화들
          for like in user_likes:
              if like.like_users.all().exists():  # 을 좋아하는 다른 유저들
                  like_users = like.like_users.all()
                  for likeuser in like_users:  # 이 좋아하는 다른 영화
                      rcmmd_movies += likeuser.like_movies.all()
      res = ''
      ids = []
      for rcmmd in rcmmd_movies:
          ids += [rcmmd.id]
      if len(ids) < 10:  # 가 열개보다 적으면
          num_entities = Movie.objects.all().count()
          rand_entities = random.sample(range(num_entities), 10-len(ids))
          # 적은 만큼 랜덤으로
          ids += rand_entities
          res = Movie.objects.filter(id__in=ids)
      else:
          rand_rcmm = random.sample(ids, 10)  # 아니면 그 중에 열개를 가져온다.
          res = Movie.objects.filter(id__in=rand_rcmm)
  ``````

  ![lastpjt3](.\pjt_images\lastpjt3.JPG)

  - 위와 같은 모습으로 출력된다.

- poster_url 정보가 없는 영화는 임의의 이미지를 넣어 출력한다.

- 각각의 card 는 클릭 시 detail 페이지로 이동한다.

#### 2. 영화 상세정보

​	![lastpjt4](.\pjt_images\lastpjt4.JPG)

- like / dislike 토글 버튼으로 `like_movies` 를 추가할 수 있다. 
  - 이를 기반으로 추천 알고리즘이 동작한다.
- scroe / comment 를 입력하여 `rating` 을 추가한다.
  - 본인이 작성한 코멘트만 삭제할 수 있다.
  - 유저 이름을 클릭하면 유저 상세정보 페이지로 이동한다.

#### 3. 유저 상세정보

​	![lastpjt5](.\pjt_images\lastpjt5.JPG)

- 다른 유저를 팔로잉 할 수 있다.
- 유저가 남긴 평점과 영화 좋아요 정보가 출력된다.

#### 4. Signup/Login

- `UserCreationForm`과 `AuthenticationForm` 을 사용하지 않고, 별도로 form 을 작성했다.

  ``````html
  <div class="field">
          <label for="form.username">Username</label>
          <input type="text" id="form.username" name="username" class="form-control" required placeholder="Username">
      </div>
      <div class="field">
          <label>Name</label>
          <div class="two fields">
          <div class="field">
              <label for="form.first_name" class="sr-only"></label>
              <input type="text" id="form.first_name" name="first_name" class="form-control" placeholder="First Name">
          </div>
          <div class="field">
              <label for="form.last_name" class="sr-only"></label>
              <input type="text" id="form.last_name" name="last_name" class="form-control"placeholder="Last Name">
          </div>
          </div>
      </div>
  ``````

  위와 같이 form 을 작성하면, 

  ``````python
  @require_http_methods(['POST', 'GET'])
  def signup(request):
      if request.user.is_authenticated:
          return redirect('accounts:user_list')
  
      if request.method == 'POST':
          form = CustomUserCreationForm(request.POST)
          if form.is_valid():
              if form.cleaned_data['password'] == form.cleaned_data['password2']:
                  user = User.objects.create(
                      username=form.cleaned_data['username'],
                      email = form.cleaned_data['email'],
                      password=form.cleaned_data['password']
                  )
                  user.last_name = form.cleaned_data['last_name']
                  user.first_name = form.cleaned_data['first_name']
                  user.set_password(user.password)
                  user.save()
                  auth_login(request, user)
                  return redirect('accounts:user_list')   
              else:
                  return render(request, 'accounts/signup.html', {
                      'form': form
                  })
      else:
          form = CustomUserCreationForm()
  
      messages = form.errors
      return render(request, 'accounts/signup.html', {
          'form': form,
          'messages': messages,
      })
  ``````

  각각의 값을 user model 에 저장한다.

  유효하지 않은 값이 들어왔을 경우, error message 를 출력한다.

  출력되는 모습은 아래와 같다.

  ![lastpjt6](.\pjt_images\lastpjt6.JPG)

  - 로그인이 되지 않았을 때는 메인페이지로 연결된다.

  ![lastpjt7](.\pjt_images\lastpjt7.JPG)

---

### 4. 배포 서버 URL

