# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_dict_constructors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = dict()
    self.assertEqual(d, {})
    d = dict({})
    self.assertEqual(d, {})
    d = dict({1: 2, 'a': 'b'})
    self.assertEqual(d, {1: 2, 'a': 'b'})
    self.assertEqual(d, dict(list(d.items())))
    self.assertEqual(d, dict(iter(d.items())))
    d = dict({'one': 1, 'two': 2})
    self.assertEqual(d, dict(one=1, two=2))
    self.assertEqual(d, dict(**d))
    self.assertEqual(d, dict({'one': 1}, two=2))
    self.assertEqual(d, dict([('two', 2)], one=1))
    self.assertEqual(d, dict([('one', 100), ('two', 200)], **d))
    self.assertEqual(d, dict(**d))
    for badarg in (0, 0, 0j, '0', [0], (0,)):
        try:
            dict(badarg)
        except TypeError:
            pass
        except ValueError:
            if badarg == '0':
                pass
            else:
                self.fail('no TypeError from dict(%r)' % badarg)
        else:
            self.fail('no TypeError from dict(%r)' % badarg)
    try:
        dict({}, {})
    except TypeError:
        pass
    else:
        self.fail('no TypeError from dict({}, {})')

    class Mapping:
        dict = {1: 2, 3: 4, 'a': 1j}
    try:
        dict(Mapping())
    except TypeError:
        pass
    else:
        self.fail('no TypeError from dict(incomplete mapping)')
    Mapping.keys = lambda self: list(self.dict.keys())
    Mapping.__getitem__ = lambda self, i: self.dict[i]
    d = dict(Mapping())
    self.assertEqual(d, Mapping.dict)

    class AddressBookEntry:

        def __init__(self, first, last):
            self.first = first
            self.last = last

        def __iter__(self):
            return iter([self.first, self.last])
    d = dict([AddressBookEntry('Tim', 'Warsaw'), AddressBookEntry('Barry', 'Peters'), AddressBookEntry('Tim', 'Peters'), AddressBookEntry('Barry', 'Warsaw')])
    self.assertEqual(d, {'Barry': 'Warsaw', 'Tim': 'Peters'})
    d = dict(zip(range(4), range(1, 5)))
    self.assertEqual(d, dict([(i, i + 1) for i in range(4)]))
    for bad in ([('tooshort',)], [('too', 'long', 'by 1')]):
        try:
            dict(bad)
        except ValueError:
            pass
        else:
            self.fail('no ValueError from dict(%r)' % bad)
