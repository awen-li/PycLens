# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: Pathname_Tests_test_basic

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expected_path = os.path.join('parts', 'of', 'a', 'path')
    expected_url = 'parts/of/a/path'
    result = urllib.request.pathname2url(expected_path)
    self.assertEqual(expected_url, result, 'pathname2url() failed; %s != %s' % (result, expected_url))
    result = urllib.request.url2pathname(expected_url)
    self.assertEqual(expected_path, result, 'url2pathame() failed; %s != %s' % (result, expected_path))
