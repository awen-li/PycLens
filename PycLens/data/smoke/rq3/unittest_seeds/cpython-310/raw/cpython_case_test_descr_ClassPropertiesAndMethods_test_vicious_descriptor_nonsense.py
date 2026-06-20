# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_vicious_descriptor_nonsense

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Evil(object):

        def __hash__(self):
            return hash('attr')

        def __eq__(self, other):
            try:
                del C.attr
            except AttributeError:
                pass
            return 0

    class Descr(object):

        def __get__(self, ob, type=None):
            return 1

    class C(object):
        attr = Descr()
    c = C()
    c.__dict__[Evil()] = 0
    self.assertEqual(c.attr, 1)
    support.gc_collect()
    self.assertNotHasAttr(c, 'attr')
