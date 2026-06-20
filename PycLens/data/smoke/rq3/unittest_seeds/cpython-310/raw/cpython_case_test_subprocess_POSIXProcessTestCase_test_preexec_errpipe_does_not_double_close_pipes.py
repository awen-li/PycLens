# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: POSIXProcessTestCase_test_preexec_errpipe_does_not_double_close_pipes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def raise_it():
        raise subprocess.SubprocessError('force the _execute_child() errpipe_data path.')
    with self.assertRaises(subprocess.SubprocessError):
        self._TestExecuteChildPopen(self, ZERO_RETURN_CMD, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, preexec_fn=raise_it)
