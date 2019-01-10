# coding=utf-8
# --author='fangfang'

from flask import render_template
from . import api


@api.route('/')
def index():
    comments = ['world']
    return render_template('login.html', comments=comments)
