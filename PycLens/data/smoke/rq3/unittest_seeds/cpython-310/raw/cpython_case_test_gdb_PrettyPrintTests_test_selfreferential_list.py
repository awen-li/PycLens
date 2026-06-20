# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gdb.py
# case: PrettyPrintTests_test_selfreferential_list

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (gdb_repr, gdb_output) = self.get_gdb_repr('a = [3, 4, 5] ; a.append(a) ; id(a)')
    self.assertEqual(gdb_repr, '[3, 4, 5, [...]]')
    (gdb_repr, gdb_output) = self.get_gdb_repr('a = [3, 4, 5] ; b = [a] ; a.append(b) ; id(a)')
    self.assertEqual(gdb_repr, '[3, 4, 5, [[...]]]')
