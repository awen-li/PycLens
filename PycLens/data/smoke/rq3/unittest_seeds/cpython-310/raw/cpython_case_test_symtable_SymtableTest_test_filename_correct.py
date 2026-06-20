# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_symtable.py
# case: SymtableTest_test_filename_correct

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def checkfilename(brokencode, offset):
        try:
            symtable.symtable(brokencode, 'spam', 'exec')
        except SyntaxError as e:
            self.assertEqual(e.filename, 'spam')
            self.assertEqual(e.lineno, 1)
            self.assertEqual(e.offset, offset)
        else:
            self.fail('no SyntaxError for %r' % (brokencode,))
    checkfilename('def f(x): foo)(', 14)
    checkfilename('def f(x): global x', 11)
    symtable.symtable('pass', b'spam', 'exec')
    with self.assertWarns(DeprecationWarning), self.assertRaises(TypeError):
        symtable.symtable('pass', bytearray(b'spam'), 'exec')
    with self.assertWarns(DeprecationWarning):
        symtable.symtable('pass', memoryview(b'spam'), 'exec')
    with self.assertRaises(TypeError):
        symtable.symtable('pass', list(b'spam'), 'exec')
