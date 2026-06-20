# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_script_helper.py
# case: TestScriptHelper_test_assert_python_ok_raises

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(AssertionError) as error_context:
        script_helper.assert_python_ok('-c', 'sys.exit(0)')
    error_msg = str(error_context.exception)
    self.assertIn('command line:', error_msg)
    self.assertIn('sys.exit(0)', error_msg, msg='unexpected command line')
