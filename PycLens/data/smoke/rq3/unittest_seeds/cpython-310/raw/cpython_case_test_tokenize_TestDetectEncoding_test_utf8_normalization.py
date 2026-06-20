# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tokenize.py
# case: TestDetectEncoding_test_utf8_normalization

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    encodings = ('utf-8', 'utf-8-mac', 'utf-8-unix')
    for encoding in encodings:
        for rep in ('-', '_'):
            enc = encoding.replace('-', rep)
            lines = (b'#!/usr/bin/python\n', b'# coding: ' + enc.encode('ascii') + b'\n', b'1 + 3\n')
            rl = self.get_readline(lines)
            (found, consumed_lines) = detect_encoding(rl)
            self.assertEqual(found, 'utf-8')
