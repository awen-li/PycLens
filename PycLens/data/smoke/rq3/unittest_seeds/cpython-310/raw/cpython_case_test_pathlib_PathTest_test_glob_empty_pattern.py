# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: PathTest_test_glob_empty_pattern

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = self.cls()
    with self.assertRaisesRegex(ValueError, 'Unacceptable pattern'):
        list(p.glob(''))
