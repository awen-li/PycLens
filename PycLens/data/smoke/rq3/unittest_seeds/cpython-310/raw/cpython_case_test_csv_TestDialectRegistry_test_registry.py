# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_csv.py
# case: TestDialectRegistry_test_registry

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class myexceltsv(csv.excel):
        delimiter = '\t'
    name = 'myexceltsv'
    expected_dialects = csv.list_dialects() + [name]
    expected_dialects.sort()
    csv.register_dialect(name, myexceltsv)
    self.addCleanup(csv.unregister_dialect, name)
    self.assertEqual(csv.get_dialect(name).delimiter, '\t')
    got_dialects = sorted(csv.list_dialects())
    self.assertEqual(expected_dialects, got_dialects)
