# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: BugsTest_test_bug_200708_newline

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    e = ET.Element('SomeTag', text='def _f():\n  return 3\n')
    self.assertEqual(ET.tostring(e), b'<SomeTag text="def _f():&#10;  return 3&#10;" />')
    self.assertEqual(ET.XML(ET.tostring(e)).get('text'), 'def _f():\n  return 3\n')
    self.assertEqual(ET.tostring(ET.XML(ET.tostring(e))), b'<SomeTag text="def _f():&#10;  return 3&#10;" />')
