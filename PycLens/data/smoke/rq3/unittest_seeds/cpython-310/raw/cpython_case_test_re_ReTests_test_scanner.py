# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_scanner

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def s_ident(scanner, token):
        return token

    def s_operator(scanner, token):
        return 'op%s' % token

    def s_float(scanner, token):
        return float(token)

    def s_int(scanner, token):
        return int(token)
    scanner = Scanner([('[a-zA-Z_]\\w*', s_ident), ('\\d+\\.\\d*', s_float), ('\\d+', s_int), ('=|\\+|-|\\*|/', s_operator), ('\\s+', None)])
    self.assertTrue(scanner.scanner.scanner('').pattern)
    self.assertEqual(scanner.scan('sum = 3*foo + 312.50 + bar'), (['sum', 'op=', 3, 'op*', 'foo', 'op+', 312.5, 'op+', 'bar'], ''))
