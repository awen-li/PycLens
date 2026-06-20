# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_difflib.py
# case: TestSFpatches_test_html_diff

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f1a = (patch914575_from1 + '123\n' * 10) * 3
    t1a = (patch914575_to1 + '123\n' * 10) * 3
    f1b = '456\n' * 10 + f1a
    t1b = '456\n' * 10 + t1a
    f1a = f1a.splitlines()
    t1a = t1a.splitlines()
    f1b = f1b.splitlines()
    t1b = t1b.splitlines()
    f2 = patch914575_from2.splitlines()
    t2 = patch914575_to2.splitlines()
    f3 = patch914575_from3
    t3 = patch914575_to3
    i = difflib.HtmlDiff()
    j = difflib.HtmlDiff(tabsize=2)
    k = difflib.HtmlDiff(wrapcolumn=14)
    full = i.make_file(f1a, t1a, 'from', 'to', context=False, numlines=5)
    tables = '\n'.join(['<h2>Context (first diff within numlines=5(default))</h2>', i.make_table(f1a, t1a, 'from', 'to', context=True), '<h2>Context (first diff after numlines=5(default))</h2>', i.make_table(f1b, t1b, 'from', 'to', context=True), '<h2>Context (numlines=6)</h2>', i.make_table(f1a, t1a, 'from', 'to', context=True, numlines=6), '<h2>Context (numlines=0)</h2>', i.make_table(f1a, t1a, 'from', 'to', context=True, numlines=0), '<h2>Same Context</h2>', i.make_table(f1a, f1a, 'from', 'to', context=True), '<h2>Same Full</h2>', i.make_table(f1a, f1a, 'from', 'to', context=False), '<h2>Empty Context</h2>', i.make_table([], [], 'from', 'to', context=True), '<h2>Empty Full</h2>', i.make_table([], [], 'from', 'to', context=False), '<h2>tabsize=2</h2>', j.make_table(f2, t2), '<h2>tabsize=default</h2>', i.make_table(f2, t2), '<h2>Context (wrapcolumn=14,numlines=0)</h2>', k.make_table(f3.splitlines(), t3.splitlines(), context=True, numlines=0), '<h2>wrapcolumn=14,splitlines()</h2>', k.make_table(f3.splitlines(), t3.splitlines()), '<h2>wrapcolumn=14,splitlines(True)</h2>', k.make_table(f3.splitlines(True), t3.splitlines(True))])
    actual = full.replace('</body>', '\n%s\n</body>' % tables)
    with open(findfile('test_difflib_expect.html'), encoding='utf-8') as fp:
        self.assertEqual(actual, fp.read())
