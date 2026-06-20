# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pydoc.py
# case: PydocDocTest_test_builtin_with_grandchild

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    doc = pydoc.TextDoc()
    text = doc.docclass(Exception)
    snip = ' |  Built-in subclasses:\n |      ArithmeticError\n |      AssertionError\n |      AttributeError'
    self.assertIn(snip, text)
    self.assertNotIn('ZeroDivisionError', text)
