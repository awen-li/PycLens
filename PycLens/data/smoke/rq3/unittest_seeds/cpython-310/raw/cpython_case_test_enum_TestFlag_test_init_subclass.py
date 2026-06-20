# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestFlag_test_init_subclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyEnum(Flag):

        def __init_subclass__(cls, **kwds):
            super().__init_subclass__(**kwds)
            self.assertFalse(cls.__dict__.get('_test', False))
            cls._test1 = 'MyEnum'

    class TheirEnum(MyEnum):

        def __init_subclass__(cls, **kwds):
            super(TheirEnum, cls).__init_subclass__(**kwds)
            cls._test2 = 'TheirEnum'

    class WhoseEnum(TheirEnum):

        def __init_subclass__(cls, **kwds):
            pass

    class NoEnum(WhoseEnum):
        ONE = 1
    self.assertEqual(TheirEnum.__dict__['_test1'], 'MyEnum')
    self.assertEqual(WhoseEnum.__dict__['_test1'], 'MyEnum')
    self.assertEqual(WhoseEnum.__dict__['_test2'], 'TheirEnum')
    self.assertFalse(NoEnum.__dict__.get('_test1', False))
    self.assertFalse(NoEnum.__dict__.get('_test2', False))

    class OurEnum(MyEnum):

        def __init_subclass__(cls, **kwds):
            cls._test2 = 'OurEnum'

    class WhereEnum(OurEnum):

        def __init_subclass__(cls, **kwds):
            pass

    class NeverEnum(WhereEnum):
        ONE = 1
    self.assertEqual(OurEnum.__dict__['_test1'], 'MyEnum')
    self.assertFalse(WhereEnum.__dict__.get('_test1', False))
    self.assertEqual(WhereEnum.__dict__['_test2'], 'OurEnum')
    self.assertFalse(NeverEnum.__dict__.get('_test1', False))
    self.assertFalse(NeverEnum.__dict__.get('_test2', False))
