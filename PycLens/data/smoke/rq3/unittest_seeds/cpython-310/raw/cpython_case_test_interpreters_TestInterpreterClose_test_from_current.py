# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_interpreters.py
# case: TestInterpreterClose_test_from_current

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (main,) = interpreters.list_all()
    interp = interpreters.create()
    out = _run_output(interp, dedent(f"\n            from test.support import interpreters\n            interp = interpreters.Interpreter({int(interp.id)})\n            try:\n                interp.close()\n            except RuntimeError:\n                print('failed')\n            "))
    self.assertEqual(out.strip(), 'failed')
    self.assertEqual(set(interpreters.list_all()), {main, interp})
