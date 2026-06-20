# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_resize

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from _testcapi import getargs_u
    for length in range(1, 100, 7):
        text = 'a' * length + 'b'
        with self.assertWarns(DeprecationWarning):
            abc = getargs_u(text)
        self.assertEqual(abc, text)
        text += 'c'
        with self.assertWarns(DeprecationWarning):
            abcdef = getargs_u(text)
        self.assertNotEqual(abc, abcdef)
        self.assertEqual(abcdef, text)
