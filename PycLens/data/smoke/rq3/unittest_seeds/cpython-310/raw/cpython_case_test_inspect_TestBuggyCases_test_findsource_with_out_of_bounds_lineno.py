# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestBuggyCases_test_findsource_with_out_of_bounds_lineno

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    mod_len = len(inspect.getsource(mod))
    src = '\n' * 2 * mod_len + 'def f(): pass'
    co = compile(src, mod.__file__, 'exec')
    (g, l) = ({}, {})
    eval(co, g, l)
    func = l['f']
    self.assertEqual(func.__code__.co_firstlineno, 1 + 2 * mod_len)
    with self.assertRaisesRegex(IOError, 'lineno is out of bounds'):
        inspect.findsource(func)
