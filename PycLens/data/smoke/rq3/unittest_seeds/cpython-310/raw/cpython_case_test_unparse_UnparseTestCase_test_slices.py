# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unparse.py
# case: UnparseTestCase_test_slices

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_ast_roundtrip('a[i]')
    self.check_ast_roundtrip('a[i,]')
    self.check_ast_roundtrip('a[i, j]')
    self.check_ast_roundtrip('a[(*a,)]')
    self.check_ast_roundtrip('a[(a:=b)]')
    self.check_ast_roundtrip('a[(a:=b,c)]')
    self.check_ast_roundtrip('a[()]')
    self.check_ast_roundtrip('a[i:j]')
    self.check_ast_roundtrip('a[:j]')
    self.check_ast_roundtrip('a[i:]')
    self.check_ast_roundtrip('a[i:j:k]')
    self.check_ast_roundtrip('a[:j:k]')
    self.check_ast_roundtrip('a[i::k]')
    self.check_ast_roundtrip('a[i:j,]')
    self.check_ast_roundtrip('a[i:j, k]')
