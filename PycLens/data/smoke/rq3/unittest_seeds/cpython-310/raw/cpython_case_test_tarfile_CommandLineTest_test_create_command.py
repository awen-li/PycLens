# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: CommandLineTest_test_create_command

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    files = [support.findfile('tokenize_tests.txt'), support.findfile('tokenize_tests-no-coding-cookie-and-utf8-bom-sig-only.txt')]
    for opt in ('-c', '--create'):
        try:
            out = self.tarfilecmd(opt, tmpname, *files)
            self.assertEqual(out, b'')
            with tarfile.open(tmpname) as tar:
                tar.getmembers()
        finally:
            os_helper.unlink(tmpname)
