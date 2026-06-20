# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_positional_only_arg.py
# case: PositionalOnlyTestCase_test_syntax_for_many_positional_only

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fundef = 'def f(%s, /):\n  pass\n' % ', '.join(('i%d' % i for i in range(300)))
    compile(fundef, '<test>', 'single')
