from fastapi import FastAPI, Form, Request
from auth_routers import auth_router
from order_routers import order_router
import uvicorn
from typing import Optional
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from models import User, Product
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from database import Session, engine
import decoders.user_decoder as decode
from schemas import SignUpModel
from fastapi.responses import HTMLResponse
from fastapi.exceptions import HTTPException
import operations.operate as db
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

@app.get('/', response_class=HTMLResponse)
def index55(request:Request):
    res1 = db.get_products_all()
    print('res1',res1)
    context = {'request': request, 'res1':res1}
    return templates.TemplateResponse("index4.html", context)

@app.get('/products1', response_class=HTMLResponse)
def index5(request:Request):
    res = db.get_products_all()
    context = {'request': request, 'res':res}
    return templates.TemplateResponse("index3.html", context)

@app.post('/products',response_class=HTMLResponse)
async def disable_cat2(request: Request, name:str = Form(...), category:str = Form(...), description:str=Form(...), price:Optional[float]=Form(...)):
    print('1')
    myproducts={"name":name, "category":category, "description":description, "price":price}
    product4=Product(name=myproducts['name'], category=myproducts['category'], description=myproducts['description'], price=myproducts['price'])
    print('2')
    
    db.create_products(product4)
    res = db.get_products_all()
    context = {'request': request, 'res':res}
    return templates.TemplateResponse("index3.html", context)

@app.get('/products/{id}', response_class=HTMLResponse)
def index5(request:Request, id):
    db.delete_product(id)
    res1 = db.get_products_all()
    context = {'request': request, 'res1':res1}
    return templates.TemplateResponse("index4.html", context)

    

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


basic: HTTPBasicCredentials = HTTPBasic()
@app.get("/who")
def get_user(creds: HTTPBasicCredentials = Depends(basic)) -> dict:
    # -*- coding: utf-8 -*-
    secret_user: str = session.query(User.username).all()
    secret_password: str = session.query(User.password).all()
    summa=0
    print(summa)
    print(secret_user)
    for item in secret_user:
        s=" ".join(item)
        print('secretuser=',s)
        if creds.username == s:
            summa=1
            print('summa=',summa)
    for item1 in secret_password:
        s1=" ".join(item1)
        print('secretpass=',s1)
        if check_password_hash(s1, creds.password):
            summa=summa+1
            print('summa2',summa)
    if summa==2: 
        print(summa)
        return {"username": creds.username, "password": creds.password}
    raise HTTPException(status_code=401, detail="Hey!")

@app.get('/database1', response_class=HTMLResponse)
def index5(request:Request):   
    res = db.get_all() 
    print('ress',res) 
    context = {'request': request, 'res':res}
    print('this is res=',res)
    return templates.TemplateResponse("index1.html", context)

@app.get('/loginpass', response_class=HTMLResponse)
def index44(request:Request):   
    
    context = {'request': request}
    
    return templates.TemplateResponse("who.html", context)

@app.post('/loginvhod',response_class=HTMLResponse)
async def logvh(request: Request, username:str = Form(...), password:str=Form(...)): 
    myusers11={"username":username, "password":password}
    username1=myusers11['username']
    password1=(myusers11['password'])
    secret_user: str = session.query(User.username).all()
    secret_password: str = session.query(User.password).all()
    print('secret_user',secret_user)
    print('password1=',password1)
    summa=0
    print(summa)
    print(secret_user)
    d_secret_user_to_list=[]
    d1_secret_password_to_list=[]
    for item in secret_user:
        
        s=" ".join(item)
        d_secret_user_to_list.append(s)
        print('d_secret_user_to_list=',d_secret_user_to_list)
        if  username1 == s:
            n=d_secret_user_to_list.index(s)         
            summa=1
            print('summa=',summa)
    for item1 in secret_password:
        s1=" ".join(item1)
        d1_secret_password_to_list.append(s1)
        print('s1=',s1)       
        if check_password_hash(s1, password1):
            n1=d1_secret_password_to_list.index(s1)
            summa=2    
    if summa==2 and n==n1 : 
        print(summa)
        context = {'request': request, 'username1':username1, 'password1':password1 }
 
        return templates.TemplateResponse("who1.html", context)
    raise HTTPException(status_code=401, detail="Hey!")
    

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)