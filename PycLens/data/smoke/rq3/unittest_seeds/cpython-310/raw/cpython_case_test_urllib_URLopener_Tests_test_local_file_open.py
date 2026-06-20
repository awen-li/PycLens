# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: URLopener_Tests_test_local_file_open

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class DummyURLopener(urllib.request.URLopener):

        def open_local_file(self, url):
            return url
    for url in ('local_file://example', 'local-file://example'):
        self.assertRaises(OSError, urllib.request.urlopen, url)
        self.assertRaises(OSError, urllib.request.URLopener().open, url)
        self.assertRaises(OSError, urllib.request.URLopener().retrieve, url)
        self.assertRaises(OSError, DummyURLopener().open, url)
        self.assertRaises(OSError, DummyURLopener().retrieve, url)
