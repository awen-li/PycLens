# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: _ZeroCopyFileTest_test_regular_copy

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.get_files() as (src, dst):
        self.zerocopy_fun(src, dst)
    self.assertEqual(read_file(TESTFN2, binary=True), self.FILEDATA)
    with self.get_files() as (src, dst):
        with unittest.mock.patch('shutil.copyfileobj') as m:
            shutil.copyfile(TESTFN, TESTFN2)
        assert not m.called
