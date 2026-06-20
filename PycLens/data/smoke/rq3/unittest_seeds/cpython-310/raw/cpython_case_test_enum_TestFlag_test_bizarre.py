# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestFlag_test_bizarre

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Bizarre(Flag):
        b = 3
        c = 4
        d = 6
    self.assertEqual(repr(Bizarre(7)), '<Bizarre.d|c|b: 7>')
