from typing import List, Optional
from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    uid : str
    full_name: str
    username : str
    email : EmailStr
    phone_number : Optional[str] = None
    user_type : Optional[str] = "free"
    user_role : Optional[str] = Field("streamer", title="Role of user", description="This will determine is a user is admin, a producer or a streamer")
    # a streamer is one who hasn't upgraded his or her account to a producer account
    
    class Config:
        orm_mode = True