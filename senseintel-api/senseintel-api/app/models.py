"""
Definition of models.
"""

from django.db import models
from django.contrib.postgres.fields import JSONField
from flask import Flask, jsonify, make_response
from collections import defaultdict


import time
import os
from gpsd import *
from time import *
import threading



class SensorModule(models.Model):

    moduleName = models.CharField(max_length = 250)
    ipAddress = models.GenericIPAddressField()
    sensorData = JSONField(db_index=True)
    sensorReadingAvg = JSONField()
    gpsData = JSONField()

    sensorList = defaultdict(list)