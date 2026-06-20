# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: CreateTests_test_after_destroy_all

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    before = set(interpreters.list_all())
    ids = []
    for _ in range(3):
        id = interpreters.create()
        ids.append(id)
    for id in ids:
        interpreters.destroy(id)
    id = interpreters.create()
    self.assertEqual(set(interpreters.list_all()), before | {id})
