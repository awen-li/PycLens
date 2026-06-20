# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exceptions.py
# case: ExceptionTests_test_exception_with_doc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import _testcapi
    doc2 = 'This is a test docstring.'
    doc4 = 'This is another test docstring.'
    self.assertRaises(SystemError, _testcapi.make_exception_with_doc, 'error1')
    error1 = _testcapi.make_exception_with_doc('_testcapi.error1')
    self.assertIs(type(error1), type)
    self.assertTrue(issubclass(error1, Exception))
    self.assertIsNone(error1.__doc__)
    error2 = _testcapi.make_exception_with_doc('_testcapi.error2', doc2)
    self.assertEqual(error2.__doc__, doc2)
    error3 = _testcapi.make_exception_with_doc('_testcapi.error3', base=error2)
    self.assertTrue(issubclass(error3, error2))

    class C(object):
        pass
    error4 = _testcapi.make_exception_with_doc('_testcapi.error4', doc4, (error3, C))
    self.assertTrue(issubclass(error4, error3))
    self.assertTrue(issubclass(error4, C))
    self.assertEqual(error4.__doc__, doc4)
    error5 = _testcapi.make_exception_with_doc('_testcapi.error5', '', error4, {'a': 1})
    self.assertTrue(issubclass(error5, error4))
    self.assertEqual(error5.a, 1)
    self.assertEqual(error5.__doc__, '')
