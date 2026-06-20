# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: BugsTest_test_lost_elem

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Tag:

        def __eq__(self, other):
            e[0] = ET.Element('changed')
            next(i)
            return True
    e = ET.Element('root')
    e.append(ET.Element(Tag()))
    e.append(ET.Element('tag'))
    i = e.iter('tag')
    try:
        t = next(i)
    except ValueError:
        self.skipTest('generators are not reentrant')
    self.assertIsInstance(t.tag, Tag)
    self.assertIsInstance(e[0].tag, str)
    self.assertEqual(e[0].tag, 'changed')
