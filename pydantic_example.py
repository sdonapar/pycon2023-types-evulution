from datetime import datetime
from pydantic import BaseModel, PositiveInt, ValidationError
import json


class User(BaseModel):
    id: int  
    name: str = 'John Doe'  
    signup_ts: datetime | None  
    tastes: dict[str, PositiveInt]  


user_data_1 = {
    'id': 123,
    'signup_ts': '2019-06-01 12:22',  
    'tastes': {
        'wine': 9,
        b'cheese': 7,  
        'cabbage': '1',  
    },
}

user1 = User(**user_data_1)  

#print(user1.id)  
#> 123
print(json.dumps(user1.model_dump(),indent=4,default=str))  

user_data_2 = {
    'id': "123 is not",
    'signup_ts': '2019-06-01 12:22',  
    'tastes': {
        'wine': 9,
        b'cheese': 7,  
        'cabbage': '1',  
    },
}
try:
    user2 = User(**user_data_2)
except ValidationError as e:
    print(json.dumps(e.errors(),indent=4))
