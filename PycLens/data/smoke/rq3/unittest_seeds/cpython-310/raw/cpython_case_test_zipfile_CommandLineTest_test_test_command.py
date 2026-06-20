# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: CommandLineTest_test_test_command

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    zip_name = findfile('zipdir.zip')
    for opt in ('-t', '--test'):
        out = self.zipfilecmd(opt, zip_name)
        self.assertEqual(out.rstrip(), b'Done testing')
    zip_name = findfile('testtar.tar')
    (rc, out, err) = self.zipfilecmd_failure('-t', zip_name)
    self.assertEqual(out, b'')
