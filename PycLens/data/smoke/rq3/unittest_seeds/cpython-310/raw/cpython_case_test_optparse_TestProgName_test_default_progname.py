# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestProgName_test_default_progname

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    save_argv = sys.argv[:]
    try:
        sys.argv[0] = os.path.join('foo', 'bar', 'baz.py')
        parser = OptionParser('%prog ...', version='%prog 1.2')
        expected_usage = 'Usage: baz.py ...\n'
        self.assertUsage(parser, expected_usage)
        self.assertVersion(parser, 'baz.py 1.2')
        self.assertHelp(parser, expected_usage + '\n' + "Options:\n  --version   show program's version number and exit\n  -h, --help  show this help message and exit\n")
    finally:
        sys.argv[:] = save_argv
