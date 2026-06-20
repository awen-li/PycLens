# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pydoc.py
# case: PydocImportTest_test_importfile

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    loaded_pydoc = pydoc.importfile(pydoc.__file__)
    self.assertIsNot(loaded_pydoc, pydoc)
    self.assertEqual(loaded_pydoc.__name__, 'pydoc')
    self.assertEqual(loaded_pydoc.__file__, pydoc.__file__)
    self.assertEqual(loaded_pydoc.__spec__, pydoc.__spec__)
