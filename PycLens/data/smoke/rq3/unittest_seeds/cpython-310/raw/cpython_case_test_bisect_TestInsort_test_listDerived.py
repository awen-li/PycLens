# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bisect.py
# case: TestInsort_test_listDerived

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class List(list):
        data = []

        def insert(self, index, item):
            self.data.insert(index, item)
    lst = List()
    self.module.insort_left(lst, 10)
    self.module.insort_right(lst, 5)
    self.assertEqual([5, 10], lst.data)
