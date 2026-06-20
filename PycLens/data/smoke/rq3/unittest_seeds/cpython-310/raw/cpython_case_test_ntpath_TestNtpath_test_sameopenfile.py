# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ntpath.py
# case: TestNtpath_test_sameopenfile

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with TemporaryFile() as tf1, TemporaryFile() as tf2:
        self.assertTrue(ntpath.sameopenfile(tf1.fileno(), tf1.fileno()))
        self.assertFalse(ntpath.sameopenfile(tf1.fileno(), tf2.fileno()))
        if sys.platform == 'win32':
            with self.assertRaises(OSError):
                ntpath.sameopenfile(-1, -1)
