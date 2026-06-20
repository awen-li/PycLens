# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_script_helper.py
# case: TestScriptHelper_test_assert_python_failure

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (rc, out, err) = script_helper.assert_python_failure('-c', 'sys.exit(0)')
    self.assertNotEqual(0, rc, 'return code should not be 0')
