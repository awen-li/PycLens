# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: CreateTests_test_in_main

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    id = interpreters.create()
    self.assertIsInstance(id, interpreters.InterpreterID)
    self.assertIn(id, interpreters.list_all())
