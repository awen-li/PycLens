# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementTreeTest_test_encoding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def check(encoding, body=''):
        xml = "<?xml version='1.0' encoding='%s'?><xml>%s</xml>" % (encoding, body)
        self.assertEqual(ET.XML(xml.encode(encoding)).text, body)
        self.assertEqual(ET.XML(xml).text, body)
    check('ascii', 'a')
    check('us-ascii', 'a')
    check('iso-8859-1', '½')
    check('iso-8859-15', '€')
    check('cp437', '√')
    check('mac-roman', '˚')

    def xml(encoding):
        return "<?xml version='1.0' encoding='%s'?><xml />" % encoding

    def bxml(encoding):
        return xml(encoding).encode(encoding)
    supported_encodings = ['ascii', 'utf-8', 'utf-8-sig', 'utf-16', 'utf-16be', 'utf-16le', 'iso8859-1', 'iso8859-2', 'iso8859-3', 'iso8859-4', 'iso8859-5', 'iso8859-6', 'iso8859-7', 'iso8859-8', 'iso8859-9', 'iso8859-10', 'iso8859-13', 'iso8859-14', 'iso8859-15', 'iso8859-16', 'cp437', 'cp720', 'cp737', 'cp775', 'cp850', 'cp852', 'cp855', 'cp856', 'cp857', 'cp858', 'cp860', 'cp861', 'cp862', 'cp863', 'cp865', 'cp866', 'cp869', 'cp874', 'cp1006', 'cp1125', 'cp1250', 'cp1251', 'cp1252', 'cp1253', 'cp1254', 'cp1255', 'cp1256', 'cp1257', 'cp1258', 'mac-cyrillic', 'mac-greek', 'mac-iceland', 'mac-latin2', 'mac-roman', 'mac-turkish', 'iso2022-jp', 'iso2022-jp-1', 'iso2022-jp-2', 'iso2022-jp-2004', 'iso2022-jp-3', 'iso2022-jp-ext', 'koi8-r', 'koi8-t', 'koi8-u', 'kz1048', 'hz', 'ptcp154']
    for encoding in supported_encodings:
        self.assertEqual(ET.tostring(ET.XML(bxml(encoding))), b'<xml />')
    unsupported_ascii_compatible_encodings = ['big5', 'big5hkscs', 'cp932', 'cp949', 'cp950', 'euc-jp', 'euc-jis-2004', 'euc-jisx0213', 'euc-kr', 'gb2312', 'gbk', 'gb18030', 'iso2022-kr', 'johab', 'shift-jis', 'shift-jis-2004', 'shift-jisx0213', 'utf-7']
    for encoding in unsupported_ascii_compatible_encodings:
        self.assertRaises(ValueError, ET.XML, bxml(encoding))
    unsupported_ascii_incompatible_encodings = ['cp037', 'cp424', 'cp500', 'cp864', 'cp875', 'cp1026', 'cp1140', 'utf_32', 'utf_32_be', 'utf_32_le']
    for encoding in unsupported_ascii_incompatible_encodings:
        self.assertRaises(ET.ParseError, ET.XML, bxml(encoding))
    self.assertRaises(ValueError, ET.XML, xml('undefined').encode('ascii'))
    self.assertRaises(LookupError, ET.XML, xml('xxx').encode('ascii'))
