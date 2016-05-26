# all the imports
import sqlite3, os
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash, send_from_directory, json
from werkzeug import secure_filename
#from contextlib import closing

BENCHMARK = '../simulator/static/benchmark/'
UPLOAD_FOLDER = '../simulator/uploads/'
DOWNLOAD_FOLDER = '../simulator/out/'
INPUT_DATA = '../simulator/inputs'
HELPER = '../simulator/helper'
RESULTS = '../simulator/results/results'
OUT = '../simulator/out/out'
ALLOWED_EXTENSIONS = set(['txt', 'csv'])

app = Flask(__name__)
app.config.from_object(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = ALLOWED_EXTENSIONS
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER
app.config['INPUT_DATA'] = INPUT_DATA
app.config['BENCHMARK'] = BENCHMARK
app.config['OUT'] = OUT
app.config['RESULTS'] = RESULTS

import simulator.views, simulator.generador, simulator.formatingData

