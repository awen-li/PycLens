# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementFindTest_test_findall_wildcard

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    root = ET.XML('\n            <a xmlns:x="X" xmlns:y="Y">\n                <x:b><c/></x:b>\n                <b/>\n                <c><x:b/><b/></c><y:b/>\n            </a>')
    root.append(ET.Comment('test'))
    self.assertEqual(summarize_list(root.findall('{*}b')), ['{X}b', 'b', '{Y}b'])
    self.assertEqual(summarize_list(root.findall('{*}c')), ['c'])
    self.assertEqual(summarize_list(root.findall('{X}*')), ['{X}b'])
    self.assertEqual(summarize_list(root.findall('{Y}*')), ['{Y}b'])
    self.assertEqual(summarize_list(root.findall('{}*')), ['b', 'c'])
    self.assertEqual(summarize_list(root.findall('{}b')), ['b'])
    self.assertEqual(summarize_list(root.findall('{}b')), summarize_list(root.findall('b')))
    self.assertEqual(summarize_list(root.findall('{*}*')), ['{X}b', 'b', 'c', '{Y}b'])
    self.assertEqual(summarize_list(root.findall('{*}*') + [root[-1]]), summarize_list(root.findall('*')))
    self.assertEqual(summarize_list(root.findall('.//{*}b')), ['{X}b', 'b', '{X}b', 'b', '{Y}b'])
    self.assertEqual(summarize_list(root.findall('.//{*}c')), ['c', 'c'])
    self.assertEqual(summarize_list(root.findall('.//{X}*')), ['{X}b', '{X}b'])
    self.assertEqual(summarize_list(root.findall('.//{Y}*')), ['{Y}b'])
    self.assertEqual(summarize_list(root.findall('.//{}*')), ['c', 'b', 'c', 'b'])
    self.assertEqual(summarize_list(root.findall('.//{}b')), ['b', 'b'])
    self.assertEqual(summarize_list(root.findall('.//{}b')), summarize_list(root.findall('.//b')))
