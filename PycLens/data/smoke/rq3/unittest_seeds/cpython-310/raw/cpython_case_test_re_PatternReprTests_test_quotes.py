# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: PatternReprTests_test_quotes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check('random "double quoted" pattern', 're.compile(\'random "double quoted" pattern\')')
    self.check("random 'single quoted' pattern", 're.compile("random \'single quoted\' pattern")')
    self.check('both \'single\' and "double" quotes', 're.compile(\'both \\\'single\\\' and "double" quotes\')')
