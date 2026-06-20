# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_locale.py
# case: TestLocaleFormatString_test_percent_escape

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(locale.format_string('%f%%', 1.0), '%f%%' % 1.0)
    self.assertEqual(locale.format_string('%d %f%%d', (1, 1.0)), '%d %f%%d' % (1, 1.0))
    self.assertEqual(locale.format_string('%(foo)s %%d', {'foo': 'bar'}), '%(foo)s %%d' % {'foo': 'bar'})
