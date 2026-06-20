# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unparse.py
# case: CosmeticTestCase_test_class_bases_and_keywords

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_src_roundtrip('class X:\n    pass')
    self.check_src_roundtrip('class X(A):\n    pass')
    self.check_src_roundtrip('class X(A, B, C, D):\n    pass')
    self.check_src_roundtrip('class X(x=y):\n    pass')
    self.check_src_roundtrip('class X(metaclass=z):\n    pass')
    self.check_src_roundtrip('class X(x=y, z=d):\n    pass')
    self.check_src_roundtrip('class X(A, x=y):\n    pass')
    self.check_src_roundtrip('class X(A, **kw):\n    pass')
    self.check_src_roundtrip('class X(*args):\n    pass')
    self.check_src_roundtrip('class X(*args, **kwargs):\n    pass')
