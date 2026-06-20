# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_locale.py
# case: TestLocaleFormatString_test_mapping

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(locale.format_string('%(foo)s bing.', {'foo': 'bar'}), '%(foo)s bing.' % {'foo': 'bar'})
    self.assertEqual(locale.format_string('%(foo)s', {'foo': 'bar'}), '%(foo)s' % {'foo': 'bar'})
