# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: DestroyTests_test_from_current

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (main,) = interpreters.list_all()
    id = interpreters.create()
    script = dedent(f'\n            import _xxsubinterpreters as _interpreters\n            try:\n                _interpreters.destroy({id})\n            except RuntimeError:\n                pass\n            ')
    interpreters.run_string(id, script)
    self.assertEqual(set(interpreters.list_all()), {main, id})
