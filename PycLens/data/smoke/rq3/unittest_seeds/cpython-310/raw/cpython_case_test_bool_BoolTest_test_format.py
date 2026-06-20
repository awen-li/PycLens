# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bool.py
# case: BoolTest_test_format

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual('%d' % False, '0')
    self.assertEqual('%d' % True, '1')
    self.assertEqual('%x' % False, '0')
    self.assertEqual('%x' % True, '1')
