# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_interpreters.py
# case: CreateTests_test_after_destroy_some

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    before = set(interpreters.list_all())
    interp1 = interpreters.create()
    interp2 = interpreters.create()
    interp3 = interpreters.create()
    interp1.close()
    interp2.close()
    interp = interpreters.create()
    self.assertEqual(set(interpreters.list_all()), before | {interp3, interp})
