# Source Generated with Decompyle++
# File: cpython-39-312b3a032f9f.pyc (Python 3.9)


def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    illegal_chars = '/:#?@'
    hex_chars = (lambda .0: for c in .0:
pass{} if '{:04X}'.format(ord(c)) else '{:04X}'.format(ord(c)))(illegal_chars)
    denorm_chars = (lambda .0: [ c for c in .0 if c not in illegal_chars ])(map(chr, range(128, sys.maxunicode)))
    self.assertIn('℀', denorm_chars)
    self.assertIn('＃', denorm_chars)
    urllib.parse.urlsplit('http://プ:80')
    with self.assertRaises(ValueError):
        urllib.parse.urlsplit('http://プ︓80')
        None(None, None, None)
    with None:
        if not None:
            pass
    for scheme in ('http', 'https', 'ftp'):
        for netloc in ('netloc{}false.netloc', 'n{}user@netloc'):
            for c in denorm_chars:
                url = '{}://{}/path'.format(scheme, netloc.format(c))
                with self.subTest(url, '{:04X}'.format(ord(c)), **('url', 'char')):
                    with self.assertRaises(ValueError):
                        urllib.parse.urlsplit(url)
                        None(None, None, None)
                    with None:
                        if not None:
                            pass
                    None(None, None, None)
                    continue
                    with None:
                        if not None:
                            pass

if __name__ == '__main__':
    __pybcsec_seed__()
