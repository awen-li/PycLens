# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_string.py
# case: ModuleTest_test_index_lookup

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fmt = string.Formatter()
    lookup = ['eggs', 'and', 'spam']
    self.assertEqual(fmt.format('{0[2]}{0[0]}', lookup), 'spameggs')
    with self.assertRaises(IndexError):
        fmt.format('{0[2]}{0[0]}', [])
    with self.assertRaises(KeyError):
        fmt.format('{0[2]}{0[0]}', {})
