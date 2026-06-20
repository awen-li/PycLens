# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestRmTree_test_rmtree_does_not_choke_on_failing_lstat

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        orig_lstat = os.lstat

        def raiser(fn, *args, **kwargs):
            if fn != TESTFN:
                raise OSError()
            else:
                return orig_lstat(fn)
        os.lstat = raiser
        os.mkdir(TESTFN)
        write_file((TESTFN, 'foo'), 'foo')
        shutil.rmtree(TESTFN)
    finally:
        os.lstat = orig_lstat
