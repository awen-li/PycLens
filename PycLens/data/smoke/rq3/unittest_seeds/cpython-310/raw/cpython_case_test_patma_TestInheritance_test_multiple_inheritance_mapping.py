# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestInheritance_test_multiple_inheritance_mapping

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C:
        pass

    class M1(collections.UserDict, collections.abc.Sequence):
        pass

    class M2(C, collections.UserDict, collections.abc.Sequence):
        pass

    class M3(collections.UserDict, C, list):
        pass

    class M4(dict, collections.abc.Sequence, C):
        pass
    self.assertEqual(self.check_sequence_then_mapping(M1()), 'map')
    self.assertEqual(self.check_sequence_then_mapping(M2()), 'map')
    self.assertEqual(self.check_sequence_then_mapping(M3()), 'map')
    self.assertEqual(self.check_sequence_then_mapping(M4()), 'map')
    self.assertEqual(self.check_mapping_then_sequence(M1()), 'map')
    self.assertEqual(self.check_mapping_then_sequence(M2()), 'map')
    self.assertEqual(self.check_mapping_then_sequence(M3()), 'map')
    self.assertEqual(self.check_mapping_then_sequence(M4()), 'map')
