# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: DestroyTests_test_one

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    id1 = interpreters.create()
    id2 = interpreters.create()
    id3 = interpreters.create()
    self.assertIn(id2, interpreters.list_all())
    interpreters.destroy(id2)
    self.assertNotIn(id2, interpreters.list_all())
    self.assertIn(id1, interpreters.list_all())
    self.assertIn(id3, interpreters.list_all())
