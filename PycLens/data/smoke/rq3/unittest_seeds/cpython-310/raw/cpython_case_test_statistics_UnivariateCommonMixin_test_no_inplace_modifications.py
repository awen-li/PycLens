# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: UnivariateCommonMixin_test_no_inplace_modifications

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = self.prepare_data()
    assert len(data) != 1
    assert data != sorted(data)
    saved = data[:]
    assert data is not saved
    _ = self.func(data)
    self.assertListEqual(data, saved, 'data has been modified')
