# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestCopyFile_test_w_source_open_fails

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def _open(filename, mode='r'):
        if filename == 'srcfile':
            raise OSError('Cannot open "srcfile"')
        assert 0
    with support.swap_attr(shutil, 'open', _open):
        with self.assertRaises(OSError):
            shutil.copyfile('srcfile', 'destfile')
