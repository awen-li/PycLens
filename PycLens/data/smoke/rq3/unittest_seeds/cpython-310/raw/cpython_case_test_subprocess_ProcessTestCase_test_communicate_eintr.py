# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ProcessTestCase_test_communicate_eintr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def handler(signum, frame):
        pass
    old_handler = signal.signal(signal.SIGUSR1, handler)
    self.addCleanup(signal.signal, signal.SIGUSR1, old_handler)
    args = [sys.executable, '-c', 'import os, signal;os.kill(os.getppid(), signal.SIGUSR1)']
    for stream in ('stdout', 'stderr'):
        kw = {stream: subprocess.PIPE}
        with subprocess.Popen(args, **kw) as process:
            process.communicate()
