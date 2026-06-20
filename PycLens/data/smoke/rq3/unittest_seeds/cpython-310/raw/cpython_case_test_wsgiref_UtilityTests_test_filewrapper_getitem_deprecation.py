# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_wsgiref.py
# case: UtilityTests_test_filewrapper_getitem_deprecation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    wrapper = util.FileWrapper(StringIO('foobar'), 3)
    with self.assertWarnsRegex(DeprecationWarning, 'Use iterator protocol instead'):
        self.assertEqual(wrapper[1], 'foo')
