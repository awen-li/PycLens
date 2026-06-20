# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestSignaturePrivateHelpers_test_signature_get_bound_param

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    getter = inspect._signature_get_bound_param
    self.assertEqual(getter('($self)'), 'self')
    self.assertEqual(getter('($self, obj)'), 'self')
    self.assertEqual(getter('($cls, /, obj)'), 'cls')
