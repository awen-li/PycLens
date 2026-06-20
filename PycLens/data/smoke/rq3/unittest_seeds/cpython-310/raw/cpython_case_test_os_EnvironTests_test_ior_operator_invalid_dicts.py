# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: EnvironTests_test_ior_operator_invalid_dicts

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    os_environ_copy = os.environ.copy()
    with self.assertRaises(TypeError):
        dict_with_bad_key = {1: '_A_'}
        os.environ |= dict_with_bad_key
    with self.assertRaises(TypeError):
        dict_with_bad_val = {'_A_': 1}
        os.environ |= dict_with_bad_val
    self.assertEqual(os_environ_copy, os.environ)
