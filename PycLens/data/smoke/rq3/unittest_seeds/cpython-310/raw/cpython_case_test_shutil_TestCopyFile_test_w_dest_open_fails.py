# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestCopyFile_test_w_dest_open_fails

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    srcfile = self.Faux()

    def _open(filename, mode='r'):
        if filename == 'srcfile':
            return srcfile
        if filename == 'destfile':
            raise OSError('Cannot open "destfile"')
        assert 0
    with support.swap_attr(shutil, 'open', _open):
        shutil.copyfile('srcfile', 'destfile')
    self.assertTrue(srcfile._entered)
    self.assertTrue(srcfile._exited_with[0] is OSError)
    self.assertEqual(srcfile._exited_with[1].args, ('Cannot open "destfile"',))
