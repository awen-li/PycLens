# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: BugsTest_test_bug_xmltoolkit63

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def xmltoolkit63():
        tree = ET.TreeBuilder()
        tree.start('tag', {})
        tree.data('text')
        tree.end('tag')
    xmltoolkit63()
    count = sys.getrefcount(None)
    for i in range(1000):
        xmltoolkit63()
    self.assertEqual(sys.getrefcount(None), count)
