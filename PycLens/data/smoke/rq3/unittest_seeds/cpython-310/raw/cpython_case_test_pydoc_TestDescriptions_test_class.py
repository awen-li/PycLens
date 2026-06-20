# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pydoc.py
# case: TestDescriptions_test_class

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C:
        """New-style class"""
    c = C()
    self.assertEqual(pydoc.describe(C), 'class C')
    self.assertEqual(pydoc.describe(c), 'C')
    expected = 'C in module %s object' % __name__
    self.assertIn(expected, pydoc.render_doc(c))
