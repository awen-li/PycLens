# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_string.py
# case: ModuleTest_test_name_lookup

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fmt = string.Formatter()

    class AnyAttr:

        def __getattr__(self, attr):
            return attr
    x = AnyAttr()
    self.assertEqual(fmt.format('{0.lumber}{0.jack}', x), 'lumberjack')
    with self.assertRaises(AttributeError):
        fmt.format('{0.lumber}{0.jack}', '')
