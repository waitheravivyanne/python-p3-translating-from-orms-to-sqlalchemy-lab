from sqlalchemy import create_engine

from lib.models import Dog 

engine = create_engine('sqlite:///dogs.db')

def create_table(Base, engine):
    Base.metadata.create_all(engine)
    return engine
    

def save(session, dog):
    session.add(dog)
    session.commit()
    return session
    

def new_from_db(session):
    return session.query(Dog).first()
    

def get_all(session):
    return session.query(Dog).all()
    

def find_by_name(session, name):
    return session.query(Dog).filter_by(name=name).first()
    

def find_by_id(session, id):
    return session.query(Dog).filter_by(id=id).first()
    

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter_by(name=name, breed=breed).first()
    

def update_breed(session, dog, breed):
    dog.breed = breed
    session.commit()
