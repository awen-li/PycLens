# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_string.py
# case: ModuleTest_test_override_convert_field

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class XFormatter(string.Formatter):

        def convert_field(self, value, conversion):
            if conversion == 'x':
                return None
            return super().convert_field(value, conversion)
    fmt = XFormatter()
    self.assertEqual(fmt.format('{0!r}:{0!x}', 'foo', 'foo'), "'foo':None")
