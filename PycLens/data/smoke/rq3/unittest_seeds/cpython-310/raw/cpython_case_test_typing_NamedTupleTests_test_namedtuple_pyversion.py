# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: NamedTupleTests_test_namedtuple_pyversion

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if sys.version_info[:2] < (3, 6):
        with self.assertRaises(TypeError):
            NamedTuple('Name', one=int, other=str)
        with self.assertRaises(TypeError):

            class NotYet(NamedTuple):
                whatever = 0
