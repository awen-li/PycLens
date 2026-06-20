# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestDocString_test_docstring_deque_field_with_default_factory

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class C:
        x: deque = field(default_factory=deque)
    self.assertDocStrEqual(C.__doc__, 'C(x:collections.deque=<factory>)')
