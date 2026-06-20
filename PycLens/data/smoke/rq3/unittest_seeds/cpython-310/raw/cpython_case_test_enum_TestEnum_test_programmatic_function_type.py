# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_programmatic_function_type

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    SummerMonth = Enum('SummerMonth', 'june july august', type=int)
    lst = list(SummerMonth)
    self.assertEqual(len(lst), len(SummerMonth))
    self.assertEqual(len(SummerMonth), 3, SummerMonth)
    self.assertEqual([SummerMonth.june, SummerMonth.july, SummerMonth.august], lst)
    for (i, month) in enumerate('june july august'.split(), 1):
        e = SummerMonth(i)
        self.assertEqual(e, i)
        self.assertEqual(e.name, month)
        self.assertIn(e, SummerMonth)
        self.assertIs(type(e), SummerMonth)
