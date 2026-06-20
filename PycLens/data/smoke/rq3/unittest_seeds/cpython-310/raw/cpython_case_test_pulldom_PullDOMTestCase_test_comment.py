# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pulldom.py
# case: PullDOMTestCase_test_comment

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    items = pulldom.parseString(SMALL_SAMPLE)
    for (evt, _) in items:
        if evt == pulldom.COMMENT:
            break
    else:
        self.fail('No comment was encountered')
