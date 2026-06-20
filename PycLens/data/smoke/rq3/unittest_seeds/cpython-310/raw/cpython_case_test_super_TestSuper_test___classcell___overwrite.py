# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_super.py
# case: TestSuper_test___classcell___overwrite

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Meta(type):

        def __new__(cls, name, bases, namespace, cell):
            namespace['__classcell__'] = cell
            return super().__new__(cls, name, bases, namespace)
    for bad_cell in (None, 0, '', object()):
        with self.subTest(bad_cell=bad_cell):
            with self.assertRaises(TypeError):

                class A(metaclass=Meta, cell=bad_cell):
                    pass
