# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: ListAllTests_test_after_destroying

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    main = interpreters.get_main()
    first = interpreters.create()
    second = interpreters.create()
    interpreters.destroy(first)
    ids = interpreters.list_all()
    self.assertEqual(ids, [main, second])
