# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_interpreters.py
# case: ListAllTests_test_after_creating

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    main = interpreters.get_current()
    first = interpreters.create()
    second = interpreters.create()
    ids = []
    for interp in interpreters.list_all():
        ids.append(interp.id)
    self.assertEqual(ids, [main.id, first.id, second.id])
