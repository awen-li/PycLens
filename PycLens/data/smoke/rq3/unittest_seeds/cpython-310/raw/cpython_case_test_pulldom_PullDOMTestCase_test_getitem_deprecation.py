# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pulldom.py
# case: PullDOMTestCase_test_getitem_deprecation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = pulldom.parseString(SMALL_SAMPLE)
    with self.assertWarnsRegex(DeprecationWarning, 'Use iterator protocol instead'):
        self.assertEqual(parser[-1][0], pulldom.START_DOCUMENT)
