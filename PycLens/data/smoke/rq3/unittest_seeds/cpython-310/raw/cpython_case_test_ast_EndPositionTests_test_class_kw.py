# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: EndPositionTests_test_class_kw

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = 'class S(metaclass=abc.ABCMeta): pass'
    cdef = ast.parse(s).body[0]
    self._check_content(s, cdef.keywords[0].value, 'abc.ABCMeta')
