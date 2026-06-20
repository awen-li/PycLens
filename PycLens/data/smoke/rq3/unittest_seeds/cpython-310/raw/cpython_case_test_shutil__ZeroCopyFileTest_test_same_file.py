# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: _ZeroCopyFileTest_test_same_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.addCleanup(self.reset)
    with self.get_files() as (src, dst):
        with self.assertRaises(Exception):
            self.zerocopy_fun(src, src)
    self.assertEqual(read_file(TESTFN, binary=True), self.FILEDATA)
