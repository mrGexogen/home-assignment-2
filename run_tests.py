import unittest
import sys
from tests.auth import AuthTest
from tests.topic import TopicTest

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(TopicTest),
        unittest.makeSuite(AuthTest),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
