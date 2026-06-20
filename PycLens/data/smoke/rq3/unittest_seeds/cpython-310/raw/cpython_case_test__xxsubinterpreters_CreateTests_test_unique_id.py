# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: CreateTests_test_unique_id

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    seen = set()
    for _ in range(100):
        id = interpreters.create()
        interpreters.destroy(id)
        seen.add(id)
    self.assertEqual(len(seen), 100)
