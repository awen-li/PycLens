# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: InterpreterIDTests_test_does_not_exist

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    id = interpreters.channel_create()
    with self.assertRaises(RuntimeError):
        interpreters.InterpreterID(int(id) + 1)
