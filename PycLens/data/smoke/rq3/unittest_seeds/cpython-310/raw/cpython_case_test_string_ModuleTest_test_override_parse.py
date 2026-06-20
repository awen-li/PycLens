# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_string.py
# case: ModuleTest_test_override_parse

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class BarFormatter(string.Formatter):

        def parse(self, format_string):
            for field in format_string.split('|'):
                if field[0] == '+':
                    (field_name, _, format_spec) = field[1:].partition(':')
                    yield ('', field_name, format_spec, None)
                else:
                    yield (field, None, None, None)
    fmt = BarFormatter()
    self.assertEqual(fmt.format('*|+0:^10s|*', 'foo'), '*   foo    *')
