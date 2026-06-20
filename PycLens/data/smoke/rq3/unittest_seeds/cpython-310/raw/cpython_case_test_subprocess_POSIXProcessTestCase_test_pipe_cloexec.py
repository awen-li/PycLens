# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: POSIXProcessTestCase_test_pipe_cloexec

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sleeper = support.findfile('input_reader.py', subdir='subprocessdata')
    fd_status = support.findfile('fd_status.py', subdir='subprocessdata')
    p1 = subprocess.Popen([sys.executable, sleeper], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=False)
    self.addCleanup(p1.communicate, b'')
    p2 = subprocess.Popen([sys.executable, fd_status], stdout=subprocess.PIPE, close_fds=False)
    (output, error) = p2.communicate()
    result_fds = set(map(int, output.split(b',')))
    unwanted_fds = set([p1.stdin.fileno(), p1.stdout.fileno(), p1.stderr.fileno()])
    self.assertFalse(result_fds & unwanted_fds, 'Expected no fds from %r to be open in child, found %r' % (unwanted_fds, result_fds & unwanted_fds))
