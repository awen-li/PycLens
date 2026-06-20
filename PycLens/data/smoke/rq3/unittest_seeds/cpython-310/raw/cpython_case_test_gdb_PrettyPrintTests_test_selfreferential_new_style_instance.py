# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gdb.py
# case: PrettyPrintTests_test_selfreferential_new_style_instance

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (gdb_repr, gdb_output) = self.get_gdb_repr('\nclass Foo(object):\n    pass\nfoo = Foo()\nfoo.an_attr = foo\nid(foo)')
    self.assertTrue(re.match('<Foo\\(an_attr=<\\.\\.\\.>\\) at remote 0x-?[0-9a-f]+>', gdb_repr), 'Unexpected gdb representation: %r\n%s' % (gdb_repr, gdb_output))
    (gdb_repr, gdb_output) = self.get_gdb_repr('\nclass Foo(object):\n    pass\na = Foo()\nb = Foo()\na.an_attr = b\nb.an_attr = a\nid(a)')
    self.assertTrue(re.match('<Foo\\(an_attr=<Foo\\(an_attr=<\\.\\.\\.>\\) at remote 0x-?[0-9a-f]+>\\) at remote 0x-?[0-9a-f]+>', gdb_repr), 'Unexpected gdb representation: %r\n%s' % (gdb_repr, gdb_output))
