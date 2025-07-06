from fastapi import FastAPI, Form, Request
from starlette.responses import JSONResponse
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from pydantic import EmailStr, BaseModel
from typing import List
import smtplib
from smtplib import SMTP
from email.message import EmailMessage
import uvicorn
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
class EmailSchema(BaseModel):
    email: List[EmailStr]


app = FastAPI()

templates = Jinja2Templates(directory='templates')

app.mount("/static", StaticFiles(directory='static'), name='static')

@app.get("/send_message1", response_class=HTMLResponse)
def index89(request:Request):    
    context = {'request': request} 
    return templates.TemplateResponse("letter.html", context)


@app.post("/email")
def send_mail(request: Request, name:str = Form(...), letter :str = Form(...)):
 
    email_address = "artur.voronov.1979@mail.ru"
    email_password = "Ce1AZb8bq5UJ5Zuuq7VT"
    msg = EmailMessage()
    msg["Subject"] = "Email subject"
    msg["From"] = email_address
    msg["To"] = "ftudw@yandex.ru"
    msg.set_content(f"""\
                    name:{name},
                    Email:{email_address},
                    Message:{letter}""")
    with smtplib.SMTP_SSL('smtp.mail.ru',465) as smtp:
        smtp.login(email_address, email_password)
        smtp.send_message(msg)
    
    return {"status":200, "errors":None}
if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)