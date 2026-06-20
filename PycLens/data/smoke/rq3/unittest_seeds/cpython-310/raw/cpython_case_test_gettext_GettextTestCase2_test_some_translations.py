# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gettext.py
# case: GettextTestCase2_test_some_translations

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eq = self.assertEqual
    eq(self._('albatross'), 'albatross')
    eq(self._('mullusk'), 'bacon')
    eq(self._('Raymond Luxury Yach-t'), 'Throatwobbler Mangrove')
    eq(self._('nudge nudge'), 'wink wink')
