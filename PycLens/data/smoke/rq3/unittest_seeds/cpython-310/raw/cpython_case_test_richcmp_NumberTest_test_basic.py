# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_richcmp.py
# case: NumberTest_test_basic

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for a in range(3):
        for b in range(3):
            for typea in (int, Number):
                for typeb in (int, Number):
                    if typea == typeb == int:
                        continue
                    ta = typea(a)
                    tb = typeb(b)
                    for ops in opmap.values():
                        for op in ops:
                            realoutcome = op(a, b)
                            testoutcome = op(ta, tb)
                            self.assertEqual(realoutcome, testoutcome)
