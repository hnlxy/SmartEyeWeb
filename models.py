from extensions import db
from sqlalchemy import Column, Integer, String, DateTime, Float, Text, Boolean, Enum, ForeignKey, LargeBinary, Double, \
    SmallInteger, BigInteger
from datetime import time, datetime
from datetime import datetime
from sqlalchemy.ext.hybrid import hybrid_property


# 管理员表
class Admin(db.Model):
    __tablename__ = 'admins'
    username = Column('username', String, nullable=False, primary_key=True)
    password = Column('password', String, nullable=False)
    email = Column('email', String, nullable=False)  # 注册时用来接收验证码
    address = Column('address', String, nullable=True)
    gmt_create = Column('gmt_create', DateTime, nullable=False, default=datetime.now())  # 创建时间
    gmt_update = Column('gmt_update', DateTime, nullable=False, default=datetime.now())  # 更新时间


# 公告表
class Announcement(db.Model):
    __tablename__ = 'announcements'
    announcement_id = Column('announcement_id', Integer, primary_key=True)
    title = Column('title', String(50), nullable=False)
    content = Column('content', Text, nullable=False)  #
    publication_date = Column('publication_date', DateTime, nullable=False, onupdate=datetime.now)


# 护工表
class Caregiver(db.Model):
    __tablename__ = 'caregivers'
    caregiver_id = Column('caregiver_id', String(255), primary_key=True)
    caregiver_name = Column('caregiver_name', String(30), nullable=False)
    caregiver_age = Column('caregiver_age', SmallInteger, nullable=False)
    caregiver_phone = Column('caregiver_phone', String(15), nullable=False)  #
    caregiver_address = Column('caregiver_address', String(255), nullable=False)
    hired_date = Column('hired_date', DateTime, nullable=False)
    caregiver_gender = Column('caregiver_gender', Enum('男', '女'), nullable=False)  #
    caregiver_email = Column('caregiver_email', String(255), nullable=True)
    caregiver_department = Column('caregiver_department', String(20), nullable=True)
    experience = Column('experience', String(255), nullable=True)
    profile_photo = Column('profile_photo', String(255), nullable=False)
    qualification_photo = Column('qualification_photo', String(255), nullable=True)

    # 获取年龄
    @hybrid_property
    def age(self):
        return (self.enter_date.year - self.birth.year) - (
                (self.enter_date.month, self.enter_date.day) < (self.birth.month, self.birth.day))


# 监护者表
class Guardian(db.Model):
    __tablename__ = 'guardians'
    guardian_id = Column('guardian_id', String(255), primary_key=True)
    guardian_name = Column('guardian_name', String(30), nullable=False)
    guardian_phone = Column('guardian_phone', String(11), nullable=False)  #
    guardian_gender = Column('guardian_gender', Enum('男', '女'), nullable=False)  #
    guardian_address = Column('guardian_address', String(255), nullable=False)
    relation = Column('relation', String, nullable=True)
    remark = Column('remark', String)


# 每月信息表
class MonthlyInfo(db.Model):
    __tablename__ = 'monthly_info'
    date = Column('date', DateTime, primary_key=True)
    all_people = Column('all_people', Integer, nullable=False)
    caregivers = Column('caregivers', Integer, nullable=False)
    available_beds = Column('available_beds', Integer, nullable=False)
    income = Column('income', Integer, nullable=False)
    expenses = Column('expenses', Integer, nullable=False)


# 用户表
class User(db.Model):
    __tablename__ = 'users'
    user_id = Column('user_id', String(255), primary_key=True)
    user_status = Column('user_status', Boolean, nullable=False)
    username = Column('username', String(20), nullable=False)
    password = Column('password', String(30), nullable=False)
    user_telephone = Column('user_telephone', String(11), nullable=False)
    user_address = Column('user_address', String(255), nullable=False)
    user_email = Column('user_email', String)


# 长者表
class Elder(db.Model):
    __tablename__ = 'elders'
    elder_id = Column('elder_id', String, primary_key=True)
    elder_name = Column('elder_name', String)
    elder_gender = Column('elder_gender', Enum('男', '女'), nullable=False)
    elder_phone = Column('elder_phone', String(11), nullable=False)
    elder_address = Column('elder_address', String)
    elder_birth = Column('elder_birth', DateTime)
    assigned_caregiver = Column('assign_caregiver', String)
    care_level = Column('level_care', Enum('一级', '二级', '三级'), nullable=False)
    room_number = Column('room_number', String)


# 长者费用表
class ElderExpense(db.Model):
    __tablename__ = 'elder_expenses'
    id = Column('id', BigInteger, autoincrement=True, primary_key=True)
    elder_id = Column('elder_id', String)
    elder_name = Column('elder_name', String)
    payment = Column('payment', Integer)
    pay_date = Column('pay_date', DateTime)


# 长者健康表
class ElderHealth(db.Model):
    __tablename__ = 'elder_health'
    elder_id = Column('elder_id', Integer, primary_key=True)
    blood_pressure = Column('blood_pressure', String)
    blood_oxygen = Column('blood_oxygen', Double)
    blood_sugar = Column('blood_glucose', Double)
    heart_rate = Column('heart_rate', Integer)
    water_intake = Column('water_intake', Double)


# 长者与监护人关系表
class ElderGuardian(db.Model):
    __tablename__ = 'elder_guardian'
    elder_id = Column('elder_id', String, primary_key=True)
    guardian_id = Column('guardian_id', String, primary_key=True)


class CaregiverTasks(db.Model):
    __tablename__ = 'caregiver_tasks'
    id = Column('id', Integer, autoincrement=True, primary_key=True)
    caregiver_id = Column('caregiver_id', String)
    caregiver_name = Column('caregiver_name', String)
    task = Column('task', String)
    task_date = Column('task_date', DateTime)
    task_status = Column('task_status', ENUM('未完成', '已完成'))
