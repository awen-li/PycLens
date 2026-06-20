# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_csv.py
# case: TestDialectRegistry_test_register_kwargs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    name = 'fedcba'
    csv.register_dialect(name, delimiter=';')
    self.addCleanup(csv.unregister_dialect, name)
    self.assertEqual(csv.get_dialect(name).delimiter, ';')
    self.assertEqual([['X', 'Y', 'Z']], list(csv.reader(['X;Y;Z'], name)))
