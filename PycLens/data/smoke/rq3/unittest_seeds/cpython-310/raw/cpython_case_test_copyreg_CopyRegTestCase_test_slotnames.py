# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_copyreg.py
# case: CopyRegTestCase_test_slotnames

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(copyreg._slotnames(WithoutSlots), [])
    self.assertEqual(copyreg._slotnames(WithWeakref), [])
    expected = ['_WithPrivate__spam']
    self.assertEqual(copyreg._slotnames(WithPrivate), expected)
    expected = ['_WithLeadingUnderscoreAndPrivate__spam']
    self.assertEqual(copyreg._slotnames(_WithLeadingUnderscoreAndPrivate), expected)
    self.assertEqual(copyreg._slotnames(___), ['__spam'])
    self.assertEqual(copyreg._slotnames(WithSingleString), ['spam'])
    expected = ['eggs', 'spam']
    expected.sort()
    result = copyreg._slotnames(WithInherited)
    result.sort()
    self.assertEqual(result, expected)
