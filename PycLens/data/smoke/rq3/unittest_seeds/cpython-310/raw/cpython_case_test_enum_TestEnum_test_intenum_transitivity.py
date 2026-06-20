# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_intenum_transitivity

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class number(IntEnum):
        one = 1
        two = 2
        three = 3

    class numero(IntEnum):
        uno = 1
        dos = 2
        tres = 3
    self.assertEqual(number.one, numero.uno)
    self.assertEqual(number.two, numero.dos)
    self.assertEqual(number.three, numero.tres)
