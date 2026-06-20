# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gdb.py
# case: PrettyPrintTests_test_builtins_help

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if sys.flags.no_site:
        self.skipTest('need site module, but -S option was used')
    (gdb_repr, gdb_output) = self.get_gdb_repr('id(__builtins__.help)', import_site=True)
    m = re.match('<_Helper at remote 0x-?[0-9a-f]+>', gdb_repr)
    self.assertTrue(m, msg='Unexpected rendering %r' % gdb_repr)
