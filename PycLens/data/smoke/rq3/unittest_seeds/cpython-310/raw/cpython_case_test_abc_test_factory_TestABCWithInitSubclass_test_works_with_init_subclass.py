# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_abc.py
# case: test_factory_TestABCWithInitSubclass_test_works_with_init_subclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class abc_ABC(metaclass=abc_ABCMeta):
        __slots__ = ()
    saved_kwargs = {}

    class ReceivesClassKwargs:

        def __init_subclass__(cls, **kwargs):
            super().__init_subclass__()
            saved_kwargs.update(kwargs)

    class Receiver(ReceivesClassKwargs, abc_ABC, x=1, y=2, z=3):
        pass
    self.assertEqual(saved_kwargs, dict(x=1, y=2, z=3))
