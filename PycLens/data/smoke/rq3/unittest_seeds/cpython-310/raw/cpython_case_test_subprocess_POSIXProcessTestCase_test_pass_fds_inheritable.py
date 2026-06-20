# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: POSIXProcessTestCase_test_pass_fds_inheritable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    script = support.findfile('fd_status.py', subdir='subprocessdata')
    (inheritable, non_inheritable) = os.pipe()
    self.addCleanup(os.close, inheritable)
    self.addCleanup(os.close, non_inheritable)
    os.set_inheritable(inheritable, True)
    os.set_inheritable(non_inheritable, False)
    pass_fds = (inheritable, non_inheritable)
    args = [sys.executable, script]
    args += list(map(str, pass_fds))
    p = subprocess.Popen(args, stdout=subprocess.PIPE, close_fds=True, pass_fds=pass_fds)
    (output, ignored) = p.communicate()
    fds = set(map(int, output.split(b',')))
    self.assertEqual(fds, set(pass_fds), 'output=%a' % output)
    self.assertEqual(os.get_inheritable(inheritable), True)
    self.assertEqual(os.get_inheritable(non_inheritable), False)
