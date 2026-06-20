# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestNamedTuple_test_keyword_only_arguments

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(TypeError):
        NT = namedtuple('NT', ['x', 'y'], True)
    NT = namedtuple('NT', ['abc', 'def'], rename=True)
    self.assertEqual(NT._fields, ('abc', '_1'))
    with self.assertRaises(TypeError):
        NT = namedtuple('NT', ['abc', 'def'], False, True)
