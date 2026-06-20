# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codeccallbacks.py
# case: CodecCallbackTest_test_bug828737

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    charmap = {ord('&'): '&amp;', ord('<'): '&lt;', ord('>'): '&gt;', ord('"'): '&quot;'}
    for n in (1, 10, 100, 1000):
        text = 'abc<def>ghi' * n
        text.translate(charmap)
