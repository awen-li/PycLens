# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_property.py
# case: PropertyTests_test_property_decorator_doc_writable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class PropertyWritableDoc(object):

        @property
        def spam(self):
            """Eggs"""
            return 'eggs'
    sub = PropertyWritableDoc()
    self.assertEqual(sub.__class__.spam.__doc__, 'Eggs')
    sub.__class__.spam.__doc__ = 'Spam'
    self.assertEqual(sub.__class__.spam.__doc__, 'Spam')
