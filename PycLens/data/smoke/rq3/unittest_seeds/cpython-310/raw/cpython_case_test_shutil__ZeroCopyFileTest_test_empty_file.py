# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: _ZeroCopyFileTest_test_empty_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    srcname = TESTFN + 'src'
    dstname = TESTFN + 'dst'
    self.addCleanup(lambda : os_helper.unlink(srcname))
    self.addCleanup(lambda : os_helper.unlink(dstname))
    with open(srcname, 'wb'):
        pass
    with open(srcname, 'rb') as src:
        with open(dstname, 'wb') as dst:
            self.zerocopy_fun(src, dst)
    self.assertEqual(read_file(dstname, binary=True), b'')
