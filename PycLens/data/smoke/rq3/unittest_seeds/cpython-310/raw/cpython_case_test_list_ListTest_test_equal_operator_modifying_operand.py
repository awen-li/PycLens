# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_list.py
# case: ListTest_test_equal_operator_modifying_operand

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class X:

        def __eq__(self, other):
            list2.clear()
            return NotImplemented

    class Y:

        def __eq__(self, other):
            list1.clear()
            return NotImplemented

    class Z:

        def __eq__(self, other):
            list3.clear()
            return NotImplemented
    list1 = [X()]
    list2 = [Y()]
    self.assertTrue(list1 == list2)
    list3 = [Z()]
    list4 = [1]
    self.assertFalse(list3 == list4)
