# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_getpass.py
# case: GetpassRawinputTest_test_flushes_stream_after_prompt

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    stream = mock.Mock(spec=StringIO)
    input = StringIO('input_string')
    getpass._raw_input('some_prompt', stream, input=input)
    stream.flush.assert_called_once_with()
