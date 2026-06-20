# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_winreg.py
# case: Win64WinregTests_test_exception_numbers

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(FileNotFoundError) as ctx:
        QueryValue(HKEY_CLASSES_ROOT, 'some_value_that_does_not_exist')
