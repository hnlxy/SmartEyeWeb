from extensions import db
from sqlalchemy import Column, Integer, String, DateTime, Float, Text, Boolean, Enum, ForeignKey, LargeBinary, Double
from datetime import time, datetime
from sqlalchemy import Column, Integer, String, DateTime, Float, Text, Boolean, Enum, ForeignKey, LargeBinary, Double, \
    BigInteger
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
    id = Column('annou_id', Integer, primary_key=True)
    title = Column('title', String(50), nullable=False)
    content = Column('content', Text, nullable=False)  #
    publication_date = Column('publication_date', DateTime, nullable=False, onupdate=datetime.now)


# 护工表
class Caregiver(db.Model):
    __tablename__ = 'caregivers'
    id = Column('caregiver_id', String(255), primary_key=True)
    name = Column('caregiver_name', String(30), nullable=False)
    phone_number = Column('caregiver_phone', String(11), nullable=False)  #
    address = Column('caregiver_address', String(255), nullable=False)
    birth = Column('caregiver_birth', DateTime, nullable=False)
    enter_date = Column('hired_date', DateTime, nullable=False)
    gender = Column('caregiver_gender', Enum('男', '女'), nullable=False)  #
    email = Column('caregiver_email', String(255), nullable=True)
    department = Column('caregiver_department', String(10), nullable=True)
    experience = Column('experienced', String(255), nullable=True)
    profile_photo = Column('photo', LargeBinary, nullable=False)
    qualification_photo = Column('qualification_photo', LargeBinary, nullable=True)

    # 获取年龄
    @hybrid_property
    def age(self):
        return (self.enter_date.year - self.birth.year) - (
                    (self.enter_date.month, self.enter_date.day) < (self.birth.month, self.birth.day))


# 监护者表
class Guardian(db.Model):
    __tablename__ = 'guardians'
    id = Column('guardian_id', String(255), primary_key=True)
    name = Column('guardian_name', String(30), nullable=False)
    phone_number = Column('guardian_phone', String(11), nullable=False)  #
    gender = Column('guardian_gender', Enum('男', '女'), nullable=False)  #
    address = Column('guardian_address', String(255), nullable=False)
    relation = Column('relation', String, nullable=True)
    notes = Column('remark', String)


# 每月信息表
class MonthlyInfo(db.Model):
    __tablename__ = 'monthly_info'
    date = Column('date', DateTime, primary_key=True)
    resident_count = Column('all_people', Integer, nullable=False)
    caregiver_count = Column('caregivers', Integer, nullable=False)
    available_beds = Column('rest_beds', Integer, nullable=False)
    income = Column('income', Integer, nullable=False)
    expenses = Column('expense', Integer, nullable=False)


# 用户表
class User(db.Model):
    __tablename__ = 'users'
    user_id = Column('user_id', String(255), primary_key=True)
    account_status = Column('user_status', Boolean, nullable=False)
    username = Column('user_name', String(20), nullable=False)
    password = Column('password', String(30), nullable=False)
    phone_number = Column('user_phone', String(11), nullable=False)
    address = Column('user_address', String(255), nullable=False)
    email = Column('user_email', String)


# 长者表
class Elder(db.Model):
    __tablename__ = 'elders'
    id = Column('elder_id', String, primary_key=True)
    name = Column('elder_name', String)
    gender = Column('elder_gender', Enum('男', '女'), nullable=False)
    phone_number = Column('elder_phone', String(11), nullable=False)
    home_address = Column('elder_address', String)
    admission_date = Column('elder_birth', DateTime)
    assigned_caregiver = Column('assign_caregiver', String)
    care_level = Column('level_care', Enum('一级', '二级', '三级'), nullable=False)
    room_number = Column('room_num', String)


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


# # 护工表
# class Caregiver(db.Model):
#     __tablename__ = 'caregivers'
#     id = Column('护工ID', String(255), primary_key=True)
#     name = Column('姓名', String(30), nullable=False)
#     phone_number = Column('联系电话', String(11), nullable=False)  #
#     address = Column('地址', String(255), nullable=False)
#     birth = Column('出生年月', datetime, nullable=False)
#     enter_date = Column('录用日期', datetime, nullable=False)
#     gender = Column('性别', Enum('男', '女'), nullable=False)  #
#     email = Column('邮箱', String(255), nullable=True)
#     department = Column('部门', String(10), nullable=True)
#     experience = Column('经历', String(255), nullable=True)
#     profile_photo = Column('头像照', LargeBinary, nullable=False)
#     qualification_photo = Column('资格照片', LargeBinary, nullable=True)
#
#     # 获取年龄
#     @hybrid_property
#     def age(self):
#         return (self.enter_date.year - self.birth.year) - (
#                     (self.enter_date.month, self.enter_date.day) < (self.birth.month, self.birth.day))
#
#
# # 监护者表
# class Guardian(db.Model):
#     __tablename__ = 'guardians'
#     id = Column('监护人ID', String(255), primary_key=True)
#     name = Column('家属姓名', String(30), nullable=False)
#     phone_number = Column('电话号码', String(11), nullable=False)  #
#     gender = Column('性别', Enum('男', '女'), nullable=False)  #
#     address = Column('地址', String(255), nullable=False)
#     relation = Column('关系', String, nullable=True)
#     notes = Column('备注', String)
#
#
# # 每月信息表
# class MonthlyInfo(db.Model):
#     __tablename__ = 'monthly_info'
#     month = Column('日期', datetime, primary_key=True)
#     resident_count = Column('住院人数', Integer, nullable=False)
#     caregiver_count = Column('护工人数', Integer, nullable=False)
#     available_beds = Column('剩余床位', Integer, nullable=False)
#     income = Column('收入', Integer, nullable=False)
#     expenses = Column('支出', Integer, nullable=False)
#
#
# # 用户表
# class User(db.Model):
#     __tablename__ = 'users'
#     id = Column('用户ID', String(255), primary_key=True)
#     guardian_id = Column('监护人ID', String(255), foreign_key=(Guardian.id))
#     account_status = Column('账户状态', Boolean, nullable=False)
#     username = Column('用户名', String(20), nullable=False)
#     password = Column('密码', String(30), nullable=False)
#     phone_number = Column('电话号码', String(11), nullable=False)
#     address = Column('地址', String(255), nullable=False)
#     birth_date = Column('出生日期', DateTime)
#     email = Column('邮箱', String)
#
#
# # 长者表
# class Elder(db.Model):
#     __tablename__ = 'elders'
#     id = Column('长者ID', String, primary_key=True)
#     name = Column('长者姓名', String)
#     gender = Column('性别', Enum('男', '女'), nullable=False)
#     phone_number = Column('电话号码', String(11), nullable=False)
#     home_address = Column('家庭住址', String)
#     admission_date = Column('入住日期', datetime)
#     assigned_caregiver = Column('分配护工', String)
#     care_level = Column('护理级别', Enum('一级', '二级', '三级'), nullable=False)
#     room_number = Column('房间号', String)
#
#
# # 长者费用表
# class ElderExpense(db.Model):
#     __tablename__ = 'elder_expenses'
#     elder_id = Column('长者ID', String, foreign_key=(Elder.id))
#     deposit = Column('押金(元)', Integer)
#     payment_record = Column('缴费记录(元)', Integer)
#     payment_date = Column('缴费时间', datetime)
#
#
# # 长者健康表
# class ElderHealth(db.Model):
#     __tablename__ = 'elder_health'
#     elder_id = Column('长者ID', Integer, foreign_key=(Elder.id))
#     blood_pressure = Column('血压(收缩压kpa/舒张压kpa)', String)
#     blood_oxygen = Column('血氧(%)', Double)
#     blood_sugar = Column('血糖(空腹mmol/L/餐后mmol/L)', Double)
#     heart_rate = Column('心率(次/分)', Integer)
#     water_intake = Column('饮水量(mL)', Double)
#
#
# # 长者与监护人关系表
# class ElderGuardian(db.Model):
#     __tablename__ = 'elder_guardian'
#     elder_id = Column('长者ID', String, foreign_key=(Elder.id))
#     guardian_id = Column('监护人ID', String, foreign_key=(Guardian.id))
