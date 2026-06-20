# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_iter.py
# case: TestCase_test_extending_list_with_iterator_does_not_segfault

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def gen():
        for i in range(500):
            yield i
    lst = [0] * 500
    for i in range(240):
        lst.pop(0)
    lst.extend(gen())
    self.assertEqual(len(lst), 760)
