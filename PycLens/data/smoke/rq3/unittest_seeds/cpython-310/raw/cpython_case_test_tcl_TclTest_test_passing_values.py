# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tcl.py
# case: TclTest_test_passing_values

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def passValue(value):
        return self.interp.call('set', '_', value)
    self.assertEqual(passValue(True), True if self.wantobjects else '1')
    self.assertEqual(passValue(False), False if self.wantobjects else '0')
    self.assertEqual(passValue('string'), 'string')
    self.assertEqual(passValue('string€'), 'string€')
    self.assertEqual(passValue('string💻'), 'string💻')
    self.assertEqual(passValue('str\x00ing'), 'str\x00ing')
    self.assertEqual(passValue('str\x00ing½'), 'str\x00ing½')
    self.assertEqual(passValue('str\x00ing€'), 'str\x00ing€')
    self.assertEqual(passValue('str\x00ing💻'), 'str\x00ing💻')
    if sys.platform != 'win32':
        self.assertEqual(passValue('<\udce2\udc82\udcac>'), '<€>')
        self.assertEqual(passValue('<\udced\udca0\udcbd\udced\udcb2\udcbb>'), '<💻>')
    self.assertEqual(passValue(b'str\x00ing'), b'str\x00ing' if self.wantobjects else 'str\x00ing')
    self.assertEqual(passValue(b'str\xc0\x80ing'), b'str\xc0\x80ing' if self.wantobjects else 'strÀ\x80ing')
    self.assertEqual(passValue(b'str\xbding'), b'str\xbding' if self.wantobjects else 'str½ing')
    for i in self.get_integers():
        self.assertEqual(passValue(i), i if self.wantobjects else str(i))
    if tcl_version < (8, 5):
        self.assertEqual(passValue(2 ** 1000), str(2 ** 1000))
    for f in (0.0, 1.0, -1.0, 1 / 3, sys.float_info.min, sys.float_info.max, -sys.float_info.min, -sys.float_info.max):
        if self.wantobjects:
            self.assertEqual(passValue(f), f)
        else:
            self.assertEqual(float(passValue(f)), f)
    if self.wantobjects:
        f = passValue(float('nan'))
        self.assertNotEqual(f, f)
        self.assertEqual(passValue(float('inf')), float('inf'))
        self.assertEqual(passValue(-float('inf')), -float('inf'))
    else:
        self.assertEqual(float(passValue(float('inf'))), float('inf'))
        self.assertEqual(float(passValue(-float('inf'))), -float('inf'))
    self.assertEqual(passValue((1, '2', (3.4,))), (1, '2', (3.4,)) if self.wantobjects else '1 2 3.4')
    self.assertEqual(passValue(['a', ['b', 'c']]), ('a', ('b', 'c')) if self.wantobjects else 'a {b c}')
