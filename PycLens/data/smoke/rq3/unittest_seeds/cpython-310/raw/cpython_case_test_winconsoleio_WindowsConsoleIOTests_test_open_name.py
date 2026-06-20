# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_winconsoleio.py
# case: WindowsConsoleIOTests_test_open_name

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(ValueError, ConIO, sys.executable)
    f = ConIO('CON')
    self.assertTrue(f.readable())
    self.assertFalse(f.writable())
    self.assertIsNotNone(f.fileno())
    f.close()
    f.close()
    f = ConIO('CONIN$')
    self.assertTrue(f.readable())
    self.assertFalse(f.writable())
    self.assertIsNotNone(f.fileno())
    f.close()
    f.close()
    f = ConIO('CONOUT$', 'w')
    self.assertFalse(f.readable())
    self.assertTrue(f.writable())
    self.assertIsNotNone(f.fileno())
    f.close()
    f.close()
    if sys.getwindowsversion()[:3] < (10, 0, 22000):
        f = open('C:/con', 'rb', buffering=0)
        self.assertIsInstance(f, ConIO)
        f.close()
