# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestVersion_test_version

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.parser = InterceptingOptionParser(usage=SUPPRESS_USAGE, version='%prog 0.1')
    save_argv = sys.argv[:]
    try:
        sys.argv[0] = os.path.join(os.curdir, 'foo', 'bar')
        self.assertOutput(['--version'], 'bar 0.1\n')
    finally:
        sys.argv[:] = save_argv
