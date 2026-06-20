# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: POSIXProcessTestCase_test_communicate_BrokenPipeError_stdin_flush

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    proc = subprocess.Popen([sys.executable, '-h'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    with proc, mock.patch.object(proc, 'stdin') as mock_proc_stdin, open(os.devnull, 'wb') as dev_null:
        mock_proc_stdin.flush.side_effect = BrokenPipeError
        mock_proc_stdin.fileno.return_value = dev_null.fileno()
        proc.communicate(b'stuff')
        mock_proc_stdin.flush.assert_called_once_with()
