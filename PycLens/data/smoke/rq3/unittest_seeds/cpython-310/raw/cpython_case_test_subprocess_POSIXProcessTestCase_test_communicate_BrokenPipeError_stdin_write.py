# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: POSIXProcessTestCase_test_communicate_BrokenPipeError_stdin_write

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    proc = subprocess.Popen(ZERO_RETURN_CMD)
    with proc, mock.patch.object(proc, 'stdin') as mock_proc_stdin:
        mock_proc_stdin.write.side_effect = BrokenPipeError
        proc.communicate(b'stuff')
        mock_proc_stdin.write.assert_called_once_with(b'stuff')
        mock_proc_stdin.close.assert_called_once_with()
