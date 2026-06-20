# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: RETests_test_re_submodule

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from typing.re import Match, Pattern, __all__, __name__
    self.assertIs(Match, typing.Match)
    self.assertIs(Pattern, typing.Pattern)
    self.assertEqual(set(__all__), set(['Match', 'Pattern']))
    self.assertEqual(__name__, 'typing.re')
