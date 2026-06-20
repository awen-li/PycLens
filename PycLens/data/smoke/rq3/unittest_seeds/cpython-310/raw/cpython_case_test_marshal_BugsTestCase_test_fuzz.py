# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_marshal.py
# case: BugsTestCase_test_fuzz

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for i in range(256):
        c = bytes([i])
        try:
            marshal.loads(c)
        except Exception:
            pass
