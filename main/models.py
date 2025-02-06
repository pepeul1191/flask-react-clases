from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from main.database import ToString

Base = declarative_base()

class BodyPart(Base, ToString):
    __tablename__ = "body_parts"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(10), nullable=False)

class Member(Base, ToString):
    __tablename__ = "members"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(40), nullable=False)
    code = Column(String(5), nullable=False)
    dni = Column(String(8), nullable=False)
    email = Column(String(40), unique=True, nullable=False)
    phone = Column(String(40), nullable=False)

class Level(Base, ToString):
    __tablename__ = "levels"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)

class Objective(Base, ToString):
    __tablename__ = "objectives"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(10), nullable=False)

class Membership(Base, ToString):
    __tablename__ = "memberships"
    id = Column(Integer, primary_key=True, autoincrement=True)
    begining = Column(Date, nullable=False)
    ending = Column(Date, nullable=False)
    member_id = Column(Integer, ForeignKey("members.id"), nullable=False)

    member = relationship("Member")

class User(Base, ToString):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(20), nullable=False, unique=True)
    password = Column(String(250), nullable=False)
    member_id = Column(Integer, ForeignKey("members.id"), nullable=False)

    member = relationship("Member")

class Exercise(Base, ToString):
    __tablename__ = "exercises"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(40), nullable=False)
    image_url = Column(String(40), nullable=False)
    body_part_id = Column(Integer, ForeignKey("body_parts.id"), nullable=False)

    body_part = relationship("BodyPart")

class Routine(Base, ToString):
    __tablename__ = "routines"
    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(Date, nullable=False)
    endend = Column(Date, nullable=False)
    medical_obs = Column(Boolean, nullable=False)
    warm_ups = Column(Boolean, nullable=False)
    level_id = Column(Integer, ForeignKey("levels.id"), nullable=False)
    objective_id = Column(Integer, ForeignKey("objectives.id"), nullable=False)
    member_id = Column(Integer, ForeignKey("members.id"), nullable=False)

    level = relationship("Level")
    objective = relationship("Objective")
    member = relationship("Member")

class RoutineExercise(Base, ToString):
    __tablename__ = "routines_exercises"
    id = Column(Integer, primary_key=True, autoincrement=True)
    body_part_id = Column(Integer, ForeignKey("body_parts.id"), nullable=False)
    routine_id = Column(Integer, ForeignKey("routines.id"), nullable=False)
    exercise_id = Column(Integer, ForeignKey("exercises.id"), nullable=False)
    exercise_order = Column(Integer, nullable=False)
    steps = Column(Integer, nullable=False)
    reps = Column(Integer, nullable=False)

    routine = relationship("Routine")
    body_part = relationship("BodyPart")
    exercise = relationship("Exercise")
