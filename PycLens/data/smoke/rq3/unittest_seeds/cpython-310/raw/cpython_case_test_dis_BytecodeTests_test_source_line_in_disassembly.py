# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dis.py
# case: BytecodeTests_test_source_line_in_disassembly

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    actual = dis.Bytecode(simple).dis()
    actual = actual.strip().partition(' ')[0]
    expected = str(simple.__code__.co_firstlineno)
    self.assertEqual(actual, expected)
    actual = dis.Bytecode(simple, first_line=350).dis()
    actual = actual.strip().partition(' ')[0]
    self.assertEqual(actual, '350')
