# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: POSIXProcessTestCase_test_wait_when_sigchild_ignored

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sigchild_ignore = support.findfile('sigchild_ignore.py', subdir='subprocessdata')
    p = subprocess.Popen([sys.executable, sigchild_ignore], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (stdout, stderr) = p.communicate()
    self.assertEqual(0, p.returncode, 'sigchild_ignore.py exited non-zero with this error:\n%s' % stderr.decode('utf-8'))
