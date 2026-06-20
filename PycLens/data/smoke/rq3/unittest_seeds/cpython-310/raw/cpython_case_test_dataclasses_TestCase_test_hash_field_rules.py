# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_hash_field_rules

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (hash_, compare, result) in [(True, False, 'field'), (True, True, 'field'), (False, False, 'absent'), (False, True, 'absent'), (None, False, 'absent'), (None, True, 'field')]:
        with self.subTest(hash=hash_, compare=compare):

            @dataclass(unsafe_hash=True)
            class C:
                x: int = field(compare=compare, hash=hash_, default=5)
            if result == 'field':
                self.assertEqual(hash(C(5)), hash((5,)))
            elif result == 'absent':
                self.assertEqual(hash(C(5)), hash(()))
            else:
                assert False, f'unknown result {result!r}'
