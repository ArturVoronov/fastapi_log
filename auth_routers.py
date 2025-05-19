from fastapi import APIRouter, status
from database import Session, engine
from models import User
from schemas import SignUpModel
from fastapi.exceptions import HTTPException
from werkzeug.security import generate_password_hash, check_password_hash
from schemas import SignUpModel

auth_router=APIRouter( prefix='/auth', tags=['auth'])

session = Session(bind=engine)

@auth_router.get('/')
async def hello():
    return {"message":"hello Artyr"}

@auth_router.post('/signup')
async def signup(users:SignUpModel):
    print('1')
    db_email=session.query(User).filter(User.email==users.email).first()
    if db_email is not None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User with the email already exists")
    print('2')
    db_username=session.query(User).filter(User.username==users.username).first()
    print('3')
    if db_username is not None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User with the username already exists")
    print('4')
    new_user=User(
        username=users.username,
        email=users.email,
        password=generate_password_hash(users.password),
        is_active=users.is_active,
        is_staff=users.is_staff
    )
    print(new_user)
    session.add(new_user)
    session.commit()
    return new_user
def create_users():
    
    user3=User(username= "artyr6635",email="5art4453@mail.ru", password=generate_password_hash('12354'), is_staff=False, is_active=True)
    print("user3",user3)
    session.add(user3)
    session.commit()
    return user3
#create_users()