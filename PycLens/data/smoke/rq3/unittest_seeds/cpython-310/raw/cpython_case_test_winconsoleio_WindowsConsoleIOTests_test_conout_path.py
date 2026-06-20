# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_winconsoleio.py
# case: WindowsConsoleIOTests_test_conout_path

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    temp_path = tempfile.mkdtemp()
    self.addCleanup(os_helper.rmtree, temp_path)
    conout_path = os.path.join(temp_path, 'CONOUT$')
    with open(conout_path, 'wb', buffering=0) as f:
        if (6, 1) < sys.getwindowsversion()[:3] < (10, 0, 22000):
            self.assertIsInstance(f, ConIO)
        else:
            self.assertNotIsInstance(f, ConIO)
