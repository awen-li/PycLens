# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: BadElementTest_test_treebuilder_start

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def element_factory(x, y):
        return []
    b = ET.TreeBuilder(element_factory=element_factory)
    b.start('tag', {})
    b.data('ABCD')
    self.assertRaises(AttributeError, b.start, 'tag2', {})
    del b
    gc_collect()
