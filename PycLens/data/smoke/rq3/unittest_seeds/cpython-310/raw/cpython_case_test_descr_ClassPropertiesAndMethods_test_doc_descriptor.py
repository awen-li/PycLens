# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_doc_descriptor

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class DocDescr(object):

        def __get__(self, object, otype):
            if object:
                object = object.__class__.__name__ + ' instance'
            if otype:
                otype = otype.__name__
            return 'object=%s; type=%s' % (object, otype)

    class OldClass:
        __doc__ = DocDescr()

    class NewClass(object):
        __doc__ = DocDescr()
    self.assertEqual(OldClass.__doc__, 'object=None; type=OldClass')
    self.assertEqual(OldClass().__doc__, 'object=OldClass instance; type=OldClass')
    self.assertEqual(NewClass.__doc__, 'object=None; type=NewClass')
    self.assertEqual(NewClass().__doc__, 'object=NewClass instance; type=NewClass')
