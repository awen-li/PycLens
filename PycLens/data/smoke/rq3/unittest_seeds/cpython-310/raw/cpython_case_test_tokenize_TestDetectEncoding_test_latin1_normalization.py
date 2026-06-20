# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tokenize.py
# case: TestDetectEncoding_test_latin1_normalization

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    encodings = ('latin-1', 'iso-8859-1', 'iso-latin-1', 'latin-1-unix', 'iso-8859-1-unix', 'iso-latin-1-mac')
    for encoding in encodings:
        for rep in ('-', '_'):
            enc = encoding.replace('-', rep)
            lines = (b'#!/usr/bin/python\n', b'# coding: ' + enc.encode('ascii') + b'\n', b'print(things)\n', b'do_something += 4\n')
            rl = self.get_readline(lines)
            (found, consumed_lines) = detect_encoding(rl)
            self.assertEqual(found, 'iso-8859-1')
