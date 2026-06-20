# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: BasicSocketTests_test_parse_all_sans

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = ssl._ssl._test_decode_cert(ALLSANFILE)
    self.assertEqual(p['subjectAltName'], (('DNS', 'allsans'), ('othername', '<unsupported>'), ('othername', '<unsupported>'), ('email', 'user@example.org'), ('DNS', 'www.example.org'), ('DirName', ((('countryName', 'XY'),), (('localityName', 'Castle Anthrax'),), (('organizationName', 'Python Software Foundation'),), (('commonName', 'dirname example'),))), ('URI', 'https://www.python.org/'), ('IP Address', '127.0.0.1'), ('IP Address', '0:0:0:0:0:0:0:1'), ('Registered ID', '1.2.3.4.5')))
