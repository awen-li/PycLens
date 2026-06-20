# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestRmTree_test_rmtree_on_symlink

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    os.mkdir(TESTFN)
    try:
        src = os.path.join(TESTFN, 'cheese')
        dst = os.path.join(TESTFN, 'shop')
        os.mkdir(src)
        os.symlink(src, dst)
        self.assertRaises(OSError, shutil.rmtree, dst)
        shutil.rmtree(dst, ignore_errors=True)
    finally:
        shutil.rmtree(TESTFN, ignore_errors=True)
