# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_interpreters.py
# case: GetCurrentTests_test_subinterpreter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    main = _interpreters.get_main()
    interp = interpreters.create()
    out = _run_output(interp, dedent('\n            from test.support import interpreters\n            cur = interpreters.get_current()\n            print(cur.id)\n            '))
    current = interpreters.Interpreter(int(out))
    self.assertNotEqual(current, main)
