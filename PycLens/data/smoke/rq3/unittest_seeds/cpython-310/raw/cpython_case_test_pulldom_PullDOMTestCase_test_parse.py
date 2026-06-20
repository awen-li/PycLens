# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pulldom.py
# case: PullDOMTestCase_test_parse

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    handler = pulldom.parse(tstfile)
    self.addCleanup(handler.stream.close)
    list(handler)
    with open(tstfile, 'rb') as fin:
        list(pulldom.parse(fin))
