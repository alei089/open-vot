from __future__ import absolute_import

import unittest
import random

from lib.managers import ManagerKCF


class TestManagerKCF(unittest.TestCase):

    def setUp(self):
        self.otb_dir = 'data/OTB'
        self.manager = ManagerKCF()

    def tearDown(self):
        pass

    def test_track(self):
        self.manager.track(self.otb_dir)


if __name__ == '__main__':
    unittest.main()
