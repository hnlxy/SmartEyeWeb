from extensions import db
from sqlalchemy import Column, Integer, String, DateTime,Float


#管理员表
class Admin(db.Model):
    __tablename__ = 'admins'
    id = Column('用户名', Integer, primary_key=True)
    password = Column('密码', Integer)
    

# 公告表
class Announcement(db.Model):
    __tablename__ = 'announcements'
    id = Column('公告ID', Integer, primary_key=True)
    title = Column('标题', String)
    content = Column('正文', String)
    publication_date = Column('发布时间', DateTime)

#护工表    
class Caregiver(db.Model):
    __tablename__ = 'caregivers'
    id = Column('护工编号', Integer, primary_key=True)
    name = Column('姓名', String)
    phone_number = Column('电话号码', Integer)
    address = Column('地址', String)
    age = Column('年龄', Integer)
    gender = Column('性别', String)
    email = Column('邮箱', String)
    department = Column('部门', String)
    experience = Column('经历', Float)
    profile_photo = Column('头像照', Float)
    qualification_photo = Column('资格照片', Float)

#监护者表
class Guardian(db.Model):
    __tablename__ = 'guardians'
    id = Column('监护人ID', Integer, primary_key=True)
    name = Column('家属姓名', String)
    phone_number = Column('手机号', Integer)
    gender = Column('性别', String)
    address = Column('地址', String)
    relation = Column('关系', String)
    notes = Column('备注', Float)

#每月信息表
class MonthlyInfo(db.Model):
    __tablename__ = 'monthly_info'
    month = Column('月份', String)
    resident_count = Column('住院人数', Integer)
    caregiver_count = Column('护工人数', Integer)
    available_beds = Column('剩余床位', Integer)
    income = Column('收入', Integer)
    expenses = Column('支出', Integer)

#用户表
class User(db.Model):
    __tablename__ = 'users'
    id = Column('用户ID', Integer, primary_key=True)
    guardian_id = Column('监护人ID', Integer)
    account_status = Column('账户状态', String)
    username = Column('用户名', String)
    password = Column('密码', Integer)
    phone_number = Column('电话号码', Integer)
    address = Column('地址', String)
    birth_date = Column('出生日期', DateTime)
    email = Column('邮箱', String)

#长者表
class Elder(db.Model):
    __tablename__ = 'elders'
    id = Column('ID', Integer, primary_key=True)
    name = Column('长者姓名', String)
    gender = Column('性别', String)
    phone_number = Column('电话号码', Integer)
    home_address = Column('家庭住址', String)
    admission_date = Column('入住日期', String)
    assigned_caregiver = Column('分配护工', String)
    care_level = Column('护理级别', String)
    room_number = Column('房间号', String)
    
#长者费用表
class ElderExpense(db.Model):
    __tablename__ = 'elder_expenses'
    elder_id = Column('长者ID', Integer, primary_key=True)
    elder_name = Column('长者姓名', String)
    deposit = Column('押金(元)', Integer)
    payment_record = Column('缴费记录(元)', Integer)
    payment_date = Column('缴费时间', String)

#长者健康表
class ElderHealth(db.Model):
    __tablename__ = 'elder_health'
    elder_id = Column('长者ID', Integer, primary_key=True)
    elder_name = Column('长者姓名', String)
    blood_pressure = Column('血压(收缩压kpa/舒张压kpa)', String)
    blood_oxygen = Column('血氧(%)', Integer)
    blood_sugar = Column('血糖(空腹mmol/L/餐后mmol/L)', String)
    heart_rate = Column('心率(次/分)', Integer)
    water_intake = Column('饮水量(mL)', Integer)

