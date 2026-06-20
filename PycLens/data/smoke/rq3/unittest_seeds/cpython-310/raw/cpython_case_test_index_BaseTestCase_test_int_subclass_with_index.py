# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_index.py
# case: BaseTestCase_test_int_subclass_with_index

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyInt(int):

        def __index__(self):
            return int(str(self)) + 1
    my_int = MyInt(7)
    direct_index = my_int.__index__()
    operator_index = operator.index(my_int)
    self.assertEqual(direct_index, 8)
    self.assertEqual(operator_index, 7)
    self.assertIs(type(direct_index), int)
