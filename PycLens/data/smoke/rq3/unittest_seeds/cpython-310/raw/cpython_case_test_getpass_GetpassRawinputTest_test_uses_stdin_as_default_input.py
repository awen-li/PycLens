# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_getpass.py
# case: GetpassRawinputTest_test_uses_stdin_as_default_input

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    mock_input.readline.return_value = 'input_string'
    getpass._raw_input(stream=StringIO())
    mock_input.readline.assert_called_once_with()
