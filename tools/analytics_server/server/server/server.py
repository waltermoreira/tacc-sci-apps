#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

from flask import Flask, render_template, redirect, url_for, request
from flask.ext import restful

import pymongo

app = Flask(__name__)
api = restful.Api(app)


class Server(restful.Resource):

    def __init__(self, *args, **kwargs):
        super(Server, self).__init__(*args, **kwargs)
        self.mongo = pymongo.MongoClient('localhost', 27017)
        self.analytics = self.mongo.analytics # the database
        self.collection = self.analytics.collection # the collection

    def get(self):
        return {'hello': 'world'}

    def post(self):
        js = request.get_json()
        self.collection.insert(js)


api.add_resource(Server, '/')
