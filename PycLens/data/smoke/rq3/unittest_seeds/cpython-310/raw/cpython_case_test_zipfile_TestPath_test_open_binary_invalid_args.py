# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: TestPath_test_open_binary_invalid_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    root = zipfile.Path(alpharep)
    with self.assertRaises(ValueError):
        root.joinpath('a.txt').open('rb', encoding='utf-8')
    with self.assertRaises(ValueError):
        root.joinpath('a.txt').open('rb', 'utf-8')
