# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_minidom.py
# case: MinidomTest_test_toprettyxml_with_adjacent_text_nodes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    dom = Document()
    elem = dom.createElement('elem')
    elem.appendChild(dom.createTextNode('TEXT'))
    elem.appendChild(dom.createTextNode('TEXT'))
    dom.appendChild(elem)
    decl = '<?xml version="1.0" ?>\n'
    self.assertEqual(dom.toprettyxml(), decl + '<elem>\n\tTEXT\n\tTEXT\n</elem>\n')
