# 이 클래스가 스프링에서 DTO 같은 역할
from pydantic import BaseModel

class UserPostIn(BaseModel):
    title: str
    body: str
    user_id: int

class UserPost(UserPostIn):
    id: int
