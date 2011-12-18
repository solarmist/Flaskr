# We need the app from the project base dir
import sys
sys.path.append('..')

import os
import tempfile
import flaskr

from testify import class_setup
from testify import class_teardown
from testify import run
from testify import TestCase


class FlaskrTestCase(TestCase):
    @class_setup
    def create_new_db(self):
        self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
        flaskr.app.config['TESTING'] = True
        self.app = flaskr.app.test_client()
        flaskr.init_db()

    def test_empty_db(self):
        rv = self.app.get('/')
        assert 'No entries here so far' in rv.data

    @class_teardown
    def destroy_db(self):
        os.close(self.db_fd)
        os.unlink(flaskr.app.config['DATABASE'])

if __name__ == '__main__':
    run()
