# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gdb.py
# case: PrettyPrintTests_test_builtin_method

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (gdb_repr, gdb_output) = self.get_gdb_repr('import sys; id(sys.stdout.readlines)')
    self.assertTrue(re.match('<built-in method readlines of _io.TextIOWrapper object at remote 0x-?[0-9a-f]+>', gdb_repr), 'Unexpected gdb representation: %r\n%s' % (gdb_repr, gdb_output))
