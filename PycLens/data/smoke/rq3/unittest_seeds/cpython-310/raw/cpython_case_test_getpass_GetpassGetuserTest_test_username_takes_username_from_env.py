# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_getpass.py
# case: GetpassGetuserTest_test_username_takes_username_from_env

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expected_name = 'some_name'
    environ.get.return_value = expected_name
    self.assertEqual(expected_name, getpass.getuser())
