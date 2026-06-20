# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestZeroCopySendfile_test_big_chunk

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    mock = unittest.mock.Mock()
    mock.st_size = self.FILESIZE + 100 * 1024 * 1024
    with unittest.mock.patch('os.fstat', return_value=mock) as m:
        with self.get_files() as (src, dst):
            shutil._fastcopy_sendfile(src, dst)
            assert m.called
    self.assertEqual(read_file(TESTFN2, binary=True), self.FILEDATA)
