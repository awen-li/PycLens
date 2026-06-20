# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_robotparser.py
# case: NetworkTestCase_test_read_404

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = urllib.robotparser.RobotFileParser(self.url('i-robot.txt'))
    parser.read()
    self.assertTrue(parser.allow_all)
    self.assertFalse(parser.disallow_all)
    self.assertEqual(parser.mtime(), 0)
    self.assertIsNone(parser.crawl_delay('*'))
    self.assertIsNone(parser.request_rate('*'))
