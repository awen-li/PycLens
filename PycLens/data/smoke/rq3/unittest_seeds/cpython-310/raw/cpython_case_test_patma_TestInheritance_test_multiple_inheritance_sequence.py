# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestInheritance_test_multiple_inheritance_sequence

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C:
        pass

    class S1(collections.UserList, collections.abc.Mapping):
        pass

    class S2(C, collections.UserList, collections.abc.Mapping):
        pass

    class S3(list, C, collections.abc.Mapping):
        pass

    class S4(collections.UserList, dict, C):
        pass
    self.assertEqual(self.check_sequence_then_mapping(S1()), 'seq')
    self.assertEqual(self.check_sequence_then_mapping(S2()), 'seq')
    self.assertEqual(self.check_sequence_then_mapping(S3()), 'seq')
    self.assertEqual(self.check_sequence_then_mapping(S4()), 'seq')
    self.assertEqual(self.check_mapping_then_sequence(S1()), 'seq')
    self.assertEqual(self.check_mapping_then_sequence(S2()), 'seq')
    self.assertEqual(self.check_mapping_then_sequence(S3()), 'seq')
    self.assertEqual(self.check_mapping_then_sequence(S4()), 'seq')
