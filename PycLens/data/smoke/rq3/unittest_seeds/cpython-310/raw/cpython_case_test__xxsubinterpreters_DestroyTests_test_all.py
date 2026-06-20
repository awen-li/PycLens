# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: DestroyTests_test_all

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    before = set(interpreters.list_all())
    ids = set()
    for _ in range(3):
        id = interpreters.create()
        ids.add(id)
    self.assertEqual(set(interpreters.list_all()), before | ids)
    for id in ids:
        interpreters.destroy(id)
    self.assertEqual(set(interpreters.list_all()), before)
