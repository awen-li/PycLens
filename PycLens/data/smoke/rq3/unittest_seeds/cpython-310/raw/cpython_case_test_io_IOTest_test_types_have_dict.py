# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: IOTest_test_types_have_dict

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    test = (self.IOBase(), self.RawIOBase(), self.TextIOBase(), self.StringIO(), self.BytesIO())
    for obj in test:
        self.assertTrue(hasattr(obj, '__dict__'))
