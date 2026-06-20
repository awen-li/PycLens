# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pickle.py
# case: CPicklerUnpicklerObjectTests_test_issue18339

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    unpickler = self.unpickler_class(io.BytesIO())
    with self.assertRaises(TypeError):
        unpickler.memo = object
    with self.assertRaises(ValueError):
        unpickler.memo = {-1: None}
    unpickler.memo = {1: None}
