# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_script_helper.py
# case: TestScriptHelperEnvironment_test_interpreter_requires_environment_details

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with mock.patch.dict(os.environ):
        os.environ.pop('PYTHONHOME', None)
        script_helper.interpreter_requires_environment()
        self.assertFalse(script_helper.interpreter_requires_environment())
        self.assertFalse(script_helper.interpreter_requires_environment())
        self.assertEqual(1, mock_check_call.call_count)
        check_call_command = mock_check_call.call_args[0][0]
        self.assertEqual(sys.executable, check_call_command[0])
        self.assertIn('-E', check_call_command)
