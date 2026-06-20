# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: POSIXProcessTestCase_test_small_errpipe_write_fd

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    new_stdin = os.dup(0)
    new_stdout = os.dup(1)
    try:
        os.close(0)
        os.close(1)
        subprocess.Popen([sys.executable, '-c', "print('AssertionError:0:CLOEXEC failure.')"]).wait()
    finally:
        os.dup2(new_stdin, 0)
        os.dup2(new_stdout, 1)
        os.close(new_stdin)
        os.close(new_stdout)
