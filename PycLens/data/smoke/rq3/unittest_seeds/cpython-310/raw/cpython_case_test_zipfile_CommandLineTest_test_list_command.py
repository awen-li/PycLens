# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: CommandLineTest_test_list_command

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    zip_name = findfile('zipdir.zip')
    t = io.StringIO()
    with zipfile.ZipFile(zip_name, 'r') as tf:
        tf.printdir(t)
    expected = t.getvalue().encode('ascii', 'backslashreplace')
    for opt in ('-l', '--list'):
        out = self.zipfilecmd(opt, zip_name, PYTHONIOENCODING='ascii:backslashreplace')
        self.assertEqual(out, expected)
