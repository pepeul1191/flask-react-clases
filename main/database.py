from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class ToString:
  def __repr__(self):
    return f"<{self.__class__.__name__}({', '.join(f'{key}={value}' for key, value in self.__dict__.items() if not key.startswith('_'))})>"


engine = create_engine("sqlite:///db/app.db", echo=True)
Session = sessionmaker(bind=engine)
