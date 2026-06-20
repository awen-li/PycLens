# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePathTest_test_with

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = self.cls(BASE)
    it = p.iterdir()
    it2 = p.iterdir()
    next(it2)
    with p:
        pass
    next(it)
    next(it2)
    p.exists()
    p.resolve()
    p.absolute()
    with p:
        pass
