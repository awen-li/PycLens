# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pydoc.py
# case: PydocDocTest_test_splitdoc_with_description

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    example_string = 'I Am A Doc\n\n\nHere is my description'
    self.assertEqual(pydoc.splitdoc(example_string), ('I Am A Doc', '\nHere is my description'))
