# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestZeroCopySendfile_test_exception_on_second_call

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def sendfile(*args, **kwargs):
        if not flag:
            flag.append(None)
            return orig_sendfile(*args, **kwargs)
        else:
            raise OSError(errno.EBADF, 'yo')
    flag = []
    orig_sendfile = os.sendfile
    with unittest.mock.patch('os.sendfile', create=True, side_effect=sendfile):
        with self.get_files() as (src, dst):
            with self.assertRaises(OSError) as cm:
                shutil._fastcopy_sendfile(src, dst)
    assert flag
    self.assertEqual(cm.exception.errno, errno.EBADF)
