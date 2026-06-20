# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compile.py
# case: TestSpecifics_test_extended_arg

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    longexpr = 'x = x or ' + '-x' * 2500
    g = {}
    code = '\ndef f(x):\n    %s\n    %s\n    %s\n    %s\n    %s\n    %s\n    %s\n    %s\n    %s\n    %s\n    # the expressions above have no effect, x == argument\n    while x:\n        x -= 1\n        # EXTENDED_ARG/JUMP_ABSOLUTE here\n    return x\n' % ((longexpr,) * 10)
    exec(code, g)
    self.assertEqual(g['f'](5), 0)
