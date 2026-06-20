# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementTreeTest_test_tostringlist_xml_declaration

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    elem = ET.XML('<body><tag/></body>')
    self.assertEqual(''.join(ET.tostringlist(elem, encoding='unicode')), '<body><tag /></body>')
    self.assertEqual(b''.join(ET.tostringlist(elem, xml_declaration=True)), b"<?xml version='1.0' encoding='us-ascii'?>\n<body><tag /></body>")
    stringlist = ET.tostringlist(elem, encoding='unicode', xml_declaration=True)
    self.assertEqual(''.join(stringlist), "<?xml version='1.0' encoding='utf-8'?>\n<body><tag /></body>")
    self.assertRegex(stringlist[0], "^<\\?xml version='1.0' encoding='.+'?>")
    self.assertEqual(['<body', '>', '<tag', ' />', '</body>'], stringlist[1:])
