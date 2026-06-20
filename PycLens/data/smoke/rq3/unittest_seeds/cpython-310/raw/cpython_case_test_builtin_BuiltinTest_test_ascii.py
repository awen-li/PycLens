# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: BuiltinTest_test_ascii

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(ascii(''), "''")
    self.assertEqual(ascii(0), '0')
    self.assertEqual(ascii(()), '()')
    self.assertEqual(ascii([]), '[]')
    self.assertEqual(ascii({}), '{}')
    a = []
    a.append(a)
    self.assertEqual(ascii(a), '[[...]]')
    a = {}
    a[0] = a
    self.assertEqual(ascii(a), '{0: {...}}')

    def _check_uni(s):
        self.assertEqual(ascii(s), repr(s))
    _check_uni("'")
    _check_uni('"')
    _check_uni('"\'')
    _check_uni('\x00')
    _check_uni('\r\n\t .')
    _check_uni('\x85')
    _check_uni('\u1fff')
    _check_uni('\U00012fff')
    _check_uni('\ud800')
    _check_uni('\udfff')
    self.assertEqual(ascii('𝄡'), "'\\U0001d121'")
    s = '\'\x00"\n\r\t abcd\x85é\U00012fff\ud800𝄡xxx.'
    self.assertEqual(ascii(s), '\'\\\'\\x00"\\n\\r\\t abcd\\x85\\xe9\\U00012fff\\ud800\\U0001d121xxx.\'')
