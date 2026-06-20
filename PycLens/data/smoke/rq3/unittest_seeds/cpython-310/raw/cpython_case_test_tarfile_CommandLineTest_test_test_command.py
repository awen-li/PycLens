# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: CommandLineTest_test_test_command

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for tar_name in testtarnames:
        for opt in ('-t', '--test'):
            out = self.tarfilecmd(opt, tar_name)
            self.assertEqual(out, b'')
