from peewee import *
from datetime import date
# SQLite database
db = SqliteDatabase('classes.db')
# Base model
class BaseModel(Model):
    class Meta:
        database = db
# Users: Admins and Teachers
class User(BaseModel):
    id_user = AutoField()
    name = CharField()
    is_admin = BooleanField() # True if admin, False if teacher
    login = BooleanField(unique=False)
    password = CharField() # Store hashed passwords in production
# Students
class Student(BaseModel):
    id_student = AutoField()
    name = CharField()
    email = CharField(unique=True)
    phone = CharField(null=True)
    birthdate = DateField()
# Classes (one teacher per class)
class Class(BaseModel):
    id_class = AutoField()
    class_name = CharField()
    id_user = ForeignKeyField(User, backref='classes')
    date = DateField()
    time = TimeField()
# Attendance
class Attendance(BaseModel):
    id = AutoField()
    id_class = ForeignKeyField(Class, backref='attendances')
    id_student = ForeignKeyField(Student, backref='attendances')
    attend = BooleanField() # True if present, False if absent
    class Meta:
        indexes = (
            (('id_class', 'id_student'), True), # Unique constraint
        )
# Create tables
def initialize_db():
    with db:
        db.create_tables([User, Student, Class, Attendance])