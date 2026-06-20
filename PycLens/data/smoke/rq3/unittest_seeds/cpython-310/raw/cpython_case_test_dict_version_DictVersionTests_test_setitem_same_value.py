# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict_version.py
# case: DictVersionTests_test_setitem_same_value

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    value = object()
    d = self.new_dict()
    self.check_version_changed(d, d.__setitem__, 'key', value)
    self.check_version_dont_change(d, d.__setitem__, 'key', value)
    self.check_version_dont_change(d, d.update, key=value)
    d2 = self.new_dict(key=value)
    self.check_version_dont_change(d, d.update, d2)
