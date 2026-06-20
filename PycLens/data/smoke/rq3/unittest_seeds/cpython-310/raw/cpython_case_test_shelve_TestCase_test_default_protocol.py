# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shelve.py
# case: TestCase_test_default_protocol

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with shelve.Shelf({}) as s:
        self.assertEqual(s._protocol, pickle.DEFAULT_PROTOCOL)
