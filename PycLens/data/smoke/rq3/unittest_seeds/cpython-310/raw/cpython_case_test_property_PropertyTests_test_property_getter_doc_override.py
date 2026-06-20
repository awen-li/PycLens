# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_property.py
# case: PropertyTests_test_property_getter_doc_override

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    newgettersub = PropertySubNewGetter()
    self.assertEqual(newgettersub.spam, 5)
    self.assertEqual(newgettersub.__class__.spam.__doc__, 'new docstring')
    newgetter = PropertyNewGetter()
    self.assertEqual(newgetter.spam, 8)
    self.assertEqual(newgetter.__class__.spam.__doc__, 'new docstring')
