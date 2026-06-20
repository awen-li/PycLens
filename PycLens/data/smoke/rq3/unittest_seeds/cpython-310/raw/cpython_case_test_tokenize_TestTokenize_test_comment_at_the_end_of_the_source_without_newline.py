# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tokenize.py
# case: TestTokenize_test_comment_at_the_end_of_the_source_without_newline

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    source = 'b = 1\n\n#test'
    expected_tokens = [token.NAME, token.EQUAL, token.NUMBER, token.NEWLINE, token.NL, token.COMMENT]
    tokens = list(tokenize(BytesIO(source.encode('utf-8')).readline))
    self.assertEqual(tok_name[tokens[0].exact_type], tok_name[ENCODING])
    for i in range(6):
        self.assertEqual(tok_name[tokens[i + 1].exact_type], tok_name[expected_tokens[i]])
    self.assertEqual(tok_name[tokens[-1].exact_type], tok_name[token.ENDMARKER])
