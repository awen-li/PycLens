# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ttk_textonly.py
# case: InternalFunctionsTest_test_format_optdict

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def check_against(fmt_opts, result):
        for i in range(0, len(fmt_opts), 2):
            self.assertEqual(result.pop(fmt_opts[i]), fmt_opts[i + 1])
        if result:
            self.fail('result still got elements: %s' % result)
    self.assertFalse(ttk._format_optdict({}))
    check_against(ttk._format_optdict({'fg': 'blue', 'padding': [1, 2, 3, 4]}), {'-fg': 'blue', '-padding': '1 2 3 4'})
    check_against(ttk._format_optdict({'test': (1, 2, '', 0)}), {'-test': '1 2 {} 0'})
    check_against(ttk._format_optdict({'test': {'left': 'as is'}}), {'-test': {'left': 'as is'}})
    check_against(ttk._format_optdict({'test': [1, -1, '', '2m', 0], 'test2': 3, 'test3': '', 'test4': 'abc def', 'test5': '"abc"', 'test6': '{}', 'test7': '} -spam {'}, script=True), {'-test': '{1 -1 {} 2m 0}', '-test2': '3', '-test3': '{}', '-test4': '{abc def}', '-test5': '{"abc"}', '-test6': '\\{\\}', '-test7': '\\}\\ -spam\\ \\{'})
    opts = {'αβγ': True, 'á': False}
    orig_opts = opts.copy()
    check_against(ttk._format_optdict(opts), {'-αβγ': True, '-á': False})
    self.assertEqual(opts, orig_opts)
    check_against(ttk._format_optdict({'option': ('one two', 'three')}), {'-option': '{one two} three'})
    check_against(ttk._format_optdict({'option': ('one\ttwo', 'three')}), {'-option': '{one\ttwo} three'})
    check_against(ttk._format_optdict({'option': ('', 'one')}), {'-option': '{} one'})
    check_against(ttk._format_optdict({'option': ('one} {two', 'three')}), {'-option': 'one\\}\\ \\{two three'})
    check_against(ttk._format_optdict({'option': ('"one"', 'two')}), {'-option': '{"one"} two'})
    check_against(ttk._format_optdict({'option': ('{one}', 'two')}), {'-option': '\\{one\\} two'})
    amount_opts = len(ttk._format_optdict(opts, ignore='á')) / 2
    self.assertEqual(amount_opts, len(opts) - 1)
    amount_opts = len(ttk._format_optdict(opts, ignore=('á', 'b'))) / 2
    self.assertEqual(amount_opts, len(opts) - 1)
    self.assertFalse(ttk._format_optdict(opts, ignore=list(opts.keys())))
