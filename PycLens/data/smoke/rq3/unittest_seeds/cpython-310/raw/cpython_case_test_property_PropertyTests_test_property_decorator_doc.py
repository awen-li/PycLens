# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_property.py
# case: PropertyTests_test_property_decorator_doc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    base = PropertyDocBase()
    sub = PropertyDocSub()
    self.assertEqual(base.__class__.spam.__doc__, 'spam spam spam')
    self.assertEqual(sub.__class__.spam.__doc__, 'spam spam spam')
