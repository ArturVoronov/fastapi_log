import sys
sys.path.append('./')
from database import Session
from models import User
import decoders.user_decoder as decode
from auth_routers import session
from schemas import SignUpModel
from decoders.user_decoder import *

def create_users(user4:SignUpModel):
    try:
        req = user4
        
        session.add(req)
        session.commit()
        return {
            'status': 'ok',
            'message':'new user added'
        }
    except Exception as e:
        return {
            'status':'error',
            'message':str(e)
        }
    # get all to-do list

    
def get_one(id:int):
    try:
        criteria = {'id':id}
        res = session.query(User).filter_by(**criteria).one_or_none()
        if res is not None:
            record = decode.decode_user(res)
            return {'status':'ok',
                    'data':record
                    }
        else:
            return {
                'status':'ok',
                'message':f'Record with id {id} do not Exist'
            }
    except Exception as e:
        return {
            'status':'error',
            'message':str(e)
        }


# update a todo
def update_todo(users:SignUpModel):
    try:
        criteria = {'id': id}
        res = session.query(users).filter_by(**criteria).one_or_none()
        if res is not None:
            res.users = users
            session.commit()
            return {'status':'ok',
                    'message':"Record update successfully"
                    }
        else:
            return {
                'status':'ok',
                'message':f'Record with id {id} do not Exist'
            }
    except Exception as e:
        return {
            'status':'error',
            'message':str(e)
        }

# delete a todo

def delete_user(id:int):
    try:
        criteria = {'id': id}
        res = session.query(User).filter_by(**criteria).one_or_none()
        if res is not None:
            session.delete(res)
            session.commit()
            return {'status':'ok',
                    'message':"Record deleted successfully"
                    }
        else:
            return {
                'status':'ok',
                'message':f'Record with id {id} do not Exist'
            }
    except Exception as e:
        return {
            'status':'error',
            'message':str(e)
        }
def get_all():
        try:
            res = session.query(User).all()
            docs = decode_todos(res)
            return {'status':'ok',
                'data':docs
                }
        except Exception as e:
            return {
            'status':'error',
            'message':str(e)
        }
