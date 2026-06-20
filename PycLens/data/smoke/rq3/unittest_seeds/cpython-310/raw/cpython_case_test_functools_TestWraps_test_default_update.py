# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestWraps_test_default_update

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (wrapper, f) = self._default_update()
    self.check_wrapper(wrapper, f)
    self.assertEqual(wrapper.__name__, 'f')
    self.assertEqual(wrapper.__qualname__, f.__qualname__)
    self.assertEqual(wrapper.attr, 'This is also a test')
