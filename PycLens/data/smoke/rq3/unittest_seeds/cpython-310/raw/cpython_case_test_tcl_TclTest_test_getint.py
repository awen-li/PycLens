# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tcl.py
# case: TclTest_test_getint

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tcl = self.interp.tk
    for i in self.get_integers():
        self.assertEqual(tcl.getint(' %d ' % i), i)
        if tcl_version >= (8, 5):
            self.assertEqual(tcl.getint(' %#o ' % i), i)
        self.assertEqual(tcl.getint((' %#o ' % i).replace('o', '')), i)
        self.assertEqual(tcl.getint(' %#x ' % i), i)
    if tcl_version < (8, 5):
        self.assertRaises(TclError, tcl.getint, str(2 ** 1000))
    self.assertEqual(tcl.getint(42), 42)
    self.assertRaises(TypeError, tcl.getint)
    self.assertRaises(TypeError, tcl.getint, '42', '10')
    self.assertRaises(TypeError, tcl.getint, b'42')
    self.assertRaises(TypeError, tcl.getint, 42.0)
    self.assertRaises(TclError, tcl.getint, 'a')
    self.assertRaises((TypeError, ValueError, TclError), tcl.getint, '42\x00')
    self.assertRaises((UnicodeEncodeError, ValueError, TclError), tcl.getint, '42\ud800')
