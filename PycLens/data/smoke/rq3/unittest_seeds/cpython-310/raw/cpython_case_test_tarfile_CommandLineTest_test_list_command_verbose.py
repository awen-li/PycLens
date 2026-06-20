# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: CommandLineTest_test_list_command_verbose

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for tar_name in testtarnames:
        with support.captured_stdout() as t:
            with tarfile.open(tar_name, 'r') as tf:
                tf.list(verbose=True)
        expected = t.getvalue().encode('ascii', 'backslashreplace')
        for opt in ('-v', '--verbose'):
            out = self.tarfilecmd(opt, '-l', tar_name, PYTHONIOENCODING='ascii')
            self.assertEqual(out, expected)
