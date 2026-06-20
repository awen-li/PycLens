# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tokenize.py
# case: Test_Tokenize_test__tokenize_decodes_with_specified_encoding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    literal = '"ЉЊЈЁЂ"'
    line = literal.encode('utf-8')
    first = False

    def readline():
        nonlocal first
        if not first:
            first = True
            return line
        else:
            return b''
    tokens = list(_tokenize(readline, encoding='utf-8'))[1:-2]
    expected_tokens = [(3, '"ЉЊЈЁЂ"', (1, 0), (1, 7), '"ЉЊЈЁЂ"')]
    self.assertEqual(tokens, expected_tokens, 'bytes not decoded with encoding')
