# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: OperatorsTest_test_ints

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.number_operators(100, 3)
    self.assertEqual(1 .__bool__(), 1)
    self.assertEqual(0 .__bool__(), 0)

    class C(int):

        def __add__(self, other):
            return NotImplemented
    self.assertEqual(C(5), 5)
    try:
        C() + ''
    except TypeError:
        pass
    else:
        self.fail('NotImplemented should have caused TypeError')
