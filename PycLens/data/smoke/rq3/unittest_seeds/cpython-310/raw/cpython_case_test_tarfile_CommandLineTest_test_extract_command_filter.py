# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: CommandLineTest_test_extract_command_filter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.make_evil_tarfile(tmpname)
    destdir = os.path.join(tarextdir, 'dest')
    os.mkdir(tarextdir)
    try:
        with os_helper.temp_cwd(destdir):
            self.tarfilecmd_failure('-e', tmpname, '-v', '--filter', 'data')
            out = self.tarfilecmd('-e', tmpname, '-v', '--filter', 'fully_trusted', PYTHONIOENCODING='utf-8')
            self.assertIn(b' file is extracted.', out)
    finally:
        os_helper.rmtree(tarextdir)
