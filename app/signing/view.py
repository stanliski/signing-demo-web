# coding=utf8
__author__ = 'stanley'
from flask import jsonify, request
from . import main
from app.model.models import Signing, User, Beacon, Meeting
import json
import types


@main.route('/signing', methods=['POST'])
def signing():
    meeting_id = request.form['meetingId']
    name = request.form['name']
    contacts = request.form['contact']
    job = request.form['job']

    user = User()
    user.name = name
    user.contacts = contacts
    user.job = job
    user.save()

    newUser = User.query.filter_by(name=name).first()

    signing = Signing()
    signing.meeting_id = meeting_id
    signing.user_id = newUser.id
    signing.save()

    return jsonify(dict(status=200, info='签到成功'))


@main.route('/check_beacon', methods=['POST'])
def check_beacon():
    request_list = request.form['data']
    decoded = json.loads(request_list)

    if len(decoded) == 0:
        return jsonify(dict(status='402', info='bad request'))

    beacon_list = []

    for obj in decoded:
        beacon = Beacon()
        beacon.beacon_name = obj['beacon_name']
        beacon.uuid = obj['uuid']
        beacon.major = obj['major']
        beacon.minor = obj['minor']
        beacon_list.append(beacon)

    meetings = Meeting.query.order_by(Meeting.time.desc())

    all_beacons = []

    for meeting in meetings:
        meeting_beacon_list = meeting.beacons
        for item in meeting_beacon_list:
            all_beacons.append(item)

    for beacon in all_beacons:
        for request_beacon in beacon_list:
            if beacon.minor == long(request_beacon.minor):
                print 'is true'
                meeting = Meeting.query.get_or_404(beacon.meeting_id)
#                print meeting.content
                return jsonify(dict(status=200, info='成功获取会议信息', data=meeting.content))
            print '-------------------------'

    return jsonify(dict(status=404, info='没有授权的Beacon'))


def strSame(str1,str2):
    if len(str1) != len(str2):
        return False
    i = 0
    while i < len(str1):
        if str1[i] is not str2[i]:
            return False
        else:
            i += 1
    return True
