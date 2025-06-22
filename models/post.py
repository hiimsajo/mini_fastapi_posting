# 이 클래스가 스프링에서 DTO 같은 역할
from pydantic import BaseModel

class UserPostIn(BaseModel):
    name: str
    body: str

class UserPost(UserPostIn):
    id: int
