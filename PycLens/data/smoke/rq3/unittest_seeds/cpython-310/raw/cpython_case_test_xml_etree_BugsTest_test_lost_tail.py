# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: BugsTest_test_lost_tail

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Text:

        def __bool__(self):
            e[0].tail = 'changed'
            return True
    e = ET.Element('root')
    e.append(ET.Element('tag'))
    e[0].tail = Text()
    i = e.itertext()
    t = next(i)
    self.assertIsInstance(t, Text)
    self.assertIsInstance(e[0].tail, str)
    self.assertEqual(e[0].tail, 'changed')
