# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestInheritance_test_late_registration_mapping

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Parent:
        pass

    class ChildPre(Parent):
        pass

    class GrandchildPre(ChildPre):
        pass
    collections.abc.Mapping.register(Parent)

    class ChildPost(Parent):
        pass

    class GrandchildPost(ChildPost):
        pass
    self.assertEqual(self.check_sequence_then_mapping(Parent()), 'map')
    self.assertEqual(self.check_sequence_then_mapping(ChildPre()), 'map')
    self.assertEqual(self.check_sequence_then_mapping(GrandchildPre()), 'map')
    self.assertEqual(self.check_sequence_then_mapping(ChildPost()), 'map')
    self.assertEqual(self.check_sequence_then_mapping(GrandchildPost()), 'map')
    self.assertEqual(self.check_mapping_then_sequence(Parent()), 'map')
    self.assertEqual(self.check_mapping_then_sequence(ChildPre()), 'map')
    self.assertEqual(self.check_mapping_then_sequence(GrandchildPre()), 'map')
    self.assertEqual(self.check_mapping_then_sequence(ChildPost()), 'map')
    self.assertEqual(self.check_mapping_then_sequence(GrandchildPost()), 'map')
