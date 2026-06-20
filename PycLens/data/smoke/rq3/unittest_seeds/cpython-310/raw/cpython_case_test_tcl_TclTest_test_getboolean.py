# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tcl.py
# case: TclTest_test_getboolean

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tcl = self.interp.tk
    self.assertIs(tcl.getboolean('on'), True)
    self.assertIs(tcl.getboolean('1'), True)
    self.assertIs(tcl.getboolean(42), True)
    self.assertIs(tcl.getboolean(0), False)
    self.assertRaises(TypeError, tcl.getboolean)
    self.assertRaises(TypeError, tcl.getboolean, 'on', '1')
    self.assertRaises(TypeError, tcl.getboolean, b'on')
    self.assertRaises(TypeError, tcl.getboolean, 1.0)
    self.assertRaises(TclError, tcl.getboolean, 'a')
    self.assertRaises((TypeError, ValueError, TclError), tcl.getboolean, 'on\x00')
    self.assertRaises((UnicodeEncodeError, ValueError, TclError), tcl.getboolean, 'on\ud800')
