# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pydoc.py
# case: PydocDocTest_test_builtin_with_more_than_four_children

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    doc = pydoc.TextDoc()
    text = doc.docclass(object)
    snip = ' |  Built-in subclasses:\n |      async_generator\n |      BaseException\n |      builtin_function_or_method\n |      bytearray\n |      ... and \\d+ other subclasses'
    self.assertRegex(text, snip)
