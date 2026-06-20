# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: GetCurrentTests_test_subinterpreter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    main = interpreters.get_main()
    interp = interpreters.create()
    out = _run_output(interp, dedent('\n            import _xxsubinterpreters as _interpreters\n            cur = _interpreters.get_current()\n            print(cur)\n            assert isinstance(cur, _interpreters.InterpreterID)\n            '))
    cur = int(out.strip())
    (_, expected) = interpreters.list_all()
    self.assertEqual(cur, expected)
    self.assertNotEqual(cur, main)
