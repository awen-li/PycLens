# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exception_hierarchy.py
# case: ExplicitSubclassingTest_test_new_overridden

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    e = SubOSErrorWithNew('some message', 'baz')
    self.assertEqual(e.baz, 'baz')
    self.assertEqual(e.args, ('some message',))
