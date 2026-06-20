# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_interpreters.py
# case: CreateTests_test_in_subinterpreter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (main,) = interpreters.list_all()
    interp = interpreters.create()
    out = _run_output(interp, dedent('\n            from test.support import interpreters\n            interp = interpreters.create()\n            print(interp.id)\n            '))
    interp2 = interpreters.Interpreter(int(out))
    self.assertEqual(interpreters.list_all(), [main, interp, interp2])
