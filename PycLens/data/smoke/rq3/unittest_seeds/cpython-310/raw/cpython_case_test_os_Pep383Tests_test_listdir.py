# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: Pep383Tests_test_listdir

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expected = self.unicodefn
    found = set(os.listdir(self.dir))
    self.assertEqual(found, expected)
    current_directory = os.getcwd()
    try:
        os.chdir(os.sep)
        self.assertEqual(set(os.listdir()), set(os.listdir(os.sep)))
    finally:
        os.chdir(current_directory)
