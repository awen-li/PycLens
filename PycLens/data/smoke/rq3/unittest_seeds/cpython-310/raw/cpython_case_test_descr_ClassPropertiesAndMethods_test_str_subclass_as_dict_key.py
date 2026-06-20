# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_str_subclass_as_dict_key

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class cistr(str):
        """Subclass of str that computes __eq__ case-insensitively.

            Also computes a hash code of the string in canonical form.
            """

        def __init__(self, value):
            self.canonical = value.lower()
            self.hashcode = hash(self.canonical)

        def __eq__(self, other):
            if not isinstance(other, cistr):
                other = cistr(other)
            return self.canonical == other.canonical

        def __hash__(self):
            return self.hashcode
    self.assertEqual(cistr('ABC'), 'abc')
    self.assertEqual('aBc', cistr('ABC'))
    self.assertEqual(str(cistr('ABC')), 'ABC')
    d = {cistr('one'): 1, cistr('two'): 2, cistr('tHree'): 3}
    self.assertEqual(d[cistr('one')], 1)
    self.assertEqual(d[cistr('tWo')], 2)
    self.assertEqual(d[cistr('THrEE')], 3)
    self.assertIn(cistr('ONe'), d)
    self.assertEqual(d.get(cistr('thrEE')), 3)
