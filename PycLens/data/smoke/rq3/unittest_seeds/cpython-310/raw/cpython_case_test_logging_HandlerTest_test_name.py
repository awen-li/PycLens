# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: HandlerTest_test_name

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    h = logging.Handler()
    h.name = 'generic'
    self.assertEqual(h.name, 'generic')
    h.name = 'anothergeneric'
    self.assertEqual(h.name, 'anothergeneric')
    self.assertRaises(NotImplementedError, h.emit, None)
