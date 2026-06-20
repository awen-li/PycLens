# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: POSIXProcessTestCase_test_exception_errpipe_normal

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def proper_error(*args):
        errpipe_write = args[13]
        err_code = '{:x}'.format(errno.EISDIR).encode()
        os.write(errpipe_write, b'OSError:' + err_code + b':')
        return 0
    fork_exec.side_effect = proper_error
    with mock.patch('subprocess.os.waitpid', side_effect=ChildProcessError):
        with self.assertRaises(IsADirectoryError):
            self.PopenNoDestructor(['non_existent_command'])
