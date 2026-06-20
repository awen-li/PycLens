# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_list.py
# case: ListTest_test_count_index_remove_crashes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class X:

        def __eq__(self, other):
            lst.clear()
            return NotImplemented
    lst = [X()]
    with self.assertRaises(ValueError):
        lst.index(lst)

    class L(list):

        def __eq__(self, other):
            str(other)
            return NotImplemented
    lst = L([X()])
    lst.count(lst)
    lst = L([X()])
    with self.assertRaises(ValueError):
        lst.remove(lst)
    lst = [X(), X()]
    3 in lst
    lst = [X(), X()]
    X() in lst
