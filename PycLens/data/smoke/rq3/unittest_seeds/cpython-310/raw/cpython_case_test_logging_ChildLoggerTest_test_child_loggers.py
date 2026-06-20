# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: ChildLoggerTest_test_child_loggers

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    r = logging.getLogger()
    l1 = logging.getLogger('abc')
    l2 = logging.getLogger('def.ghi')
    c1 = r.getChild('xyz')
    c2 = r.getChild('uvw.xyz')
    self.assertIs(c1, logging.getLogger('xyz'))
    self.assertIs(c2, logging.getLogger('uvw.xyz'))
    c1 = l1.getChild('def')
    c2 = c1.getChild('ghi')
    c3 = l1.getChild('def.ghi')
    self.assertIs(c1, logging.getLogger('abc.def'))
    self.assertIs(c2, logging.getLogger('abc.def.ghi'))
    self.assertIs(c2, c3)
