# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_script_helper.py
# case: TestScriptHelper_test_assert_python_isolated_when_env_not_required

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with mock.patch.object(script_helper, 'interpreter_requires_environment', return_value=False) as mock_ire_func:
        mock_popen.side_effect = RuntimeError('bail out of unittest')
        try:
            script_helper._assert_python(True, '-c', 'None')
        except RuntimeError as err:
            self.assertEqual('bail out of unittest', err.args[0])
        self.assertEqual(1, mock_popen.call_count)
        self.assertEqual(1, mock_ire_func.call_count)
        popen_command = mock_popen.call_args[0][0]
        self.assertEqual(sys.executable, popen_command[0])
        self.assertIn('None', popen_command)
        self.assertIn('-I', popen_command)
        self.assertNotIn('-E', popen_command)
