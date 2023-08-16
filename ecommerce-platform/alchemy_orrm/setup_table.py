# setup_tables.py
from setup_orm import engine, get_session
from models import Base


def create_tables():
    with get_session() as session:
        Base.metadata.create_all(bind=engine)
        print("Tables created successfully")


if __name__ == "__main__":
    create_tables()
