# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_interpreters.py
# case: CreateTests_test_after_destroy_all

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    before = set(interpreters.list_all())
    interp_lst = []
    for _ in range(3):
        interps = interpreters.create()
        interp_lst.append(interps)
    for interp in interp_lst:
        interp.close()
    interp = interpreters.create()
    self.assertEqual(set(interpreters.list_all()), before | {interp})
