# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict.py
# case: DictTest_test_str_nonstr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class StrSub(str):
        pass
    eq_count = 0

    class Key3:

        def __hash__(self):
            return hash('key3')

        def __eq__(self, other):
            nonlocal eq_count
            if isinstance(other, Key3) or (isinstance(other, str) and other == 'key3'):
                eq_count += 1
                return True
            return False
    key3_1 = StrSub('key3')
    key3_2 = Key3()
    key3_3 = Key3()
    dicts = []
    for key3 in (key3_1, key3_2):
        dicts.append({'key1': 42, 'key2': 43, key3: 44})
        d = {'key1': 42, 'key2': 43}
        d[key3] = 44
        dicts.append(d)
        d = {'key1': 42, 'key2': 43}
        self.assertEqual(d.setdefault(key3, 44), 44)
        dicts.append(d)
        d = {'key1': 42, 'key2': 43}
        d.update({key3: 44})
        dicts.append(d)
        d = {'key1': 42, 'key2': 43}
        d |= {key3: 44}
        dicts.append(d)

        def make_pairs():
            yield ('key1', 42)
            yield ('key2', 43)
            yield (key3, 44)
        d = dict(make_pairs())
        dicts.append(d)
        d = d.copy()
        dicts.append(d)
        d = {key: 42 + i for (i, key) in enumerate(['key1', 'key2', key3])}
        dicts.append(d)
    for d in dicts:
        with self.subTest(d=d):
            self.assertEqual(d.get('key1'), 42)
            noninterned_key1 = 'ke'
            noninterned_key1 += 'y1'
            if support.check_impl_detail(cpython=True):
                interned_key1 = 'key1'
                self.assertFalse(noninterned_key1 is interned_key1)
            self.assertEqual(d.get(noninterned_key1), 42)
            self.assertEqual(d.get('key3'), 44)
            self.assertEqual(d.get(key3_1), 44)
            self.assertEqual(d.get(key3_2), 44)
            eq_count = 0
            self.assertEqual(d.get(key3_3), 44)
            self.assertGreaterEqual(eq_count, 1)
