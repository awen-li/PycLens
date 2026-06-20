# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: DestroyTests_test_from_sibling

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (main,) = interpreters.list_all()
    id1 = interpreters.create()
    id2 = interpreters.create()
    script = dedent(f'\n            import _xxsubinterpreters as _interpreters\n            _interpreters.destroy({id2})\n            ')
    interpreters.run_string(id1, script)
    self.assertEqual(set(interpreters.list_all()), {main, id1})
