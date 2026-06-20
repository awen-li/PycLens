# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fnmatch.py
# case: FilterTestCase_test_case

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ignorecase = os.path.normcase('P') == os.path.normcase('p')
    self.assertEqual(filter(['Test.py', 'Test.rb', 'Test.PL'], '*.p*'), ['Test.py', 'Test.PL'] if ignorecase else ['Test.py'])
    self.assertEqual(filter(['Test.py', 'Test.rb', 'Test.PL'], '*.P*'), ['Test.py', 'Test.PL'] if ignorecase else ['Test.PL'])
