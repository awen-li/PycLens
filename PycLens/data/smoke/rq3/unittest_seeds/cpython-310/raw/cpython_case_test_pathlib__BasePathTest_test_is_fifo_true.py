# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePathTest_test_is_fifo_true

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls(BASE, 'myfifo')
    try:
        os.mkfifo(str(P))
    except PermissionError as e:
        self.skipTest('os.mkfifo(): %s' % e)
    self.assertTrue(P.is_fifo())
    self.assertFalse(P.is_socket())
    self.assertFalse(P.is_file())
    self.assertIs(self.cls(BASE, 'myfifo\udfff').is_fifo(), False)
    self.assertIs(self.cls(BASE, 'myfifo\x00').is_fifo(), False)
