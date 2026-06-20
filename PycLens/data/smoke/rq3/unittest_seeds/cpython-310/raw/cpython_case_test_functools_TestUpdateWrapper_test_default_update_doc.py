# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestUpdateWrapper_test_default_update_doc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (wrapper, f) = self._default_update()
    self.assertEqual(wrapper.__doc__, 'This is a test')
