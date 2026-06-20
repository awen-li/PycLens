# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test___future__.py
# case: FutureTest_test_names

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    given_feature_names = features[:]
    for name in dir(__future__):
        obj = getattr(__future__, name, None)
        if obj is not None and isinstance(obj, __future__._Feature):
            self.assertTrue(name in given_feature_names, '%r should have been in all_feature_names' % name)
            given_feature_names.remove(name)
    self.assertEqual(len(given_feature_names), 0, 'all_feature_names has too much: %r' % given_feature_names)
