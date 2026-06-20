# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: CommandLineTest_test_extract_command

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.make_simple_tarfile(tmpname)
    for opt in ('-e', '--extract'):
        try:
            with os_helper.temp_cwd(tarextdir):
                out = self.tarfilecmd(opt, tmpname)
            self.assertEqual(out, b'')
        finally:
            os_helper.rmtree(tarextdir)
