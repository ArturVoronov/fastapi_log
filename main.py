from fastapi import FastAPI, Form, Request
from auth_routers import auth_router
from order_routers import order_router
import uvicorn
from typing import Optional
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from models import User
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from database import Session, engine
import decoders.user_decoder as decode
from schemas import SignUpModel
from fastapi.responses import HTMLResponse
from fastapi.exceptions import HTTPException
import operations.operate as db

import uvicorn

from fastapi import APIRouter, status
from operations.operate import get_all, delete_user
from fastapi.responses import FileResponse
from werkzeug.security import generate_password_hash, check_password_hash


app=FastAPI()
app.include_router(auth_router)
app.include_router(order_router)

templates = Jinja2Templates(directory='templates')

app.mount("/static", StaticFiles(directory='static'), name='static')

session = Session(bind=engine)




@app.get('/index/', response_class=HTMLResponse)
def index1(request:Request):
    films=[
        {'name':'Blade Runner', 'director':'Ridley Scott'},
        {'name':'Pulp Fiction', 'director':'Quentin Tarantino'},
        {'name':'Mulholland drive', 'director':'David Lynch'},
    ]
    context = {'request': request, 'films':films}
    return templates.TemplateResponse("index.html", context)



    

@app.get('/loginusers', response_class=HTMLResponse)
def index4(request:Request):   
    res = db.get_all() 
    print('ress',res) 
    context = {'request': request, 'res':res}
    print('this is res=',res)
    return templates.TemplateResponse("index.html", context)
@app.post('/login_to_database',response_class=HTMLResponse)
async def disable_cat(request: Request, username:str = Form(...), email:str = Form(...), password:str=Form(...), is_staff:Optional[bool]=Form(...), is_active:Optional[bool]=Form(...)):
    
    myusers={"username":username, "email":email, "password":password, "is_staff":is_staff, "is_active":is_active}
    user4=User(username=myusers['username'], email=myusers['email'], password=generate_password_hash(myusers['password']), is_staff=myusers['is_staff'], is_active=myusers['is_active'])
    print("user4=",user4.username)
    #user111={id==cats.id, username==cats.username, email==cats.email, password==cats.password, is_staff==cats.is_staff, is_active==cats.is_active}
    
    print('username1============',myusers)
    db_email=session.query(User).filter(User.email==user4.email).first()
    if db_email is not None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User with the email already exists")
    print('2')
    db_username=session.query(User).filter(User.username==user4.username).first()
    print('3')
    if db_username is not None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User with the username already exists")
    print('4')
    db.create_users(user4)
    res = db.get_all()
    context = {'request': request, 'res':res}
    return templates.TemplateResponse("index.html", context)

@app.get('/login_to_database/{id}', response_class=HTMLResponse)
def index22(request:Request, id):
    db.delete_user(id)
    res = db.get_all()
    context = {'request': request, 'res':res}
    return templates.TemplateResponse("index.html", context)



secret_user: str = session.query(User.username).all()
secret_password: str = session.query(User.password).all()


print(secret_user)
print(secret_password)
basic: HTTPBasicCredentials = HTTPBasic()
@app.get("/who")
def get_user(creds: HTTPBasicCredentials = Depends(basic)) -> dict:
    summa=0
    print(summa)
    for item in secret_user:
        s=" ".join(item)
        print(s)
        if creds.username == s:
            summa=1
            print('summa=',summa)
    for item1 in secret_password:
        s1=" ".join(item1)
        print(s1)
        if check_password_hash(s1, creds.password):
            summa=summa+1
            print('summa2',summa)
    if summa==2: 
        print(summa)
        return {"username": creds.username, "password": creds.password}
    raise HTTPException(status_code=401, detail="Hey!")

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)