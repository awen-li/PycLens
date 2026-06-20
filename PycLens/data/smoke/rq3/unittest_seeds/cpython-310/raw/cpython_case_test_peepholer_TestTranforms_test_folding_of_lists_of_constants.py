# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_peepholer.py
# case: TestTranforms_test_folding_of_lists_of_constants

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (line, elem) in (('a in [1,2,3]', (1, 2, 3)), ('a not in ["a","b","c"]', ('a', 'b', 'c')), ('a in [None, 1, None]', (None, 1, None)), ('a not in [(1, 2), 3, 4]', ((1, 2), 3, 4))):
        code = compile(line, '', 'single')
        self.assertInBytecode(code, 'LOAD_CONST', elem)
        self.assertNotInBytecode(code, 'BUILD_LIST')
        self.check_lnotab(code)
