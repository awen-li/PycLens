# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_plistlib.py
# case: TestPlistlib_test_xml_encodings

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    base = TESTDATA[plistlib.FMT_XML]
    for (xml_encoding, encoding, bom) in [(b'utf-8', 'utf-8', codecs.BOM_UTF8), (b'utf-16', 'utf-16-le', codecs.BOM_UTF16_LE), (b'utf-16', 'utf-16-be', codecs.BOM_UTF16_BE)]:
        pl = self._create(fmt=plistlib.FMT_XML)
        with self.subTest(encoding=encoding):
            data = base.replace(b'UTF-8', xml_encoding)
            data = bom + data.decode('utf-8').encode(encoding)
            pl2 = plistlib.loads(data)
            self.assertEqual(dict(pl), dict(pl2))
