# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fstring.py
# case: TestCase_test_many_expressions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def build_fstr(n, extra=''):
        return "f'" + '{x} ' * n + extra + "'"
    x = 'X'
    width = 1
    for i in range(250, 260):
        self.assertEqual(eval(build_fstr(i)), (x + ' ') * i)
    self.assertEqual(eval(build_fstr(255) * 256), (x + ' ') * (255 * 256))
    s = build_fstr(253, '{x:{width}} ')
    self.assertEqual(eval(s), (x + ' ') * 254)
    s = "f'{1}' 'x' 'y'" * 1024
    self.assertEqual(eval(s), '1xy' * 1024)
