# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementTreeTest_test_tostring_xml_declaration_cases

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    elem = ET.XML('<body><tag>ø</tag></body>')
    TESTCASES = [(b'<body><tag>&#248;</tag></body>', None, None), (b'<body><tag>\xc3\xb8</tag></body>', 'UTF-8', None), (b'<body><tag>&#248;</tag></body>', 'US-ASCII', None), (b"<?xml version='1.0' encoding='ISO-8859-1'?>\n<body><tag>\xf8</tag></body>", 'ISO-8859-1', None), ('<body><tag>ø</tag></body>', 'unicode', None), (b'<body><tag>&#248;</tag></body>', None, False), (b'<body><tag>\xc3\xb8</tag></body>', 'UTF-8', False), (b'<body><tag>&#248;</tag></body>', 'US-ASCII', False), (b'<body><tag>\xf8</tag></body>', 'ISO-8859-1', False), ('<body><tag>ø</tag></body>', 'unicode', False), (b"<?xml version='1.0' encoding='us-ascii'?>\n<body><tag>&#248;</tag></body>", None, True), (b"<?xml version='1.0' encoding='UTF-8'?>\n<body><tag>\xc3\xb8</tag></body>", 'UTF-8', True), (b"<?xml version='1.0' encoding='US-ASCII'?>\n<body><tag>&#248;</tag></body>", 'US-ASCII', True), (b"<?xml version='1.0' encoding='ISO-8859-1'?>\n<body><tag>\xf8</tag></body>", 'ISO-8859-1', True), ("<?xml version='1.0' encoding='utf-8'?>\n<body><tag>ø</tag></body>", 'unicode', True)]
    for (expected_retval, encoding, xml_declaration) in TESTCASES:
        with self.subTest(f'encoding={encoding} xml_declaration={xml_declaration}'):
            self.assertEqual(ET.tostring(elem, encoding=encoding, xml_declaration=xml_declaration), expected_retval)
