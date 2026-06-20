# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePathTest_test_mkdir_exist_ok_root

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.cls('/').resolve().mkdir(exist_ok=True)
    self.cls('/').resolve().mkdir(parents=True, exist_ok=True)
