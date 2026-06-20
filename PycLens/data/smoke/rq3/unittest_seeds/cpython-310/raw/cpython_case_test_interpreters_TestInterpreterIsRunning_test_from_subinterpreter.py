# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_interpreters.py
# case: TestInterpreterIsRunning_test_from_subinterpreter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    interp = interpreters.create()
    out = _run_output(interp, dedent(f'\n            import _xxsubinterpreters as _interpreters\n            if _interpreters.is_running({interp.id}):\n                print(True)\n            else:\n                print(False)\n            '))
    self.assertEqual(out.strip(), 'True')
