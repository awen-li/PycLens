# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gdb.py
# case: PrettyPrintTests_test_sets

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if (gdb_major_version, gdb_minor_version) < (7, 3):
        self.skipTest('pretty-printing of sets needs gdb 7.3 or later')
    self.assertGdbRepr(set(), 'set()')
    self.assertGdbRepr(set(['a']), "{'a'}")
    if not sys.flags.ignore_environment:
        self.assertGdbRepr(set(['a', 'b']), "{'a', 'b'}")
        self.assertGdbRepr(set([4, 5, 6]), '{4, 5, 6}')
    (gdb_repr, gdb_output) = self.get_gdb_repr("s = set(['a','b'])\ns.remove('a')\nid(s)")
    self.assertEqual(gdb_repr, "{'b'}")
