# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestPositionalsGroups_test_group_first

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = ErrorRaisingArgumentParser()
    group = parser.add_argument_group('xxx')
    group.add_argument('foo')
    parser.add_argument('bar')
    parser.add_argument('baz')
    expected = NS(foo='1', bar='2', baz='3')
    result = parser.parse_args('1 2 3'.split())
    self.assertEqual(expected, result)
