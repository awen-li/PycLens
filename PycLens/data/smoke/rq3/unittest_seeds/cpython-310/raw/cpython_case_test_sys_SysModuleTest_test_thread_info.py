# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys.py
# case: SysModuleTest_test_thread_info

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    info = sys.thread_info
    self.assertEqual(len(info), 3)
    self.assertIn(info.name, ('nt', 'pthread', 'solaris', None))
    self.assertIn(info.lock, ('semaphore', 'mutex+cond', None))
