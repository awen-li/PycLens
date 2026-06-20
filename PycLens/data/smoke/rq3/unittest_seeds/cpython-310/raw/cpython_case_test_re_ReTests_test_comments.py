# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_comments

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(re.fullmatch('#x\na', 'a', re.VERBOSE))
    self.assertTrue(re.fullmatch(b'#x\na', b'a', re.VERBOSE))
    self.assertTrue(re.fullmatch('(?x)#x\na', 'a'))
    self.assertTrue(re.fullmatch('#x\n(?x)#y\na', 'a', re.VERBOSE))
    self.assertTrue(re.fullmatch('(?x)#x\n(?x)#y\na', 'a'))
    self.assertTrue(re.fullmatch('#x\na(?x:#y\nb)#z\nc', '#x\nab#z\nc'))
    self.assertTrue(re.fullmatch('#x\na(?-x:#y\nb)#z\nc', 'a#y\nbc', re.VERBOSE))
    self.assertTrue(re.fullmatch('(?x)#x\na(?-x:#y\nb)#z\nc', 'a#y\nbc'))
    self.assertTrue(re.fullmatch('(?x)#x\na|#y\nb', 'a'))
    self.assertTrue(re.fullmatch('(?x)#x\na|#y\nb', 'b'))
