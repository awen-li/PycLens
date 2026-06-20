# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_symtable.py
# case: SymtableTest_test_bytes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    top = symtable.symtable(TEST_CODE.encode('utf8'), '?', 'exec')
    self.assertIsNotNone(find_block(top, 'Mine'))
    code = b'# -*- coding: iso8859-15 -*-\nclass \xb4: pass\n'
    top = symtable.symtable(code, '?', 'exec')
    self.assertIsNotNone(find_block(top, 'Ž'))
