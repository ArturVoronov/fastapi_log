from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base



engine=create_engine('postgresql://postgres:c420av98@localhost:5432/pizzadb', echo=True)

Base=declarative_base()

Session=sessionmaker()
