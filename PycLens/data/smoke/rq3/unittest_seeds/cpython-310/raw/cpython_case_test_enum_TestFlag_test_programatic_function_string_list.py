# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestFlag_test_programatic_function_string_list

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Perm = Flag('Perm', ['R', 'W', 'X'])
    lst = list(Perm)
    self.assertEqual(len(lst), len(Perm))
    self.assertEqual(len(Perm), 3, Perm)
    self.assertEqual(lst, [Perm.R, Perm.W, Perm.X])
    for (i, n) in enumerate('R W X'.split()):
        v = 1 << i
        e = Perm(v)
        self.assertEqual(e.value, v)
        self.assertEqual(type(e.value), int)
        self.assertEqual(e.name, n)
        self.assertIn(e, Perm)
        self.assertIs(type(e), Perm)
