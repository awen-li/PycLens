# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: CommandLineTest_test_create_command_dotless_filename

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    files = [support.findfile('tokenize_tests.txt')]
    try:
        out = self.tarfilecmd('-c', dotlessname, *files)
        self.assertEqual(out, b'')
        with tarfile.open(dotlessname) as tar:
            tar.getmembers()
    finally:
        os_helper.unlink(dotlessname)
