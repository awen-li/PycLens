# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httpservers.py
# case: CGIHTTPServerTestCase_test_url_collapse_path

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    test_vectors = {'': '//', '..': IndexError, '/.//..': IndexError, '/': '//', '//': '//', '/\\': '//\\', '/.//': '//', 'cgi-bin/file1.py': '/cgi-bin/file1.py', '/cgi-bin/file1.py': '/cgi-bin/file1.py', 'a': '//a', '/a': '//a', '//a': '//a', './a': '//a', './C:/': '/C:/', '/a/b': '/a/b', '/a/b/': '/a/b/', '/a/b/.': '/a/b/', '/a/b/c/..': '/a/b/', '/a/b/c/../d': '/a/b/d', '/a/b/c/../d/e/../f': '/a/b/d/f', '/a/b/c/../d/e/../../f': '/a/b/f', '/a/b/c/../d/e/.././././..//f': '/a/b/f', '../a/b/c/../d/e/.././././..//f': IndexError, '/a/b/c/../d/e/../../../f': '/a/f', '/a/b/c/../d/e/../../../../f': '//f', '/a/b/c/../d/e/../../../../../f': IndexError, '/a/b/c/../d/e/../../../../f/..': '//', '/a/b/c/../d/e/../../../../f/../.': '//'}
    for (path, expected) in test_vectors.items():
        if isinstance(expected, type) and issubclass(expected, Exception):
            self.assertRaises(expected, server._url_collapse_path, path)
        else:
            actual = server._url_collapse_path(path)
            self.assertEqual(expected, actual, msg='path = %r\nGot:    %r\nWanted: %r' % (path, actual, expected))
