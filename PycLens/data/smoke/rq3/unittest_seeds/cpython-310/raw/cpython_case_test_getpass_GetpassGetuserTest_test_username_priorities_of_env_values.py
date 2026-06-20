# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_getpass.py
# case: GetpassGetuserTest_test_username_priorities_of_env_values

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    environ.get.return_value = None
    try:
        getpass.getuser()
    except ImportError:
        pass
    self.assertEqual(environ.get.call_args_list, [mock.call(x) for x in ('LOGNAME', 'USER', 'LNAME', 'USERNAME')])
