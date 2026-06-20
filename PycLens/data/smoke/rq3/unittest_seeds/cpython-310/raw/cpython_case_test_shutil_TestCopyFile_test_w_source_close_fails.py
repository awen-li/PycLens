# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestCopyFile_test_w_source_close_fails

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    srcfile = self.Faux(True)
    destfile = self.Faux()

    def _open(filename, mode='r'):
        if filename == 'srcfile':
            return srcfile
        if filename == 'destfile':
            return destfile
        assert 0
    with support.swap_attr(shutil, 'open', _open):
        with self.assertRaises(OSError):
            shutil.copyfile('srcfile', 'destfile')
    self.assertTrue(srcfile._entered)
    self.assertTrue(destfile._entered)
    self.assertFalse(destfile._raised)
    self.assertTrue(srcfile._exited_with[0] is None)
    self.assertTrue(srcfile._raised)
