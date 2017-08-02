import unittest
import transaction

from pyramid import testing


def dummy_request(dbsession):
    return testing.DummyRequest(dbsession=dbsession)


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp(settings={
            'sqlalchemy.url': 'sqlite:///:memory:'
        })
        self.config.include('.models')
        settings = self.config.get_settings()

    def init_database(self):
        pass

    def tearDown(self):
        testing.tearDown()
        transaction.abort()


class TestMyViewSuccessCondition(BaseTest):

    def setUp(self):
        super(TestMyViewSuccessCondition, self).setUp()
        self.init_database()

        from .models import MyModel

        model = MyModel(name='one', value=55)

    def test_passing_view(self):
        from .views.default import my_view

class TestMyViewFailureCondition(BaseTest):

    def test_failing_view(self):
        from .views.default import my_view
