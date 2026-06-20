# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_textwrap.py
# case: WrapTestCase_test_funky_hyphens

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_split('what the--hey!', ['what', ' ', 'the', '--', 'hey!'])
    self.check_split('what the--', ['what', ' ', 'the--'])
    self.check_split('what the--.', ['what', ' ', 'the--.'])
    self.check_split('--text--.', ['--text--.'])
    self.check_split('--option', ['--option'])
    self.check_split('--option-opt', ['--option-', 'opt'])
    self.check_split('foo --option-opt bar', ['foo', ' ', '--option-', 'opt', ' ', 'bar'])
