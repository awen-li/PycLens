# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestZeroCopySendfile_test_file2file_not_supported

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    assert shutil._USE_CP_SENDFILE
    try:
        with unittest.mock.patch(self.PATCHPOINT, side_effect=OSError(errno.ENOTSOCK, 'yo')) as m:
            with self.get_files() as (src, dst):
                with self.assertRaises(_GiveupOnFastCopy):
                    shutil._fastcopy_sendfile(src, dst)
            assert m.called
        assert not shutil._USE_CP_SENDFILE
        with unittest.mock.patch(self.PATCHPOINT) as m:
            shutil.copyfile(TESTFN, TESTFN2)
            assert not m.called
    finally:
        shutil._USE_CP_SENDFILE = True
