# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gdb.py
# case: PrettyPrintTests_test_subclassing_list

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (gdb_repr, gdb_output) = self.get_gdb_repr('\nclass Foo(list):\n    pass\nfoo = Foo()\nfoo += [1, 2, 3]\nfoo.an_int = 42\nid(foo)')
    m = re.match('<Foo\\(an_int=42\\) at remote 0x-?[0-9a-f]+>', gdb_repr)
    self.assertTrue(m, msg='Unexpected new-style class rendering %r' % gdb_repr)
