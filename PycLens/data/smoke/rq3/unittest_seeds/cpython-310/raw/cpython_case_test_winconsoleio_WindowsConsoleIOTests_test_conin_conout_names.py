# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_winconsoleio.py
# case: WindowsConsoleIOTests_test_conin_conout_names

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = open('\\\\.\\conin$', 'rb', buffering=0)
    self.assertIsInstance(f, ConIO)
    f.close()
    f = open('//?/conout$', 'wb', buffering=0)
    self.assertIsInstance(f, ConIO)
    f.close()
