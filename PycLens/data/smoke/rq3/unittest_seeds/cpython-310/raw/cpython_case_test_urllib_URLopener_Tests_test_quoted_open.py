# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: URLopener_Tests_test_quoted_open

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class DummyURLopener(urllib.request.URLopener):

        def open_spam(self, url):
            return url
    with warnings_helper.check_warnings(('DummyURLopener style of invoking requests is deprecated.', DeprecationWarning)):
        self.assertEqual(DummyURLopener().open('spam://example/ /'), '//example/%20/')
        self.assertEqual(DummyURLopener().open("spam://c:|windows%/:=&?~#+!$,;'@()*[]|/path/"), "//c:|windows%/:=&?~#+!$,;'@()*[]|/path/")
