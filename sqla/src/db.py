
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine("postgresql+psycopg:///test_db_2025")
Session = sessionmaker(engine)
