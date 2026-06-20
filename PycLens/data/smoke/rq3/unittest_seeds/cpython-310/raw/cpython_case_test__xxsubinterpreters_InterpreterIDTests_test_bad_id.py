# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: InterpreterIDTests_test_bad_id

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, interpreters.InterpreterID, object())
    self.assertRaises(TypeError, interpreters.InterpreterID, 10.0)
    self.assertRaises(TypeError, interpreters.InterpreterID, '10')
    self.assertRaises(TypeError, interpreters.InterpreterID, b'10')
    self.assertRaises(ValueError, interpreters.InterpreterID, -1)
    self.assertRaises(OverflowError, interpreters.InterpreterID, 2 ** 64)
