# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_interpreters.py
# case: TestInterpreterClose_test_all

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    before = set(interpreters.list_all())
    interps = set()
    for _ in range(3):
        interp = interpreters.create()
        interps.add(interp)
    self.assertEqual(set(interpreters.list_all()), before | interps)
    for interp in interps:
        interp.close()
    self.assertEqual(set(interpreters.list_all()), before)
