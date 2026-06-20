# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ttk_textonly.py
# case: InternalFunctionsTest_test_val_or_dict

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def func(res, opt=None, val=None):
        if opt is None:
            return res
        if val is None:
            return 'test val'
        return (opt, val)
    tk = MockTkApp()
    tk.call = func
    self.assertEqual(ttk._val_or_dict(tk, {}, '-test:3'), {'test': '3'})
    self.assertEqual(ttk._val_or_dict(tk, {}, ('-test', 3)), {'test': 3})
    self.assertEqual(ttk._val_or_dict(tk, {'test': None}, 'x:y'), 'test val')
    self.assertEqual(ttk._val_or_dict(tk, {'test': 3}, 'x:y'), {'test': 3})
