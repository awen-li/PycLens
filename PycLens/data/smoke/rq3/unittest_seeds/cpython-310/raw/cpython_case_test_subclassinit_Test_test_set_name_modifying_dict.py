# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subclassinit.py
# case: Test_test_set_name_modifying_dict

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    notified = []

    class Descriptor:

        def __set_name__(self, owner, name):
            setattr(owner, name + 'x', None)
            notified.append(name)

    class A:
        a = Descriptor()
        b = Descriptor()
        c = Descriptor()
        d = Descriptor()
        e = Descriptor()
    self.assertCountEqual(notified, ['a', 'b', 'c', 'd', 'e'])
