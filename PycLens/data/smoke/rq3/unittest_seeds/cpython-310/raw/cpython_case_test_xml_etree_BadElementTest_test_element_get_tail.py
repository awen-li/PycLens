# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: BadElementTest_test_element_get_tail

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class X(str):

        def __del__(self):
            try:
                elem[0].tail
            except NameError:
                pass
    b = ET.TreeBuilder()
    b.start('root', {})
    b.start('tag', {})
    b.end('tag')
    b.data('ABCD')
    b.data(X('EFGH'))
    b.data('IJKL')
    b.end('root')
    elem = b.close()
    self.assertEqual(elem[0].tail, 'ABCDEFGHIJKL')
