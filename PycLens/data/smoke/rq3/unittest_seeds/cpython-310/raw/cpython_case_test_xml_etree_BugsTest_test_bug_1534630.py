# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: BugsTest_test_bug_1534630

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    bob = ET.TreeBuilder()
    e = bob.data('data')
    e = bob.start('tag', {})
    e = bob.end('tag')
    e = bob.close()
    self.assertEqual(serialize(e), '<tag />')
