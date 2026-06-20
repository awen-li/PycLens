# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_msilib.py
# case: Test_make_id_test_is_no_change_required

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(msilib.make_id('short'), 'short')
    self.assertEqual(msilib.make_id('nochangerequired'), 'nochangerequired')
    self.assertEqual(msilib.make_id('one.dot'), 'one.dot')
    self.assertEqual(msilib.make_id('_'), '_')
    self.assertEqual(msilib.make_id('a'), 'a')
