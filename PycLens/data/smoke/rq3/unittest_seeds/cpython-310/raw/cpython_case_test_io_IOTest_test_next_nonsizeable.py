# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: IOTest_test_next_nonsizeable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class R(self.IOBase):

        def __next__(self):
            return None
    self.assertRaises(TypeError, R().readlines, 1)
