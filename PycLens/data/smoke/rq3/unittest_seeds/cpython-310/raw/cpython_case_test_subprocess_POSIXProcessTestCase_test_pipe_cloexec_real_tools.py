# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: POSIXProcessTestCase_test_pipe_cloexec_real_tools

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    qcat = support.findfile('qcat.py', subdir='subprocessdata')
    qgrep = support.findfile('qgrep.py', subdir='subprocessdata')
    subdata = b'zxcvbn'
    data = subdata * 4 + b'\n'
    p1 = subprocess.Popen([sys.executable, qcat], stdin=subprocess.PIPE, stdout=subprocess.PIPE, close_fds=False)
    p2 = subprocess.Popen([sys.executable, qgrep, subdata], stdin=p1.stdout, stdout=subprocess.PIPE, close_fds=False)
    self.addCleanup(p1.wait)
    self.addCleanup(p2.wait)

    def kill_p1():
        try:
            p1.terminate()
        except ProcessLookupError:
            pass

    def kill_p2():
        try:
            p2.terminate()
        except ProcessLookupError:
            pass
    self.addCleanup(kill_p1)
    self.addCleanup(kill_p2)
    p1.stdin.write(data)
    p1.stdin.close()
    (readfiles, ignored1, ignored2) = select.select([p2.stdout], [], [], 10)
    self.assertTrue(readfiles, 'The child hung')
    self.assertEqual(p2.stdout.read(), data)
    p1.stdout.close()
    p2.stdout.close()
