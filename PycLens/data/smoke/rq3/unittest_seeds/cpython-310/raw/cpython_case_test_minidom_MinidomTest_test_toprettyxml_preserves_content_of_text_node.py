# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_minidom.py
# case: MinidomTest_test_toprettyxml_preserves_content_of_text_node

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for str in ('<B>A</B>', '<A><B>C</B></A>'):
        dom = parseString(str)
        dom2 = parseString(dom.toprettyxml())
        self.assertEqual(dom.getElementsByTagName('B')[0].childNodes[0].toxml(), dom2.getElementsByTagName('B')[0].childNodes[0].toxml())
