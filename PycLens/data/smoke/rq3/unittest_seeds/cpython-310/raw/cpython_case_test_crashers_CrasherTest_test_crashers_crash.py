# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_crashers.py
# case: CrasherTest_test_crashers_crash

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for fname in glob.glob(CRASHER_FILES):
        if os.path.basename(fname) in infinite_loops:
            continue
        if test.support.verbose:
            print('Checking crasher:', fname)
        assert_python_failure(fname)
