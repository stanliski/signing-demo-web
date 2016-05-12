# coding=utf-8
import unittest
from app.model.models import Beacon, Meeting
from datetime import datetime
from tests import test_db

class AppModelTestCase(unittest.TestCase):

    def setUp(self):
        print('do before test...')

    def tearDown(self):
        print('do after class...')

    def testInsert(self):
        meeting = Meeting()
       	meeting.content = '尊敬的客人！您现在位于“亿豪酒店15楼行政会议室”，这里即将举办“2015梅赛德斯-奔驰中国国际名车交流会”。如您应邀参与此会，可直接在此签到，签到成功可领取精美礼物一份！';
	test_db.session.add(meeting)
        test_db.session.commit()
        meeting1 = test_db.session.query(Meeting).get(1)
        beacon = Beacon()
        beacon.uuid = 'FDA50693-A4E2-4FB1-AFCF-C6EB07647825'
        beacon.major = '1'
        beacon.minor = '33012'
        beacon.meeting_id = 1
        beacon.meeting = meeting1
        test_db.session.add(beacon)
        test_db.session.commit()

