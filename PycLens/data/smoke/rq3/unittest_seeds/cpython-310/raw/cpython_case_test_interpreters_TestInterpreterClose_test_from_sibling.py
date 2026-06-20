# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_interpreters.py
# case: TestInterpreterClose_test_from_sibling

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (main,) = interpreters.list_all()
    interp1 = interpreters.create()
    interp2 = interpreters.create()
    self.assertEqual(set(interpreters.list_all()), {main, interp1, interp2})
    interp1.run(dedent(f'\n            from test.support import interpreters\n            interp2 = interpreters.Interpreter(int({interp2.id}))\n            interp2.close()\n            interp3 = interpreters.create()\n            interp3.close()\n            '))
    self.assertEqual(set(interpreters.list_all()), {main, interp1})
