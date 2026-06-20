# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gdb.py
# case: PrettyPrintTests_test_frozensets

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if (gdb_major_version, gdb_minor_version) < (7, 3):
        self.skipTest('pretty-printing of frozensets needs gdb 7.3 or later')
    self.assertGdbRepr(frozenset(), 'frozenset()')
    self.assertGdbRepr(frozenset(['a']), "frozenset({'a'})")
    if not sys.flags.ignore_environment:
        self.assertGdbRepr(frozenset(['a', 'b']), "frozenset({'a', 'b'})")
        self.assertGdbRepr(frozenset([4, 5, 6]), 'frozenset({4, 5, 6})')
