# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: POSIXProcessTestCase_test_communicate_BrokenPipeError_stdin_close_with_timeout

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    proc = subprocess.Popen([sys.executable, '-h'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    with proc, mock.patch.object(proc, 'stdin') as mock_proc_stdin:
        mock_proc_stdin.close.side_effect = BrokenPipeError
        proc.communicate(timeout=999)
        mock_proc_stdin.close.assert_called_once_with()
