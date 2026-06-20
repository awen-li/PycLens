# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: UnicodeTest_test_uname_unicode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    t = tarfile.TarInfo('foo')
    t.uname = 'äöü'
    t.gname = 'äöü'
    tar = tarfile.open(tmpname, mode='w', format=self.format, encoding='iso8859-1')
    try:
        tar.addfile(t)
    finally:
        tar.close()
    tar = tarfile.open(tmpname, encoding='iso8859-1')
    try:
        t = tar.getmember('foo')
        self.assertEqual(t.uname, 'äöü')
        self.assertEqual(t.gname, 'äöü')
        if self.format != tarfile.PAX_FORMAT:
            tar.close()
            tar = tarfile.open(tmpname, encoding='ascii')
            t = tar.getmember('foo')
            self.assertEqual(t.uname, '\udce4\udcf6\udcfc')
            self.assertEqual(t.gname, '\udce4\udcf6\udcfc')
    finally:
        tar.close()
