# mini_fastapi_project_tutorial
파이썬 fastapi 기반 게시판 만들기

FastAPI 기반의 인증 기능이 있는 게시판 미니 프로젝트 입니다.
• 사용된 기술 :  Python 3.11, FastAPI, SQLite, SQLAlchemy, Pydantic, Uvicorn, Postman, Git, pyenv, venv

주요 기능 및 성과:
•    RESTful API 서버 개발
•    FastAPI와 Pydantic을 활용해 게시글 등록(POST), 전체 조회(GET), 
     회원가입(POST), 로그인(POST) 기능 구현
•    회원가입 시 사용자 정보 저장, 로그인 시 비밀번호 검증 및 JWT 토큰 
     발급
•    JWT 토큰을 활용한 인증 로직 구현 및 인증 실패 시 사용자 맞춤 에러 
     메시지 반환
•    SQLAlchemy ORM과 SQLite를 연동하여 게시글, 사용자 정보 영구 저장
•    lifespan 이벤트 핸들러로 DB 연결/해제 자동화
•    Postman 및 Swagger UI를 통한 API 테스트 
•    pyenv, venv를 이용한 파이썬 가상환경 및 버전 관리
•    GitHub를 통한 형상 관리 

Swagger UI로 확인
![스웨거_파이썬](https://github.com/user-attachments/assets/461d3d6a-caa1-4250-8aaf-93bcdfa239c7)

