# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_richcmp.py
# case: ListTest_test_goodentry

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Good:

        def __lt__(self, other):
            return True
    x = [Good()]
    y = [Good()]
    for op in opmap['lt']:
        self.assertIs(op(x, y), True)
