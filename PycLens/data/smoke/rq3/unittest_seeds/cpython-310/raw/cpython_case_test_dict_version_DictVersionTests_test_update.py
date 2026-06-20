# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict_version.py
# case: DictVersionTests_test_update

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = self.new_dict(key='value')
    self.check_version_dont_change(d, d.update)
    self.check_version_changed(d, d.update, key='new value')
    d2 = self.new_dict(key='value 3')
    self.check_version_changed(d, d.update, d2)
