# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tcl.py
# case: TclTest_test_splitdict

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    splitdict = tkinter._splitdict
    tcl = self.interp.tk
    arg = '-a {1 2 3} -something foo status {}'
    self.assertEqual(splitdict(tcl, arg, False), {'-a': '1 2 3', '-something': 'foo', 'status': ''})
    self.assertEqual(splitdict(tcl, arg), {'a': '1 2 3', 'something': 'foo', 'status': ''})
    arg = ('-a', (1, 2, 3), '-something', 'foo', 'status', '{}')
    self.assertEqual(splitdict(tcl, arg, False), {'-a': (1, 2, 3), '-something': 'foo', 'status': '{}'})
    self.assertEqual(splitdict(tcl, arg), {'a': (1, 2, 3), 'something': 'foo', 'status': '{}'})
    self.assertRaises(RuntimeError, splitdict, tcl, '-a b -c ')
    self.assertRaises(RuntimeError, splitdict, tcl, ('-a', 'b', '-c'))
    arg = tcl.call('list', '-a', (1, 2, 3), '-something', 'foo', 'status', ())
    self.assertEqual(splitdict(tcl, arg), {'a': (1, 2, 3) if self.wantobjects else '1 2 3', 'something': 'foo', 'status': ''})
    if tcl_version >= (8, 5):
        arg = tcl.call('dict', 'create', '-a', (1, 2, 3), '-something', 'foo', 'status', ())
        if not self.wantobjects or get_tk_patchlevel() < (8, 5, 5):
            expected = {'a': '1 2 3', 'something': 'foo', 'status': ''}
        else:
            expected = {'a': (1, 2, 3), 'something': 'foo', 'status': ''}
        self.assertEqual(splitdict(tcl, arg), expected)
