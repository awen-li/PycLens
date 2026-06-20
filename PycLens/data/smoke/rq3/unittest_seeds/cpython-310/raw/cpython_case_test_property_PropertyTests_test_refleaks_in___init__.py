# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_property.py
# case: PropertyTests_test_refleaks_in___init__

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    gettotalrefcount = support.get_attribute(sys, 'gettotalrefcount')
    fake_prop = property('fget', 'fset', 'fdel', 'doc')
    refs_before = gettotalrefcount()
    for i in range(100):
        fake_prop.__init__('fget', 'fset', 'fdel', 'doc')
    self.assertAlmostEqual(gettotalrefcount() - refs_before, 0, delta=10)
