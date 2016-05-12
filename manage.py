#! /usr/bin/env/ python

from flask.ext.script import Manager, Server
from app import create_app
from app import db

app = create_app('online')
manager = Manager(app)

@manager.command
def run():
    app.run(host='0.0.0.0', port=5000, debug=True)

@manager.command
def create_db():
    db.drop_all()
    db.create_all()


if __name__ == '__main__':
    manager.run()