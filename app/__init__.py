# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
#from flask_moment import Moment
from config import config
from flask_login import LoginManager

bootstrap = Bootstrap()
#mail = Mail()
#moment = Moment()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'



def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    #moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    #路由和其他处理程序定义
    #...
    return app

