# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_call.py
# case: TestCallingConventions_test_fastcall_keywords

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(self.obj.meth_fastcall_keywords(1, 2, a=3, b=4), (self.expected_self, (1, 2), {'a': 3, 'b': 4}))
