#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request, render_template
from app import app

if __name__ == '__main__':
    app.run(debug = True)
