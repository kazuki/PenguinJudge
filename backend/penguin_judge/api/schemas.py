from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

# TODO(*): 制約の定義を共通化する (https://github.com/samuelcolvin/pydantic/issues/2129)
PASSWORD_MIN_LENGTH = 6
PASSWORD_MAX_LENGTH = 256
NAME_MIN_LENGTH = 3
NAME_MAX_LENGTH = 256
LOGIN_ID_MIN_LENGTH = NAME_MIN_LENGTH
LOGIN_ID_MAX_LENGTH = NAME_MAX_LENGTH


class Login(BaseModel):
    login_id: str = Field(
        ..., min_length=LOGIN_ID_MIN_LENGTH, max_length=LOGIN_ID_MAX_LENGTH
    )
    password: str = Field(
        ..., min_length=PASSWORD_MIN_LENGTH, max_length=PASSWORD_MAX_LENGTH
    )


class UserBase(BaseModel):
    name: str = Field(..., min_length=NAME_MIN_LENGTH, max_length=NAME_MAX_LENGTH)
    admin: bool = Field(False)


class User(UserBase):
    id: int = Field(...)
    created: datetime = Field(...)
    login_id: Optional[str] = Field(
        None, min_length=LOGIN_ID_MIN_LENGTH, max_length=LOGIN_ID_MAX_LENGTH
    )


class UserUpdate(BaseModel):
    old_password: Optional[str] = Field(
        None, min_length=PASSWORD_MIN_LENGTH, max_length=PASSWORD_MAX_LENGTH
    )
    new_password: Optional[str] = Field(
        None, min_length=PASSWORD_MIN_LENGTH, max_length=PASSWORD_MAX_LENGTH
    )
    name: Optional[str] = Field(
        None, min_length=NAME_MIN_LENGTH, max_length=NAME_MAX_LENGTH
    )


class UserRegistration(UserBase, Login):
    pass
