# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: NamedTupleTests_test_namedtuple_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(TypeError):
        NamedTuple.__new__()
    with self.assertRaises(TypeError):
        NamedTuple()
    with self.assertRaises(TypeError):
        NamedTuple('Emp', [('name', str)], None)
    with self.assertRaises(ValueError):
        NamedTuple('Emp', [('_name', str)])
    with self.assertRaises(TypeError):
        NamedTuple(typename='Emp', name=str, id=int)
    with self.assertRaises(TypeError):
        NamedTuple('Emp', fields=[('name', str), ('id', int)])
