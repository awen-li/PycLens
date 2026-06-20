# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: EnvironTests_test_ior_operator_key_value_iterable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    overridden_key = '_TEST_VAR_'
    os.environ[overridden_key] = 'original_value'
    new_vars_items = (('_A_', '1'), ('_B_', '2'), (overridden_key, '3'))
    expected = dict(os.environ)
    expected.update(new_vars_items)
    os.environ |= new_vars_items
    self.assertEqual(expected, os.environ)
    self.assertEqual('3', os.environ[overridden_key])
    self._test_underlying_process_env('_A_', '1')
    self._test_underlying_process_env(overridden_key, '3')
