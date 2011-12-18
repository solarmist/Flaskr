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

    def login(self, username, password):
        return self.app.post('/login', data=dict(
                username=username,
                password=password
                ), follow_redirects=True)

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    def test_login_logout(self):
        rv = self.login('solarmist', 'niko-angel')
        assert 'You were logged in' in rv.data
        rv = self.logout()
        assert 'You were logged out' in rv.data
        rv = self.login('adminx', 'niko-angel')
        assert 'Invalid username and/or password' in rv.data
        rv = self.login('solarmist', 'default')
        assert 'Invalid username and/or password' in rv.data

    def test_messages(self):
        self.login('solarmist', 'niko-angel')
        rv = self.app.post('/add', data=dict(
                title='<Hello>',
                text='<strong>HTML</strong> allowed here'
                ), follow_redirects=True)
        assert 'No entries here so far' not in rv.data
        assert '&lt;Hello&gt;' in rv.data
        assert '<strong>HTML</strong> allowed here' in rv.data

    @class_teardown
    def destroy_db(self):
        os.close(self.db_fd)
        os.unlink(flaskr.app.config['DATABASE'])

if __name__ == '__main__':
    run()
