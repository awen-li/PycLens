# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: POSIXProcessTestCase_test_exception_errpipe_bad_data

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    error_data = b'\xff\x00\xde\xad'

    def bad_error(*args):
        errpipe_write = args[13]
        os.write(errpipe_write, error_data)
        return 0
    fork_exec.side_effect = bad_error
    with mock.patch('subprocess.os.waitpid', side_effect=ChildProcessError):
        with self.assertRaises(subprocess.SubprocessError) as e:
            self.PopenNoDestructor(['non_existent_command'])
    self.assertIn(repr(error_data), str(e.exception))
