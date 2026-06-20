# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_string.py
# case: ModuleTest_test_override_format_field

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class CallFormatter(string.Formatter):

        def format_field(self, value, format_spec):
            return format(value(), format_spec)
    fmt = CallFormatter()
    self.assertEqual(fmt.format('*{0}*', lambda : 'result'), '*result*')
