# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2.py
# case: TrivialTests_test_trivial

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.addCleanup(urllib.request.urlcleanup)
    self.assertRaises(ValueError, urllib.request.urlopen, 'bogus url')
    fname = os.path.abspath(urllib.request.__file__).replace(os.sep, '/')
    if os.name == 'nt':
        file_url = 'file:///%s' % fname
    else:
        file_url = 'file://%s' % fname
    with urllib.request.urlopen(file_url) as f:
        f.read()
