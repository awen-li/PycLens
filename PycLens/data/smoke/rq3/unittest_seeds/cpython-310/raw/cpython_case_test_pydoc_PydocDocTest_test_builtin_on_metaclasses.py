# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pydoc.py
# case: PydocDocTest_test_builtin_on_metaclasses

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    doc = pydoc.TextDoc()
    text = doc.docclass(type)
    self.assertNotIn('Built-in subclasses', text)
