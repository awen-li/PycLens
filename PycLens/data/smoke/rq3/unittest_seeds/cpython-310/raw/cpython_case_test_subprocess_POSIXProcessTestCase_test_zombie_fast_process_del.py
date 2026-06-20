# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: POSIXProcessTestCase_test_zombie_fast_process_del

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = subprocess.Popen([sys.executable, '-c', 'import sys, time;time.sleep(0.2)'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    self.addCleanup(p.stdout.close)
    self.addCleanup(p.stderr.close)
    ident = id(p)
    pid = p.pid
    with warnings_helper.check_warnings(('', ResourceWarning)):
        p = None
    if mswindows:
        self.assertIsNone(subprocess._active)
    else:
        self.assertIn(ident, [id(o) for o in subprocess._active])
