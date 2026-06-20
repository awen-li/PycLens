# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: EnvironTests_test_ror_operator

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    overridden_key = '_TEST_VAR_'
    original_value = 'original_value'
    os.environ[overridden_key] = original_value
    new_vars_dict = {'_A_': '1', '_B_': '2', overridden_key: '3'}
    expected = dict(new_vars_dict)
    expected.update(os.environ)
    actual = new_vars_dict | os.environ
    self.assertDictEqual(expected, actual)
    self.assertEqual(original_value, actual[overridden_key])
    new_vars_items = new_vars_dict.items()
    self.assertIs(NotImplemented, os.environ.__ror__(new_vars_items))
    self._test_underlying_process_env('_A_', '')
    self._test_underlying_process_env(overridden_key, original_value)
