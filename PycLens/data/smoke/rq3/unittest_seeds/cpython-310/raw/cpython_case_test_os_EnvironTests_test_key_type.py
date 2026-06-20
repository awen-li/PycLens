# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: EnvironTests_test_key_type

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    missing = 'missingkey'
    self.assertNotIn(missing, os.environ)
    with self.assertRaises(KeyError) as cm:
        os.environ[missing]
    self.assertIs(cm.exception.args[0], missing)
    self.assertTrue(cm.exception.__suppress_context__)
    with self.assertRaises(KeyError) as cm:
        del os.environ[missing]
    self.assertIs(cm.exception.args[0], missing)
    self.assertTrue(cm.exception.__suppress_context__)
