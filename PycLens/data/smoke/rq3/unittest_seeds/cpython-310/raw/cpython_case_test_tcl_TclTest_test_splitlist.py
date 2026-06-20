# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tcl.py
# case: TclTest_test_splitlist

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    splitlist = self.interp.tk.splitlist
    call = self.interp.tk.call
    self.assertRaises(TypeError, splitlist)
    self.assertRaises(TypeError, splitlist, 'a', 'b')
    self.assertRaises(TypeError, splitlist, 2)
    testcases = [('2', ('2',)), ('', ()), ('{}', ('',)), ('""', ('',)), ('a\n b\t\r c\n ', ('a', 'b', 'c')), (b'a\n b\t\r c\n ', ('a', 'b', 'c')), ('a €', ('a', '€')), ('a 💻', ('a', '💻')), (b'a \xe2\x82\xac', ('a', '€')), (b'a \xf0\x9f\x92\xbb', ('a', '💻')), (b'a \xed\xa0\xbd\xed\xb2\xbb', ('a', '💻')), (b'a\xc0\x80b c\xc0\x80d', ('a\x00b', 'c\x00d')), ('a {b c}', ('a', 'b c')), ('a b\\ c', ('a', 'b c')), (('a', 'b c'), ('a', 'b c')), ('a 2', ('a', '2')), (('a', 2), ('a', 2)), ('a 3.4', ('a', '3.4')), (('a', 3.4), ('a', 3.4)), ((), ()), ([], ()), (['a', ['b', 'c']], ('a', ['b', 'c'])), (call('list', 1, '2', (3.4,)), (1, '2', (3.4,)) if self.wantobjects else ('1', '2', '3.4'))]
    tk_patchlevel = get_tk_patchlevel()
    if tcl_version >= (8, 5):
        if not self.wantobjects or tk_patchlevel < (8, 5, 5):
            expected = ('12', '€', 'â\x82¬', '3.4')
        else:
            expected = (12, '€', b'\xe2\x82\xac', (3.4,))
        testcases += [(call('dict', 'create', 12, '€', b'\xe2\x82\xac', (3.4,)), expected)]
    dbg_info = 'want objects? %s, Tcl version: %s, Tk patchlevel: %s' % (self.wantobjects, tcl_version, tk_patchlevel)
    for (arg, res) in testcases:
        self.assertEqual(splitlist(arg), res, 'arg=%a, %s' % (arg, dbg_info))
    self.assertRaises(TclError, splitlist, '{')
