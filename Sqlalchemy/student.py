import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker

# -----------------------------------------Database Connect-------------------------------------------------------------
# Bağlantı URL'si
DATABASE_URL = "mysql+pymysql://root:@localhost/student"

# Veritabanına bağlan
engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)
session = Session()

Base = sqlalchemy.orm.declarative_base()


# ---------------------------------------------Create Table-------------------------------------------------------------
class Student(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    grade = Column(String(50))


# ----------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------Student add-----------------------------------------------------------
# Base.metadata.create_all(engine)

student1 = Student(name="Furkan", age=22, grade="Elli")
student2 = Student(name="Rabia", age=26, grade="Altmış")
student3 = Student(name="Hakan", age=34, grade="Yüz")
student4 = Student(name="Ülkü", age=31, grade="Yüz")

# session.add(student1)

# session.add_all([student2, student3, student4])

# -------------------------------------------Get function---------------------------------------------------------------

# students = session.query(Student)
#
# # Get students info
# for student in students:
#     print(student.name, student.age, student.grade)
#
# print("******************************************************************************")
#
# # Get data in order
# students_order = session.query(Student).order_by(Student.name)
#
# for student in students_order:
#     print(student.name)
#
# print("******************************************************************************")
#
# # Get data by filtering
# students_filter = session.query(Student).filter(or_(Student.name=="Furkan", Student.name=="Rabia"))
#
# for student in students_filter:
#     print(student.name, student.age)
#
# print("******************************************************************************")
#
# student_count = session.query(Student).filter(or_(Student.name=="Furkan", Student.name=="Rabia")).count()
# print(student_count)

# --------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------Update Data----------------------------------------------------------
# student_update = session.query(Student).filter(Student.age == "23").first()
# student_update.name = "TengriHan"
# student_update.age =23

# session.commit()

# print(student_update.name)
# print(student_update.age)

# ----------------------------------------------------------------------------------------------------------------------
# ------------------------------------------Delete Data-----------------------------------------------------------------

student_delete = session.query(Student).filter(Student.name == "Tengrihan").first()
# session.delete(student_delete)
# session.commit()
# print(student_delete.name)
