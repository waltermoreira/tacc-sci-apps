#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

from flask import Flask, render_template, redirect, url_for, request
from flask.ext import restful

app = Flask(__name__)
api = restful.Api(app)


class Server(restful.Resource):

    def get(self):
        return {'hello': 'world'}

    def post(self):
        print('------')
        print(request.get_json())


api.add_resource(Server, '/')
