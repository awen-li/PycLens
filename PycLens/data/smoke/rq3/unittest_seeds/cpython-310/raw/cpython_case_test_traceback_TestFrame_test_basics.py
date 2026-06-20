# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_traceback.py
# case: TestFrame_test_basics

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    linecache.clearcache()
    linecache.lazycache('f', globals())
    f = traceback.FrameSummary('f', 1, 'dummy')
    self.assertEqual(f, ('f', 1, 'dummy', '"""Test cases for traceback module"""'))
    self.assertEqual(tuple(f), ('f', 1, 'dummy', '"""Test cases for traceback module"""'))
    self.assertEqual(f, traceback.FrameSummary('f', 1, 'dummy'))
    self.assertEqual(f, tuple(f))
    self.assertEqual(tuple(f), f)
    self.assertIsNone(f.locals)
    self.assertNotEqual(f, object())
    self.assertEqual(f, ALWAYS_EQ)
