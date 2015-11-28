from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import Column, String, Integer

# db settings
dbuser = 'root' #DB username
dbpass = 'root' #DB password
dbhost = 'localhost' #DB host
dbname = 'scrapyspiders' #DB database name
engine = create_engine("mysql://%s:%s@%s/%s?charset=utf8&use_unicode=0"
                                           %(dbuser, dbpass, dbhost, dbname),
                                           echo=False,
                                           pool_recycle=1800)
db = scoped_session(sessionmaker(autocommit=False,
                                 autoflush=False,
                                 bind=engine))

Base = declarative_base()

class AllData(Base):
    __tablename__ = 'alldata'

    id = Column(Integer, primary_key=True)
    title = Column(String(1000))
    url = Column(String(1000))
    desc = Column(String(3000))

    def __init__(self, id=None, title=None, url=None, desc=None):
        self.id = id
        self.title = title
        self.url = url
        self.desc = desc

    def __repr__(self):
        return "<AllData: id='%d', title='%s', url='%s', desc='%s'>" % (self.id, self.title, self.url, self.desc)
