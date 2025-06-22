from database import database, post_table
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, status, Depends
from models.post import UserPost, UserPostIn
from database import user_table
from models.user import UserIn
from security import get_password_hash
from security import create_access_token
from security import authenticate_user
from models.user import User
from security import get_current_user


app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 앱 시작 시 실행 (기존 startup 이벤트)
    await database.connect()
    yield
    # 앱 종료 시 실행 (기존 shutdown 이벤트)
    await database.disconnect()

app = FastAPI(lifespan=lifespan)

@app.post("/post", status_code=201, response_model=UserPost)
async def create_post(
    post: UserPostIn, current_user: User = Depends(get_current_user)
):
    data = {**post.model_dump(), "user_id": current_user.id}
    query = post_table.insert().values(data)
    last_record_id = await database.execute(query)
    return {**data, "id": last_record_id}

@app.post("/register")
async def register(user: UserIn):
    hashed_password = get_password_hash(user.password)
    query = user_table.insert().values(username=user.username, password=hashed_password)
    await database.execute(query)
    access_token = create_access_token(user.username)
    return {"access_token": access_token, "token_type": "bearer", "message": "가입완료!"}


from fastapi import FastAPI, HTTPException, status
from security import authenticate_user

@app.post("/login")
async def login(user: UserIn):
    user = await authenticate_user(user.username, user.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(user.username)
    return {"access_token": access_token, "token_type": "bearer", "message": "로그인 완료!"}

@app.get("/users/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user


