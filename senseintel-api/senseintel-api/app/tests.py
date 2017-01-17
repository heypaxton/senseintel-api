"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".
"""

import django
from django.test import TestCase
from app.models import *

# TODO: Configure your database in settings.py and sync before running tests.
class SaveTest(TestCase):
    def test_save(self):
        reading = SensorModule(  moduleName='test',sensorData=[{
    
         "accel": {
           "pitch": 0.05162583142908932,
           "roll": 358.9180023060999,
           "yaw": 88.41593137179046
         },
         "accelRaw": {
           "x": -0.0017278495943173766,
           "y": -0.018815619871020317,
           "z": 0.9628462195396423
         },
         "compass": 88.41024182421185,
         "compassRaw": {
           "x": 0.38670799136161804,
           "y": -14.604934692382812,
           "z": 5.905102252960205
         },
         "gyro": {
           "pitch": 0.08530018482155957,
           "roll": 358.92965845080533,
           "yaw": 88.41337005085171
         },
         "gyroRaw": {
           "x": -0.012549860402941704,
           "y": -0.03786290064454079,
           "z": 0.0020742900669574738
         },
         "humidity": 37.94554901123047,
         "orient": {
           "pitch": 0.1468588055109267,
           "roll": 358.95223457388977,
           "yaw": 88.40925827697137
         },
         "orientRaw": {
           "pitch": 0.00207962142303586,
           "roll": -0.018486613407731056,
           "yaw": 1.5430498123168945
         },
         "pressure": 1026.365234375,
         "temp": 16.053691864013672,
         "tempHumidity": 16.053691864013672,
         "tempPressure": 15.012500762939453
         }
         ]
        )
        reading.save()
        self.assertTrue(
            SensorModule.objects.filter(pk = reading.pk).exists()
        )


class ViewTest(TestCase):
    """Tests for the application views."""

    if django.VERSION[:2] >= (1, 7):
        # Django 1.7 requires an explicit setup() when running tests in PTVS
        @classmethod
        def setUpClass(cls):
            super(ViewTest, cls).setUpClass()
            django.setup()

    def test_home(self):
        """Tests the home page."""
        response = self.client.get('/')
        self.assertContains(response, 'Home Page', 1, 200)

    def test_contact(self):
        """Tests the contact page."""
        response = self.client.get('/contact')
        self.assertContains(response, 'Contact', 3, 200)

    def test_about(self):
        """Tests the about page."""
        response = self.client.get('/about')
        self.assertContains(response, 'About', 3, 200)
