# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict_version.py
# case: DictVersionTests_test_setitem

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = self.new_dict()
    self.check_version_changed(d, d.__setitem__, 'x', 'x')
    self.check_version_changed(d, d.__setitem__, 'y', 'y')
    self.check_version_changed(d, d.__setitem__, 'x', 1)
    self.check_version_changed(d, d.__setitem__, 'y', 2)
