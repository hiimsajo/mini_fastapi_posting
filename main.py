import databases
import sqlalchemy 
from contextlib import asynccontextmanager
from fastapi import FastAPI
from models.post import UserPost, UserPostIn

DATABASE_URL = "sqlite:///data.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
post_table = sqlalchemy.Table(
    "posta",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("body", sqlalchemy.String),
)

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)

app = FastAPI()

'''
@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

    이건 사장된 거여서 lifespan으로 바꿈
'''

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 앱 시작 시 실행 (기존 startup 이벤트)
    await database.connect()
    yield
    # 앱 종료 시 실행 (기존 shutdown 이벤트)
    await database.disconnect()

app = FastAPI(lifespan=lifespan)

@app.post("/post", status_code=201, response_model=UserPost)
async def create_post(post: UserPostIn):
    query = post_table.insert().values(name=post.name, body=post.body)
    last_record_id = await database.execute(query)
    return {**post.model_dump(), "id": last_record_id}

@app.get("/posts", response_model=list[UserPost])
async def get_all_posts():
    query = post_table.select()
    return await database.fetch_all(query)