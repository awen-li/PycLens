# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subclassinit.py
# case: Test_test_init_subclass_diamond

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Base:

        def __init_subclass__(cls, **kwargs):
            super().__init_subclass__(**kwargs)
            cls.calls = []

    class Left(Base):
        pass

    class Middle:

        def __init_subclass__(cls, middle, **kwargs):
            super().__init_subclass__(**kwargs)
            cls.calls += [middle]

    class Right(Base):

        def __init_subclass__(cls, right='right', **kwargs):
            super().__init_subclass__(**kwargs)
            cls.calls += [right]

    class A(Left, Middle, Right, middle='middle'):
        pass
    self.assertEqual(A.calls, ['right', 'middle'])
    self.assertEqual(Left.calls, [])
    self.assertEqual(Right.calls, [])
