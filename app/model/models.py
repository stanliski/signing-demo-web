# coding=utf-8
from app import db
from datetime import datetime
from app.tools import helper

# 签到实体类
class Signing(db.Model):
    __tablename__ = "signing"
    id = db.Column(db.Integer, primary_key=True)
    meeting_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    signing_time = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, **kwargs):
        super(Signing, self).__init__(**kwargs)

    def save(self):
        db.session.add(self)
        db.session.commit()


# 会议实体类
class Meeting(db.Model):
    __tablename__ = "meeting"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200))
    time = db.Column(db.DateTime, default=datetime.now())
    activities = db.relationship('Activity', backref="meeting", lazy='dynamic')
    beacons = db.relationship('Beacon', backref="meeting", lazy='dynamic')

    def __init__(self, **kwargs):
        super(Meeting, self).__init__(**kwargs)

    def save(self):
        db.session.add(self)
        db.session.commit()


# 签到人信息
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    contacts = db.Column(db.String(200))
    job = db.Column(db.String(200))

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

    def save(self):
        db.session.add(self)
        db.session.commit()


# 活动安排实体类
class Activity(db.Model):
    __tablename__ = "activity"
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime, default=datetime.now())
    description = db.Column(db.String(200))
    meeting_id = db.Column(db.Integer, db.ForeignKey('meeting.id'))

    def __init__(self, **kwargs):
        super(Activity, self).__init__(**kwargs)

    def save(self):
        db.session.add(self)
        db.session.commit()


# 云平台注册的Beacon实体类
class Beacon(db.Model):
    __tablename__ = "ibeacon"
    id = db.Column(db.Integer, primary_key=True)
    beacon_name = db.Column(db.String(100))
    uuid = db.Column(db.String(200))
    major = db.Column(db.Integer)
    minor = db.Column(db.Integer)
    deploy_time = db.Column(db.DateTime, default=datetime.now())
    meeting_id = db.Column(db.Integer, db.ForeignKey('meeting.id'))

    def __init__(self, **kwargs):
        super(Beacon, self).__init__(**kwargs)

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_beacon_list():
        return db.session.query(Beacon).order_by(Beacon.deploy_time.desc())
