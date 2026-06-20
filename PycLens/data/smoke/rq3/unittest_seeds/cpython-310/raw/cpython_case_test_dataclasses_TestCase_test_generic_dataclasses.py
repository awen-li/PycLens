# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_generic_dataclasses

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    T = TypeVar('T')

    @dataclass
    class LabeledBox(Generic[T]):
        content: T
        label: str = '<unknown>'
    box = LabeledBox(42)
    self.assertEqual(box.content, 42)
    self.assertEqual(box.label, '<unknown>')
    Alias = List[LabeledBox[int]]
