# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_source_encoding.py
# case: AbstractSourceEncodingTest_test_second_non_utf8_coding_line

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    src = b'\n#coding:iso-8859-15 \xa4\nprint(ascii("\xc3\xa4"))\n'
    self.check_script_output(src, b"'\\xc3\\u20ac'")
