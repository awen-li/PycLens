# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_minidom.py
# case: MinidomTest_test_toprettyxml_with_text_nodes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    decl = '<?xml version="1.0" ?>\n'
    self.assertEqual(parseString('<B>A</B>').toprettyxml(), decl + '<B>A</B>\n')
    self.assertEqual(parseString('<C>A<B>A</B></C>').toprettyxml(), decl + '<C>\n\tA\n\t<B>A</B>\n</C>\n')
    self.assertEqual(parseString('<C><B>A</B>A</C>').toprettyxml(), decl + '<C>\n\t<B>A</B>\n\tA\n</C>\n')
    self.assertEqual(parseString('<C><B>A</B><B>A</B></C>').toprettyxml(), decl + '<C>\n\t<B>A</B>\n\t<B>A</B>\n</C>\n')
    self.assertEqual(parseString('<C><B>A</B>A<B>A</B></C>').toprettyxml(), decl + '<C>\n\t<B>A</B>\n\tA\n\t<B>A</B>\n</C>\n')
