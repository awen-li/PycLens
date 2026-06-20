# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: PAXUnicodeTest_test_binary_header

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (encoding, name) in (('utf-8', 'pax/hdrcharset-\udce4\udcf6\udcfc'), ('iso8859-1', 'pax/hdrcharset-äöü')):
        with tarfile.open(tarname, encoding=encoding, errors='surrogateescape') as tar:
            try:
                t = tar.getmember(name)
            except KeyError:
                self.fail('unable to read POSIX.1-2008 binary header')
