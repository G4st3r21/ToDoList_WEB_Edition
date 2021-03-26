import datetime
from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.orm import relation
from .db_session import SqlAlchemyBase
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(SqlAlchemyBase, UserMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String, nullable=True)

    email = Column(String, index=True, unique=True, nullable=True)

    hashed_password = Column(String, nullable=True)

    created_date = Column(DateTime, default=datetime.datetime.now)

    tasks = relation("Tasks", back_populates='user')

    def __repr__(self):
        return f'<User> {self.id} {self.name} {self.email}'

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)
