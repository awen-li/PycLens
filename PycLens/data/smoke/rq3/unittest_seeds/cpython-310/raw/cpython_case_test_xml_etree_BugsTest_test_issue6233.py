# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: BugsTest_test_issue6233

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    e = ET.XML(b"<?xml version='1.0' encoding='utf-8'?><body>t\xc3\xa3g</body>")
    self.assertEqual(ET.tostring(e, 'ascii'), b"<?xml version='1.0' encoding='ascii'?>\n<body>t&#227;g</body>")
    e = ET.XML(b"<?xml version='1.0' encoding='iso-8859-1'?><body>t\xe3g</body>")
    self.assertEqual(ET.tostring(e, 'ascii'), b"<?xml version='1.0' encoding='ascii'?>\n<body>t&#227;g</body>")
