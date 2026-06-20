# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: POSIXProcessTestCase_test_send_signal_race2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = subprocess.Popen([sys.executable, '-c', 'exit(1)'])
    while not p.returncode:
        p.poll()
    with mock.patch.object(p, 'poll', new=lambda : None):
        p.returncode = None
        p.send_signal(signal.SIGTERM)
