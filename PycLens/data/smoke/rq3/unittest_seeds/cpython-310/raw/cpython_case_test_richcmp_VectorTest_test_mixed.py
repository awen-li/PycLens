# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_richcmp.py
# case: VectorTest_test_mixed

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = Vector(range(2))
    b = Vector(range(3))
    for opname in opmap:
        self.checkfail(ValueError, opname, a, b)
    a = list(range(5))
    b = 5 * [2]
    args = [(a, Vector(b)), (Vector(a), b), (Vector(a), Vector(b))]
    for (a, b) in args:
        self.checkequal('lt', a, b, [True, True, False, False, False])
        self.checkequal('le', a, b, [True, True, True, False, False])
        self.checkequal('eq', a, b, [False, False, True, False, False])
        self.checkequal('ne', a, b, [True, True, False, True, True])
        self.checkequal('gt', a, b, [False, False, False, True, True])
        self.checkequal('ge', a, b, [False, False, True, True, True])
        for ops in opmap.values():
            for op in ops:
                self.assertRaises(TypeError, bool, op(a, b))
