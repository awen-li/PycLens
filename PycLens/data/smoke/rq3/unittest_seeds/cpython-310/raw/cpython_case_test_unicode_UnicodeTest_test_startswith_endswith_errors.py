# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_startswith_endswith_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for meth in ('foo'.startswith, 'foo'.endswith):
        with self.assertRaises(TypeError) as cm:
            meth(['f'])
        exc = str(cm.exception)
        self.assertIn('str', exc)
        self.assertIn('tuple', exc)
