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

