# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: RunStringTests_test_does_not_exist

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    id = 0
    while id in interpreters.list_all():
        id += 1
    with self.assertRaises(RuntimeError):
        interpreters.run_string(id, 'print("spam")')
