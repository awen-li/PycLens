# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestInheritance_test_late_registration_sequence

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Parent:
        pass

    class ChildPre(Parent):
        pass

    class GrandchildPre(ChildPre):
        pass
    collections.abc.Sequence.register(Parent)

    class ChildPost(Parent):
        pass

    class GrandchildPost(ChildPost):
        pass
    self.assertEqual(self.check_sequence_then_mapping(Parent()), 'seq')
    self.assertEqual(self.check_sequence_then_mapping(ChildPre()), 'seq')
    self.assertEqual(self.check_sequence_then_mapping(GrandchildPre()), 'seq')
    self.assertEqual(self.check_sequence_then_mapping(ChildPost()), 'seq')
    self.assertEqual(self.check_sequence_then_mapping(GrandchildPost()), 'seq')
    self.assertEqual(self.check_mapping_then_sequence(Parent()), 'seq')
    self.assertEqual(self.check_mapping_then_sequence(ChildPre()), 'seq')
    self.assertEqual(self.check_mapping_then_sequence(GrandchildPre()), 'seq')
    self.assertEqual(self.check_mapping_then_sequence(ChildPost()), 'seq')
    self.assertEqual(self.check_mapping_then_sequence(GrandchildPost()), 'seq')
