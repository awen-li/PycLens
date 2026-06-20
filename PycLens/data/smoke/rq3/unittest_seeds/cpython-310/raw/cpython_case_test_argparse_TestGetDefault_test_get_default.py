# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestGetDefault_test_get_default

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = ErrorRaisingArgumentParser()
    self.assertIsNone(parser.get_default('foo'))
    self.assertIsNone(parser.get_default('bar'))
    parser.add_argument('--foo')
    self.assertIsNone(parser.get_default('foo'))
    self.assertIsNone(parser.get_default('bar'))
    parser.add_argument('--bar', type=int, default=42)
    self.assertIsNone(parser.get_default('foo'))
    self.assertEqual(42, parser.get_default('bar'))
    parser.set_defaults(foo='badger')
    self.assertEqual('badger', parser.get_default('foo'))
    self.assertEqual(42, parser.get_default('bar'))
