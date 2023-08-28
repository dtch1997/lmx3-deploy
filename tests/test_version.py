import unittest

import lxm3_deploy


class VersionTestCase(unittest.TestCase):
    """ Version tests """

    def test_version(self):
        """ check lxm3_deploy exposes a version attribute """
        self.assertTrue(hasattr(lxm3_deploy, "__version__"))
        self.assertIsInstance(lxm3_deploy.__version__, str)


if __name__ == "__main__":
    unittest.main()
