# Simple seed script (run inside container or with env pointing to DB)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base, Issue
import os

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://civic:civic@db:5432/civicstack')
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def seed():
    Base.metadata.create_all(engine)
    s = Session()
    for i in range(1,31):
        iss = Issue(title=f'Demo issue {i}', description='Seed data', category='road', lat=17.3850, lon=78.4867)
        s.add(iss)
    s.commit()
    s.close()

if __name__ == '__main__':
    seed()
