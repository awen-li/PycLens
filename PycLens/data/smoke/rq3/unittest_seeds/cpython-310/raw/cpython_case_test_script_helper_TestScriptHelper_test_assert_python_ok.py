# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_script_helper.py
# case: TestScriptHelper_test_assert_python_ok

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    t = script_helper.assert_python_ok('-c', 'import sys; sys.exit(0)')
    self.assertEqual(0, t[0], 'return code was not 0')
