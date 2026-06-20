# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: GetMainTests_test_from_subinterpreter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    [expected] = interpreters.list_all()
    interp = interpreters.create()
    out = _run_output(interp, dedent('\n            import _xxsubinterpreters as _interpreters\n            main = _interpreters.get_main()\n            print(main)\n            assert isinstance(main, _interpreters.InterpreterID)\n            '))
    main = int(out.strip())
    self.assertEqual(main, expected)
