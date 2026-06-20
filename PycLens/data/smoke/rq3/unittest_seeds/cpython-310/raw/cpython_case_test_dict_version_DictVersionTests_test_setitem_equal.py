# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict_version.py
# case: DictVersionTests_test_setitem_equal

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class AlwaysEqual:

        def __eq__(self, other):
            return True
    value1 = AlwaysEqual()
    value2 = AlwaysEqual()
    self.assertTrue(value1 == value2)
    self.assertFalse(value1 != value2)
    self.assertIsNot(value1, value2)
    d = self.new_dict()
    self.check_version_changed(d, d.__setitem__, 'key', value1)
    self.assertIs(d['key'], value1)
    self.check_version_changed(d, d.__setitem__, 'key', value2)
    self.assertIs(d['key'], value2)
    self.check_version_changed(d, d.update, key=value1)
    self.assertIs(d['key'], value1)
    d2 = self.new_dict(key=value2)
    self.check_version_changed(d, d.update, d2)
    self.assertIs(d['key'], value2)
