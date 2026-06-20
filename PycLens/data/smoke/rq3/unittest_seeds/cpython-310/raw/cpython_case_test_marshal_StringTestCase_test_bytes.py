# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_marshal.py
# case: StringTestCase_test_bytes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for s in [b'', b'Andr\xe8 Previn', b'abc', b' ' * 10000]:
        self.helper(s)
