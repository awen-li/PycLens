# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pyexpat.py
# case: NamespaceSeparatorTest_test_legal

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expat.ParserCreate()
    expat.ParserCreate(namespace_separator=None)
    expat.ParserCreate(namespace_separator=' ')
