# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tcl.py
# case: TclTest_test_getdouble

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tcl = self.interp.tk
    self.assertEqual(tcl.getdouble(' 42 '), 42.0)
    self.assertEqual(tcl.getdouble(' 42.5 '), 42.5)
    self.assertEqual(tcl.getdouble(42.5), 42.5)
    self.assertEqual(tcl.getdouble(42), 42.0)
    self.assertRaises(TypeError, tcl.getdouble)
    self.assertRaises(TypeError, tcl.getdouble, '42.5', '10')
    self.assertRaises(TypeError, tcl.getdouble, b'42.5')
    self.assertRaises(TclError, tcl.getdouble, 'a')
    self.assertRaises((TypeError, ValueError, TclError), tcl.getdouble, '42.5\x00')
    self.assertRaises((UnicodeEncodeError, ValueError, TclError), tcl.getdouble, '42.5\ud800')
