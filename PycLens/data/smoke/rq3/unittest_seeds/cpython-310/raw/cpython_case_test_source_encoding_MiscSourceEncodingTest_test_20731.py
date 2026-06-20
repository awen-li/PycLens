# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_source_encoding.py
# case: MiscSourceEncodingTest_test_20731

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sub = subprocess.Popen([sys.executable, os.path.join(os.path.dirname(__file__), 'coding20731.py')], stderr=subprocess.PIPE)
    err = sub.communicate()[1]
    self.assertEqual(sub.returncode, 0)
    self.assertNotIn(b'SyntaxError', err)
