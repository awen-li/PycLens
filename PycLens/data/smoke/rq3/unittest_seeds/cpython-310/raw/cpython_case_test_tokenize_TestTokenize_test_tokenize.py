# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tokenize.py
# case: TestTokenize_test_tokenize

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import tokenize as tokenize_module
    encoding = object()
    encoding_used = None

    def mock_detect_encoding(readline):
        return (encoding, [b'first', b'second'])

    def mock__tokenize(readline, encoding):
        nonlocal encoding_used
        encoding_used = encoding
        out = []
        while True:
            next_line = readline()
            if next_line:
                out.append(next_line)
                continue
            return out
    counter = 0

    def mock_readline():
        nonlocal counter
        counter += 1
        if counter == 5:
            return b''
        return str(counter).encode()
    orig_detect_encoding = tokenize_module.detect_encoding
    orig__tokenize = tokenize_module._tokenize
    tokenize_module.detect_encoding = mock_detect_encoding
    tokenize_module._tokenize = mock__tokenize
    try:
        results = tokenize(mock_readline)
        self.assertEqual(list(results), [b'first', b'second', b'1', b'2', b'3', b'4'])
    finally:
        tokenize_module.detect_encoding = orig_detect_encoding
        tokenize_module._tokenize = orig__tokenize
    self.assertEqual(encoding_used, encoding)
