# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tokenize.py
# case: TestRoundtrip_test_roundtrip

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_roundtrip('if x == 1:\n    print(x)\n')
    self.check_roundtrip('# This is a comment\n# This also\n')
    self.check_roundtrip('if x == 1 : \n  print(x)\n')
    fn = support.findfile('tokenize_tests.txt')
    with open(fn, 'rb') as f:
        self.check_roundtrip(f)
    self.check_roundtrip('if x == 1:\n    # A comment by itself.\n    print(x) # Comment here, too.\n    # Another comment.\nafter_if = True\n')
    self.check_roundtrip("if (x # The comments need to go in the right place\n    == 1):\n    print('x==1')\n")
    self.check_roundtrip('class Test: # A comment here\n  # A comment with weird indent\n  after_com = 5\n  def x(m): return m*5 # a one liner\n  def y(m): # A whitespace after the colon\n     return y*4 # 3-space indent\n')
    self.check_roundtrip("try: import somemodule\nexcept ImportError: # comment\n    print('Can not import' # comment2\n)else:   print('Loaded')\n")
