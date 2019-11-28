# 서버 배포

## 배포란 무엇인가?

software deployment 소프트웨어 배치(배포)

소프트웨어를 사용할 수 있도록 하는 모든 활동

- 서버컴퓨터에서 요청과 응답을 처리할 프로그램을 개발해서
- 프로그램은 배포해야 태어난다. 사용할 수 있게 배치되는 순간 부터 운영 내내
- 누가&어디에? > 다운로드해서 배치 가능해짐
  - 사용자가 > 사용자 컴퓨터에 설치 (Native App)
  - 제공자가 > 제공자 컴퓨터에 설치 **(Web App)**
    - 우리가 할건 웹 서비스!
    - **우리가, 우리 컴퓨터에 설치**
      - 직접 산 컴퓨터
      - 남의 컴퓨터... 클라우드 컴퓨팅

- 어떻게

  - AWS
    - Route53 (DNS, Routing) / EC2 (Main computer, Python&Django) / RDS (DB, MySQL.. ) / S3 (Disk, static media files .. )

  - 우리가 어디  push 해서 가져오는게 아니고, CI(Continuous Integrations, 지속적 통합) > pull
    - test code 써놓으면, 알아서 돌아가서 클라우드로 배포
    - DevOps 

- 왜??

  - 사용하기 위해서
  - real artists ship





## 배포하자

**IAAS** 

infrastructurn as a service

컴퓨터, 스토리지, 네트워킹, ... 리소스를 제공함

고객이 인프라를 구축 (조립 컴퓨터 같은..)

커스터마이즈 자유로움

app 배포 전까지 할 일이 많음

**PAAS**

platform as a service

컴퓨터, 스토리지, 네트워킹, db 풀 세트

완성된, 풀 옵션

상대적으로 쉽고 빠르다

제한된 기능만 수행할 수 있다



## Heroku

`pip install django-heroku`

`pip install gunicorn`

`python -V > runtime.txt`

​	`python-3.7.4` 안에 이렇게 바꿔서 저장

헤로쿠 가입&설치

`heroku login`

`heroku create <domainname>`

