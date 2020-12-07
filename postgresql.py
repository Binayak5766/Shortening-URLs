from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker

urls = declarative_base()

class Links(urls):
	__tablename__ = 'Links'
	id=Column(Integer, primary_key=True)
	Link=Column(String, unique=True)
	ShortLink=Column(String, unique=True)

	def __init__(self, link, short):
		self.Link = link
		self.ShortLink = short

	def __repr__(self):
		return "<Link(URL='{}', Short='{}')>".format(self.Link, self.ShortLink)

DATABASE_URI = 'postgres+psycopg2://postgres:Binayak@5766@localhost:5432/URLs'

engine = create_engine(DATABASE_URI)
urls.metadata.create_all(engine)

def add_to_table(string, second_string):
	Session = sessionmaker(bind=engine)
	s = Session()
	new_link = Links(link=string, short=second_string)
	s.add(new_link)
	s.commit()
	s.close()

def search_through_shortlink(shortlink):
	Session = sessionmaker(bind=engine)
	s = Session()
	search = s.query(Links).filter(Links.ShortLink==shortlink).first()
	return search.Link
	s.close()

