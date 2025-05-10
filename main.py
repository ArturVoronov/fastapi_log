from fastapi import FastAPI
from auth_routers import auth_router
from order_routers import order_router
import uvicorn
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from models import User
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app=FastAPI()
app.include_router(auth_router)
app.include_router(order_router)

templates = Jinja2Templates(directory='templates')

app.mount("/static", StaticFiles(directory='static'), name='static')

secret_user: str = "newphone"

secret_password: str = "whodis?"

basic: HTTPBasicCredentials = HTTPBasic()
@app.get("/who")
def get_user(creds: HTTPBasicCredentials = Depends(basic)) -> dict:
    if (creds.username == secret_user 
        and creds.password == secret_password 
        ):
        return {"username": creds.username, "password": creds.password}
    raise HTTPException(status_code=401, detail="Hey!")

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)