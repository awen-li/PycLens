# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_possible_set_operations

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = bytes(range(128)).decode()
    with self.assertWarns(FutureWarning):
        p = re.compile('[0-9--1]')
    self.assertEqual(p.findall(s), list('-./0123456789'))
    self.assertEqual(re.findall('[--1]', s), list('-./01'))
    with self.assertWarns(FutureWarning):
        p = re.compile('[%--1]')
    self.assertEqual(p.findall(s), list("%&'()*+,-1"))
    with self.assertWarns(FutureWarning):
        p = re.compile('[%--]')
    self.assertEqual(p.findall(s), list("%&'()*+,-"))
    with self.assertWarns(FutureWarning):
        p = re.compile('[0-9&&1]')
    self.assertEqual(p.findall(s), list('&0123456789'))
    with self.assertWarns(FutureWarning):
        p = re.compile('[\\d&&1]')
    self.assertEqual(p.findall(s), list('&0123456789'))
    self.assertEqual(re.findall('[&&1]', s), list('&1'))
    with self.assertWarns(FutureWarning):
        p = re.compile('[0-9||a]')
    self.assertEqual(p.findall(s), list('0123456789a|'))
    with self.assertWarns(FutureWarning):
        p = re.compile('[\\d||a]')
    self.assertEqual(p.findall(s), list('0123456789a|'))
    self.assertEqual(re.findall('[||1]', s), list('1|'))
    with self.assertWarns(FutureWarning):
        p = re.compile('[0-9~~1]')
    self.assertEqual(p.findall(s), list('0123456789~'))
    with self.assertWarns(FutureWarning):
        p = re.compile('[\\d~~1]')
    self.assertEqual(p.findall(s), list('0123456789~'))
    self.assertEqual(re.findall('[~~1]', s), list('1~'))
    with self.assertWarns(FutureWarning):
        p = re.compile('[[0-9]|]')
    self.assertEqual(p.findall(s), list('0123456789[]'))
    with self.assertWarns(FutureWarning):
        p = re.compile('[[:digit:]|]')
    self.assertEqual(p.findall(s), list(':[]dgit'))
