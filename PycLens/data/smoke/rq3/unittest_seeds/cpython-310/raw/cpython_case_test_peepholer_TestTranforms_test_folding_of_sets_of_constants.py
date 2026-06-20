# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_peepholer.py
# case: TestTranforms_test_folding_of_sets_of_constants

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (line, elem) in (('a in {1,2,3}', frozenset({1, 2, 3})), ('a not in {"a","b","c"}', frozenset({'a', 'c', 'b'})), ('a in {None, 1, None}', frozenset({1, None})), ('a not in {(1, 2), 3, 4}', frozenset({(1, 2), 3, 4})), ('a in {1, 2, 3, 3, 2, 1}', frozenset({1, 2, 3}))):
        code = compile(line, '', 'single')
        self.assertNotInBytecode(code, 'BUILD_SET')
        self.assertInBytecode(code, 'LOAD_CONST', elem)
        self.check_lnotab(code)

    def f(a):
        return a in {1, 2, 3}

    def g(a):
        return a not in {1, 2, 3}
    self.assertTrue(f(3))
    self.assertTrue(not f(4))
    self.check_lnotab(f)
    self.assertTrue(not g(3))
    self.assertTrue(g(4))
    self.check_lnotab(g)
