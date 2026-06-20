# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_richcmp.py
# case: ListTest_test_badentry

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Exc(Exception):
        pass

    class Bad:

        def __eq__(self, other):
            raise Exc
    x = [Bad()]
    y = [Bad()]
    for op in opmap['eq']:
        self.assertRaises(Exc, op, x, y)
