# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tcl.py
# case: TclTest_test_user_command

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    result = None

    def testfunc(arg):
        nonlocal result
        result = arg
        return arg
    self.interp.createcommand('testfunc', testfunc)
    self.addCleanup(self.interp.tk.deletecommand, 'testfunc')

    def check(value, expected=None, *, eq=self.assertEqual):
        if expected is None:
            expected = value
        nonlocal result
        result = None
        r = self.interp.call('testfunc', value)
        self.assertIsInstance(result, str)
        eq(result, expected)
        self.assertIsInstance(r, str)
        eq(r, expected)

    def float_eq(actual, expected):
        self.assertAlmostEqual(float(actual), expected, delta=abs(expected) * 1e-10)
    check(True, '1')
    check(False, '0')
    check('string')
    check('string½')
    check('string€')
    check('string💻')
    if sys.platform != 'win32':
        check('<\udce2\udc82\udcac>', '<€>')
        check('<\udced\udca0\udcbd\udced\udcb2\udcbb>', '<💻>')
    check('')
    check(b'string', 'string')
    check(b'string\xe2\x82\xac', 'stringâ\x82¬')
    check(b'string\xbd', 'string½')
    check(b'', '')
    check('str\x00ing')
    check('str\x00ing½')
    check('str\x00ing€')
    check(b'str\x00ing', 'str\x00ing')
    check(b'str\xc0\x80ing', 'strÀ\x80ing')
    check(b'str\xc0\x80ing\xe2\x82\xac', 'strÀ\x80ingâ\x82¬')
    for i in self.get_integers():
        check(i, str(i))
    if tcl_version < (8, 5):
        check(2 ** 1000, str(2 ** 1000))
    for f in (0.0, 1.0, -1.0):
        check(f, repr(f))
    for f in (1 / 3.0, sys.float_info.min, sys.float_info.max, -sys.float_info.min, -sys.float_info.max):
        check(f, eq=float_eq)
    check(float('inf'), eq=float_eq)
    check(-float('inf'), eq=float_eq)
    check((), '')
    check((1, (2,), (3, 4), '5 6', ()), '1 2 {3 4} {5 6} {}')
    check([1, [2], [3, 4], '5 6', []], '1 2 {3 4} {5 6} {}')
