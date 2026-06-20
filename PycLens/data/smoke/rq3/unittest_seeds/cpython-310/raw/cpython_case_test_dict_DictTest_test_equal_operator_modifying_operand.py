# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict.py
# case: DictTest_test_equal_operator_modifying_operand

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class X:

        def __del__(self):
            dict_b.clear()

        def __eq__(self, other):
            dict_a.clear()
            return True

        def __hash__(self):
            return 13
    dict_a = {X(): 0}
    dict_b = {X(): X()}
    self.assertTrue(dict_a == dict_b)

    class Y:

        def __eq__(self, other):
            dict_d.clear()
            return True
    dict_c = {0: Y()}
    dict_d = {0: set()}
    self.assertTrue(dict_c == dict_d)
