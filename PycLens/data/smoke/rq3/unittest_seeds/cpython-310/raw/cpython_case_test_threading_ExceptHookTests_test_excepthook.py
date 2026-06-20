# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading.py
# case: ExceptHookTests_test_excepthook

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with support.captured_output('stderr') as stderr:
        thread = ThreadRunFail(name='excepthook thread')
        thread.start()
        thread.join()
    stderr = stderr.getvalue().strip()
    self.assertIn(f'Exception in thread {thread.name}:\n', stderr)
    self.assertIn('Traceback (most recent call last):\n', stderr)
    self.assertIn('  raise ValueError("run failed")', stderr)
    self.assertIn('ValueError: run failed', stderr)
