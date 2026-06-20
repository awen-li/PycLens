# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_support.py
# case: TestSupport_test_unload

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import sched
    self.assertIn('sched', sys.modules)
    import_helper.unload('sched')
    self.assertNotIn('sched', sys.modules)
