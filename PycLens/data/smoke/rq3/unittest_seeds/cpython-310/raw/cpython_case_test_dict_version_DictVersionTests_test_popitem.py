# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict_version.py
# case: DictVersionTests_test_popitem

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = self.new_dict(key='value')
    self.check_version_changed(d, d.popitem)
    self.check_version_dont_change(d, self.assertRaises, KeyError, d.popitem)
