# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ProcessTestCase_test_communicate_pipe_fd_leak

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for stdin_pipe in (False, True):
        for stdout_pipe in (False, True):
            for stderr_pipe in (False, True):
                options = {}
                if stdin_pipe:
                    options['stdin'] = subprocess.PIPE
                if stdout_pipe:
                    options['stdout'] = subprocess.PIPE
                if stderr_pipe:
                    options['stderr'] = subprocess.PIPE
                if not options:
                    continue
                p = subprocess.Popen(ZERO_RETURN_CMD, **options)
                p.communicate()
                if p.stdin is not None:
                    self.assertTrue(p.stdin.closed)
                if p.stdout is not None:
                    self.assertTrue(p.stdout.closed)
                if p.stderr is not None:
                    self.assertTrue(p.stderr.closed)
