# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: BugsTest_test_lost_text

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Text:

        def __bool__(self):
            e.text = 'changed'
            return True
    e = ET.Element('tag')
    e.text = Text()
    i = e.itertext()
    t = next(i)
    self.assertIsInstance(t, Text)
    self.assertIsInstance(e.text, str)
    self.assertEqual(e.text, 'changed')
