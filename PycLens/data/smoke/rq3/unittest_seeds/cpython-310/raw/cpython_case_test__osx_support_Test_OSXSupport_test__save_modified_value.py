# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__osx_support.py
# case: Test_OSXSupport_test__save_modified_value

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    config_vars = {'CC': 'gcc-test -pthreads'}
    expected_vars = {'CC': 'clang -pthreads'}
    self.add_expected_saved_initial_values(config_vars, expected_vars)
    cv = 'CC'
    newvalue = 'clang -pthreads'
    _osx_support._save_modified_value(config_vars, cv, newvalue)
    self.assertEqual(expected_vars, config_vars)
