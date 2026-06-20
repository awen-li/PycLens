# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: CommandLineTest_test_test_command_verbose

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for tar_name in testtarnames:
        for opt in ('-v', '--verbose'):
            out = self.tarfilecmd(opt, '-t', tar_name, PYTHONIOENCODING='utf-8')
            self.assertIn(b'is a tar archive.\n', out)
