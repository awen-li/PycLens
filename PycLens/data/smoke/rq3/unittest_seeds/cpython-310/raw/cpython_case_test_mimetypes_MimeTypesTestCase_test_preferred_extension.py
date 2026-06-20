# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mimetypes.py
# case: MimeTypesTestCase_test_preferred_extension

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def check_extensions():
        self.assertEqual(mimetypes.guess_extension('application/octet-stream'), '.bin')
        self.assertEqual(mimetypes.guess_extension('application/postscript'), '.ps')
        self.assertEqual(mimetypes.guess_extension('application/vnd.apple.mpegurl'), '.m3u')
        self.assertEqual(mimetypes.guess_extension('application/vnd.ms-excel'), '.xls')
        self.assertEqual(mimetypes.guess_extension('application/vnd.ms-powerpoint'), '.ppt')
        self.assertEqual(mimetypes.guess_extension('application/x-texinfo'), '.texi')
        self.assertEqual(mimetypes.guess_extension('application/x-troff'), '.roff')
        self.assertEqual(mimetypes.guess_extension('application/xml'), '.xsl')
        self.assertEqual(mimetypes.guess_extension('audio/mpeg'), '.mp3')
        self.assertEqual(mimetypes.guess_extension('image/jpeg'), '.jpg')
        self.assertEqual(mimetypes.guess_extension('image/tiff'), '.tiff')
        self.assertEqual(mimetypes.guess_extension('message/rfc822'), '.eml')
        self.assertEqual(mimetypes.guess_extension('text/html'), '.html')
        self.assertEqual(mimetypes.guess_extension('text/plain'), '.txt')
        self.assertEqual(mimetypes.guess_extension('video/mpeg'), '.mpeg')
        self.assertEqual(mimetypes.guess_extension('video/quicktime'), '.mov')
    check_extensions()
    mimetypes.init()
    check_extensions()
