# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: BugsTest_test_expat224_utf8_bug

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    text = b'\xc3\xa0' * 1024
    self.check_expat224_utf8_bug(text)
    text = b'x' + b'\xc3\xa0' * 1024
    self.check_expat224_utf8_bug(text)
