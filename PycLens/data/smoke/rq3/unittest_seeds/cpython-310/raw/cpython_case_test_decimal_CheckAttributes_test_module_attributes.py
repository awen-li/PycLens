# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: CheckAttributes_test_module_attributes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(C.MAX_PREC, P.MAX_PREC)
    self.assertEqual(C.MAX_EMAX, P.MAX_EMAX)
    self.assertEqual(C.MIN_EMIN, P.MIN_EMIN)
    self.assertEqual(C.MIN_ETINY, P.MIN_ETINY)
    self.assertTrue(C.HAVE_THREADS is True or C.HAVE_THREADS is False)
    self.assertTrue(P.HAVE_THREADS is True or P.HAVE_THREADS is False)
    self.assertEqual(C.__version__, P.__version__)
    self.assertEqual(dir(C), dir(P))
