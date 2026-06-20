# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ucn.py
# case: UnicodeNamesTest_test_named_sequences_full

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def check_version(testfile):
        hdr = testfile.readline()
        return unicodedata.unidata_version in hdr
    url = 'http://www.pythontest.net/unicode/%s/NamedSequences.txt' % unicodedata.unidata_version
    try:
        testdata = support.open_urlresource(url, encoding='utf-8', check=check_version)
    except (OSError, HTTPException):
        self.skipTest('Could not retrieve ' + url)
    self.addCleanup(testdata.close)
    for line in testdata:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        (seqname, codepoints) = line.split(';')
        codepoints = ''.join((chr(int(cp, 16)) for cp in codepoints.split()))
        self.assertEqual(unicodedata.lookup(seqname), codepoints)
        with self.assertRaises(SyntaxError):
            self.checkletter(seqname, None)
        with self.assertRaises(KeyError):
            unicodedata.ucd_3_2_0.lookup(seqname)
