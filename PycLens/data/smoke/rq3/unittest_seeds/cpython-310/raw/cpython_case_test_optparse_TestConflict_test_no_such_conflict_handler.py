# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestConflict_test_no_such_conflict_handler

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(self.parser.set_conflict_handler, ('foo',), None, ValueError, "invalid conflict_resolution value 'foo'")
