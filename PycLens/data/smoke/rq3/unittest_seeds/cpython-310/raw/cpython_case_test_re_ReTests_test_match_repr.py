# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_match_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for string in ('[abracadabra]', S('[abracadabra]')):
        m = re.search('(.+)(.*?)\\1', string)
        pattern = "<(%s\\.)?%s object; span=\\(1, 12\\), match='abracadabra'>" % (type(m).__module__, type(m).__qualname__)
        self.assertRegex(repr(m), pattern)
    for string in (b'[abracadabra]', B(b'[abracadabra]'), bytearray(b'[abracadabra]'), memoryview(b'[abracadabra]')):
        m = re.search(b'(.+)(.*?)\\1', string)
        pattern = "<(%s\\.)?%s object; span=\\(1, 12\\), match=b'abracadabra'>" % (type(m).__module__, type(m).__qualname__)
        self.assertRegex(repr(m), pattern)
    (first, second) = list(re.finditer('(aa)|(bb)', 'aa bb'))
    pattern = "<(%s\\.)?%s object; span=\\(0, 2\\), match='aa'>" % (type(second).__module__, type(second).__qualname__)
    self.assertRegex(repr(first), pattern)
    pattern = "<(%s\\.)?%s object; span=\\(3, 5\\), match='bb'>" % (type(second).__module__, type(second).__qualname__)
    self.assertRegex(repr(second), pattern)
