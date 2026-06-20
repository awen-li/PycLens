# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pprint.py
# case: QueryTestCase_test_unreadable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pp = pprint.PrettyPrinter()
    for unreadable in (type(3), pprint, pprint.isrecursive):
        self.assertFalse(pprint.isrecursive(unreadable), 'expected not isrecursive for %r' % (unreadable,))
        self.assertFalse(pprint.isreadable(unreadable), 'expected not isreadable for %r' % (unreadable,))
        self.assertFalse(pp.isrecursive(unreadable), 'expected not isrecursive for %r' % (unreadable,))
        self.assertFalse(pp.isreadable(unreadable), 'expected not isreadable for %r' % (unreadable,))
