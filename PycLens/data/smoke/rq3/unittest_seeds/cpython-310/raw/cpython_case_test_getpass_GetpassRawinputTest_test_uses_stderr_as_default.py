# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_getpass.py
# case: GetpassRawinputTest_test_uses_stderr_as_default

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    input = StringIO('input_string')
    prompt = 'some_prompt'
    with mock.patch('sys.stderr') as stderr:
        getpass._raw_input(prompt, input=input)
        stderr.write.assert_called_once_with(prompt)
