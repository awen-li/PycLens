# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_call.py
# case: CFunctionCallsErrorMessages_test_varargs18_kw

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg = 'invalid keyword argument for print\\(\\)$'
    with self.assertRaisesRegex(TypeError, msg):
        print(0, 1, **{BadStr('foo'): ','})
