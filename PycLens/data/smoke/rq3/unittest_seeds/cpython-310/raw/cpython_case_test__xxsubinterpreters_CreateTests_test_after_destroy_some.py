# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: CreateTests_test_after_destroy_some

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    before = set(interpreters.list_all())
    id1 = interpreters.create()
    id2 = interpreters.create()
    id3 = interpreters.create()
    interpreters.destroy(id1)
    interpreters.destroy(id3)
    id = interpreters.create()
    self.assertEqual(set(interpreters.list_all()), before | {id, id2})
