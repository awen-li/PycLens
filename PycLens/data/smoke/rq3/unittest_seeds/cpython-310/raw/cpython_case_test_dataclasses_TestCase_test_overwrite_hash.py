# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_overwrite_hash

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass(frozen=True)
    class C:
        x: int

        def __hash__(self):
            return 301
    self.assertEqual(hash(C(100)), 301)

    @dataclass(frozen=True)
    class C:
        x: int

        def __eq__(self, other):
            return False
    self.assertEqual(hash(C(100)), hash((100,)))
    with self.assertRaisesRegex(TypeError, 'Cannot overwrite attribute __hash__'):

        @dataclass(unsafe_hash=True)
        class C:

            def __hash__(self):
                pass

    @dataclass(unsafe_hash=True)
    class C:
        x: int

        def __eq__(self):
            pass
    self.assertEqual(hash(C(10)), hash((10,)))
    with self.assertRaisesRegex(TypeError, 'Cannot overwrite attribute __hash__'):

        @dataclass(unsafe_hash=True)
        class C:
            x: int

            def __eq__(self):
                pass

            def __hash__(self):
                pass
