# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_finditer

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    iter = re.finditer(':+', 'a:b::c:::d')
    self.assertEqual([item.group(0) for item in iter], [':', '::', ':::'])
    pat = re.compile(':+')
    iter = pat.finditer('a:b::c:::d', 1, 10)
    self.assertEqual([item.group(0) for item in iter], [':', '::', ':::'])
    pat = re.compile(':+')
    iter = pat.finditer('a:b::c:::d', pos=1, endpos=10)
    self.assertEqual([item.group(0) for item in iter], [':', '::', ':::'])
    pat = re.compile(':+')
    iter = pat.finditer('a:b::c:::d', endpos=10, pos=1)
    self.assertEqual([item.group(0) for item in iter], [':', '::', ':::'])
    pat = re.compile(':+')
    iter = pat.finditer('a:b::c:::d', pos=3, endpos=8)
    self.assertEqual([item.group(0) for item in iter], ['::', '::'])
