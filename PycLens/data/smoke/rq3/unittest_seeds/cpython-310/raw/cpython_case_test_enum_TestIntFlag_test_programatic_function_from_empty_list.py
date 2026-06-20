# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestIntFlag_test_programatic_function_from_empty_list

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Perm = enum.IntFlag('Perm', [])
    lst = list(Perm)
    self.assertEqual(len(lst), len(Perm))
    self.assertEqual(len(Perm), 0, Perm)
    Thing = enum.Enum('Thing', [])
    lst = list(Thing)
    self.assertEqual(len(lst), len(Thing))
    self.assertEqual(len(Thing), 0, Thing)
