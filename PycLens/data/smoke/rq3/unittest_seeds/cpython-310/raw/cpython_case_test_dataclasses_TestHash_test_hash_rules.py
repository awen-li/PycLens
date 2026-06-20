# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestHash_test_hash_rules

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def non_bool(value):
        if value is None:
            return None
        if value:
            return (3,)
        return 0

    def test(case, unsafe_hash, eq, frozen, with_hash, result):
        with self.subTest(case=case, unsafe_hash=unsafe_hash, eq=eq, frozen=frozen):
            if result != 'exception':
                if with_hash:

                    @dataclass(unsafe_hash=unsafe_hash, eq=eq, frozen=frozen)
                    class C:

                        def __hash__(self):
                            return 0
                else:

                    @dataclass(unsafe_hash=unsafe_hash, eq=eq, frozen=frozen)
                    class C:
                        pass
            if result == 'fn':
                self.assertIn('__hash__', C.__dict__)
                self.assertIsNotNone(C.__dict__['__hash__'])
            elif result == '':
                if not with_hash:
                    self.assertNotIn('__hash__', C.__dict__)
            elif result == 'none':
                self.assertIn('__hash__', C.__dict__)
                self.assertIsNone(C.__dict__['__hash__'])
            elif result == 'exception':
                assert with_hash
                with self.assertRaisesRegex(TypeError, 'Cannot overwrite attribute __hash__'):

                    @dataclass(unsafe_hash=unsafe_hash, eq=eq, frozen=frozen)
                    class C:

                        def __hash__(self):
                            return 0
            else:
                assert False, f'unknown result {result!r}'
    for (case, (unsafe_hash, eq, frozen, res_no_defined_hash, res_defined_hash)) in enumerate([(False, False, False, '', ''), (False, False, True, '', ''), (False, True, False, 'none', ''), (False, True, True, 'fn', ''), (True, False, False, 'fn', 'exception'), (True, False, True, 'fn', 'exception'), (True, True, False, 'fn', 'exception'), (True, True, True, 'fn', 'exception')], 1):
        test(case, unsafe_hash, eq, frozen, False, res_no_defined_hash)
        test(case, unsafe_hash, eq, frozen, True, res_defined_hash)
        test(case, non_bool(unsafe_hash), non_bool(eq), non_bool(frozen), False, res_no_defined_hash)
        test(case, non_bool(unsafe_hash), non_bool(eq), non_bool(frozen), True, res_defined_hash)
