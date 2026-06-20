# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_script_helper.py
# case: TestScriptHelperEnvironment_test_interpreter_requires_environment_with_pythonhome

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with mock.patch.dict(os.environ):
        os.environ['PYTHONHOME'] = 'MockedHome'
        self.assertTrue(script_helper.interpreter_requires_environment())
        self.assertTrue(script_helper.interpreter_requires_environment())
        self.assertEqual(0, mock_check_call.call_count)
