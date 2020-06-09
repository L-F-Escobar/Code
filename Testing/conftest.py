import os
import pytest
import time
import collections
from flask import Flask
from datetime import datetime
from unittest import  mock, TestCase
# from flask_testing import TestCase
from datetime import datetime
os.environ["ENV"] = "TESTING"
from tests.imports import *


@pytest.fixture(scope='session', autouse=False)
def date_time_stamper():
    """ Report the time at the end of a session. """
    start = time.time()
    yield
    stop = time.time()
    delta = stop - start
    now = time.time()

    print('\n--')
    print('- Total test duration: {:0.3} seconds'.format(delta))
    print('- Finished: {}'.format(time.strftime('%d %b %X', time.localtime(now))))
    print('-----------------')

@pytest.fixture()
def run_time_stamper(capsys):
    """ Report test durations after each function. """
    start = time.time()
    yield
    stop = time.time()
    delta = stop- start

    with capsys.disabled():
        print('\n- Test duration: {:0.3} seconds'.format(delta))

def test_pytestconfig(pytestconfig):
    print('args:', pytestconfig.args)
    print('inifile:', pytestconfig.inifile)
    print('invocation_dir:', pytestconfig.invocation_dir)
    print('rootdir:', pytestconfig.rootdir)
    print('-k EXPRESSION:', pytestconfig.getoption('keyword'))
    print('-v,--verbose:', pytestconfig.getoption('verbose'))
    print('-q,--quiet:', pytestconfig.getoption('quiet'))
    print('-l,--showlocals:', pytestconfig.getoption('showlocals'))
    print('--tb=style:', pytestconfig.getoption('tbstyle'))

Duration = collections.namedtuple('Duration', ['current','last'])
@pytest.fixture(scope='session')
def duration_cache(request):
    ''' Session scope, reads previous entry or an empty dict if there is no previous cache data. '''
    key = 'duration/testdurations'
    d = Duration({}, request.config.cache.get(key, {}))
    yield d
    request.config.cache.set(key, d.current)

@pytest.fixture(autouse=True)
def check_duration(request, duration_cache):
    _duration = duration_cache
    nodeid = request.node.nodeid
    start_time = datetime.now()
    yield
    duration = (datetime.now() - start_time).total_seconds()
    _duration.current[nodeid] = duration
    if _duration.last.get(nodeid, None) is not None:
        errorstring = "test duration over 10x last duration"
        assert duration <= (_duration.last[nodeid] * 10), errorstring

# https://docs.pytest.org/en/latest/reference.html#_pytest.hookspec.pytest_report_header
def pytest_report_header(config, startdir):
    '''
        Return a string or list of strings to be displayed as header info for terminal reporting.

        Parameters:
        - config (_pytest.config.Config): Pytest config object, (config.args).
        - startdir (py._path.local.LocalPath): Object with the starting dir.

        Returns:
        - outputList (list) : List to display as header information into the terminal.
    '''
    outputList = []

    outputList.append("Automated Testing Framework")
    outputList.append("Luis Fernando Escobar-Driver")

    if config.getoption("verbose") > 0:
        outputList.append("Verbose: Enabled")

    return outputList

# # https://docs.pytest.org/en/latest/reference.html#_pytest.hookspec.pytest_runtest_makereport
# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     '''
#         Postprocess test reports, called when the test “report” object is about to be created.
#         Makes a report of all failures and outputs the text file into reports/failures.txt.

#         Parameters:
#         - item (_pytest.python.Function): The test which is being examined.
#                                           Ex: <Function test_full_filter_suite_ensure_passing_all>.
#         - call (_pytest.runner.CallInfo): The state of the call, ie, setup, call, teardown.
#                                           Ex: <CallInfo when='setup' result: []>
#         Returns:
#         - A _pytest.runner.TestReport object for the given pytest.Item and _pytest.runner.CallInfo.
#     '''
#     # Execute all other hooks to obtain the report object
#     outcome = yield
#     report = outcome.get_result()

#     # We only look at actual failing test calls, not setup
#     if (report.when == "call" or report.when == "teardown") and report.failed:
#         mode = "a+" if os.path.exists("cds/tests/reports/failures.txt") else "w+"

#         # Reports folder must exist in within test folder for this to not error out.
#         with open("cds/tests/reports/failures.txt", mode) as f:
#             # Let's also access a fixture for the fun of it.
#             if "tmpdir" in item.fixturenames:
#                 extra = " (%s)" % item.funcargs["tmpdir"]
#             else:
#                 extra = ""

#             f.write(report.when + " - " + report.nodeid + extra + "\n")

# https://docs.pytest.org/en/latest/_modules/_pytest/hookspec.html#pytest_terminal_summary
@pytest.hookimpl(hookwrapper=True)
def pytest_terminal_summary(terminalreporter, exitstatus, config):
    '''
        Add a section to terminal summary reporting.

        Parameters:
        - terminalreporter (_pytest.terminal.TerminalReporter): the internal terminal reporter object.
        - exitstatus (int): the exit status that will be reported back to the OS
        - config (_pytest.config.Config): Access to configuration values, pluginmanager and plugin hooks - (config.args).

        Returns:
    '''
    outcome = yield

    rep = outcome.get_result()
    now = time.time()

    totalPassed = 0
    totalFailed = 0
    totalDuration = 0.00

    for passed in terminalreporter.stats.get('passed', []):  # type: TestReport
        totalPassed = totalPassed + 1
        totalDuration = totalDuration + passed.duration
        # print('passed! node_id:%s, duration: %s, details: %s' % (passed.nodeid, passed.duration, str(passed.longrepr)))
    
    for failed in terminalreporter.stats.get('failed', []):  # type: TestReport
        totalFailed = totalFailed + 1
        totalDuration = totalDuration + failed.duration
        # print('failed! node_id:%s, duration: %s, details: %s' % (failed.nodeid, failed.duration, str(failed.longrepr)))

    print('\n--')
    print('- Total Tests         :', totalFailed + totalPassed)
    print('- Total Passed        :', totalPassed)
    print('- Total Failed        :', totalFailed)
    print('- Total Test Duration : {:0.3} seconds'.format(totalDuration))
    print('- Finished            : {}'.format(time.strftime('%d %b %X', time.localtime(now))))
    print('-----------------')

def create_test_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    return app

class TestConfig(object):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'test.db')
    ENV = 'test'
    # Bcrypt algorithm hashing rounds (reduced for testing purposes only!)
    BCRYPT_LOG_ROUNDS = 4
    # Disable CSRF tokens in the Forms (only valid for testing purposes!)
    WTF_CSRF_ENABLED = False

def post_to_db(_data, _db):
    _db.session.add(_data)
    _db.session.commit()
    _db.session.execute('pragma foreign_keys=on')

class ModelTestBase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = create_test_app(TestConfig)

    def setUp(self):
        self.db = db
        self.db.init_app(self.app)
        self.app_context = self.app.app_context()
        self.app_context.push() # Engine binding event to memory
        self.db.session.execute('pragma foreign_keys=on')
        self.db.create_all()

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()
        self.app_context.pop() # Engine unbinding event from memory


# https://docs.pytest.org/en/latest/unittest.html ~ using unittest.Testcase with pytest
@pytest.fixture(scope="function")
def user(request):
    user = User(email='test@gmail.com', first_name='Lucy', last_name='Ferr', phone='7146668402', photo='photo.jpeg')
    user.set_password('some men just want to watch the world burn')
    request.cls.user = user

@pytest.fixture(scope="function")
def user_config(request):
    user_config = UserConfig(user_id=1, option='this user is wicked sick - admin privledges', vale='vale items')
    request.cls.user_config = user_config

@pytest.fixture(scope="function")
def role(request):
    role = Roles(user_id=1, name='supervisor')
    request.cls.role = role

@pytest.fixture(scope="function")
def permission(request):
    permission = Permissions(user_id=1, name='full admin')
    request.cls.permission = permission

@pytest.fixture(scope="function")
def role_permission_link(request):
    role_permission_link = RolesPermissionsLink(role_id=1, permission_id=1)
    request.cls.role_permission_link = role_permission_link
