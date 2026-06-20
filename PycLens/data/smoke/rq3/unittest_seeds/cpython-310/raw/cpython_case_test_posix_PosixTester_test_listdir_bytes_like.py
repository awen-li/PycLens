# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: PosixTester_test_listdir_bytes_like

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for cls in (bytearray, memoryview):
        with self.assertWarns(DeprecationWarning):
            names = posix.listdir(cls(b'.'))
        self.assertIn(os.fsencode(os_helper.TESTFN), names)
        for name in names:
            self.assertIs(type(name), bytes)
