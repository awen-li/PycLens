# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: InterpreterIDTests_test_coerce_id

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Int(str):

        def __index__(self):
            return 10
    id = interpreters.InterpreterID(Int(), force=True)
    self.assertEqual(int(id), 10)
