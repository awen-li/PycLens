# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_source_encoding.py
# case: AbstractSourceEncodingTest_test_crcrcrlf2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    src = b'#coding:iso-8859-1\nprint(ascii("""\r\r\r\n"""))\n'
    out = self.check_script_output(src, b"'\\n\\n\\n'")
