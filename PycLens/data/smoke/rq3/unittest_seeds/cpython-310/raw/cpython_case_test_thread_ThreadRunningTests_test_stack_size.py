# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_thread.py
# case: ThreadRunningTests_test_stack_size

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(thread.stack_size(), 0, 'initial stack size is not 0')
    thread.stack_size(0)
    self.assertEqual(thread.stack_size(), 0, 'stack_size not reset to default')
