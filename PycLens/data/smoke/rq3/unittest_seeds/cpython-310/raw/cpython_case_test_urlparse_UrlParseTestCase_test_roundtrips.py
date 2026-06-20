# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urlparse.py
# case: UrlParseTestCase_test_roundtrips

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    str_cases = [('file:///tmp/junk.txt', ('file', '', '/tmp/junk.txt', '', '', ''), ('file', '', '/tmp/junk.txt', '', '')), ('imap://mail.python.org/mbox1', ('imap', 'mail.python.org', '/mbox1', '', '', ''), ('imap', 'mail.python.org', '/mbox1', '', '')), ('mms://wms.sys.hinet.net/cts/Drama/09006251100.asf', ('mms', 'wms.sys.hinet.net', '/cts/Drama/09006251100.asf', '', '', ''), ('mms', 'wms.sys.hinet.net', '/cts/Drama/09006251100.asf', '', '')), ('nfs://server/path/to/file.txt', ('nfs', 'server', '/path/to/file.txt', '', '', ''), ('nfs', 'server', '/path/to/file.txt', '', '')), ('svn+ssh://svn.zope.org/repos/main/ZConfig/trunk/', ('svn+ssh', 'svn.zope.org', '/repos/main/ZConfig/trunk/', '', '', ''), ('svn+ssh', 'svn.zope.org', '/repos/main/ZConfig/trunk/', '', '')), ('git+ssh://git@github.com/user/project.git', ('git+ssh', 'git@github.com', '/user/project.git', '', '', ''), ('git+ssh', 'git@github.com', '/user/project.git', '', ''))]

    def _encode(t):
        return (t[0].encode('ascii'), tuple((x.encode('ascii') for x in t[1])), tuple((x.encode('ascii') for x in t[2])))
    bytes_cases = [_encode(x) for x in str_cases]
    for (url, parsed, split) in str_cases + bytes_cases:
        self.checkRoundtrips(url, parsed, split)
