# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: ListTest_test_list

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tio = io.TextIOWrapper(io.BytesIO(), 'ascii', newline='\n')
    with support.swap_attr(sys, 'stdout', tio):
        self.tar.list(verbose=False)
    out = tio.detach().getvalue()
    self.assertIn(b'ustar/conttype', out)
    self.assertIn(b'ustar/regtype', out)
    self.assertIn(b'ustar/lnktype', out)
    self.assertIn(b'ustar' + b'/12345' * 40 + b'67/longname', out)
    self.assertIn(b'./ustar/linktest2/symtype', out)
    self.assertIn(b'./ustar/linktest2/lnktype', out)
    self.assertIn(b'ustar/dirtype/', out)
    self.assertIn(b'ustar/dirtype-with-size/', out)

    def conv(b):
        s = b.decode(self.tar.encoding, 'surrogateescape')
        return s.encode('ascii', 'backslashreplace')
    self.assertIn(conv(b'ustar/umlauts-\xc4\xd6\xdc\xe4\xf6\xfc\xdf'), out)
    self.assertIn(conv(b'misc/regtype-hpux-signed-chksum-\xc4\xd6\xdc\xe4\xf6\xfc\xdf'), out)
    self.assertIn(conv(b'misc/regtype-old-v7-signed-chksum-\xc4\xd6\xdc\xe4\xf6\xfc\xdf'), out)
    self.assertIn(conv(b'pax/bad-pax-\xe4\xf6\xfc'), out)
    self.assertIn(conv(b'pax/hdrcharset-\xe4\xf6\xfc'), out)
    self.assertRegex(out, b'ustar/conttype ?\\r?\\nustar/regtype ?\\r?\\n')
    self.assertNotIn(b'link to', out)
    self.assertNotIn(b'->', out)
