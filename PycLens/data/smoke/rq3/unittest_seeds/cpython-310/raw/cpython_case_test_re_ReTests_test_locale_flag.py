# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_locale_flag

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    enc = locale.getpreferredencoding()
    for i in range(128, 256):
        try:
            c = bytes([i]).decode(enc)
            sletter = c.lower()
            if sletter == c:
                continue
            bletter = sletter.encode(enc)
            if len(bletter) != 1:
                continue
            if bletter.decode(enc) != sletter:
                continue
            bpat = re.escape(bytes([i]))
            break
        except (UnicodeError, TypeError):
            pass
    else:
        bletter = None
        bpat = b'A'
    pat = re.compile(bpat, re.LOCALE | re.IGNORECASE)
    if bletter:
        self.assertTrue(pat.match(bletter))
    pat = re.compile(b'(?L)' + bpat, re.IGNORECASE)
    if bletter:
        self.assertTrue(pat.match(bletter))
    pat = re.compile(bpat, re.IGNORECASE)
    if bletter:
        self.assertIsNone(pat.match(bletter))
    pat = re.compile(b'\\w', re.LOCALE)
    if bletter:
        self.assertTrue(pat.match(bletter))
    pat = re.compile(b'(?L)\\w')
    if bletter:
        self.assertTrue(pat.match(bletter))
    pat = re.compile(b'\\w')
    if bletter:
        self.assertIsNone(pat.match(bletter))
    self.assertRaises(ValueError, re.compile, '', re.LOCALE)
    self.assertRaises(re.error, re.compile, '(?L)')
    self.assertRaises(ValueError, re.compile, b'', re.LOCALE | re.ASCII)
    self.assertRaises(ValueError, re.compile, b'(?L)', re.ASCII)
    self.assertRaises(ValueError, re.compile, b'(?a)', re.LOCALE)
    self.assertRaises(re.error, re.compile, b'(?aL)')
