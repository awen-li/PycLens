# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pulldom.py
# case: PullDOMTestCase_test_external_ges_default

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = pulldom.parseString(SMALL_SAMPLE)
    saxparser = parser.parser
    ges = saxparser.getFeature(feature_external_ges)
    self.assertEqual(ges, False)
