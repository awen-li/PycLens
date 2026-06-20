# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_richcmp.py
# case: DictTest_test_dicts

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import random
    imag1a = {}
    for i in range(50):
        imag1a[random.randrange(100) * 1j] = random.randrange(100) * 1j
    items = list(imag1a.items())
    random.shuffle(items)
    imag1b = {}
    for (k, v) in items:
        imag1b[k] = v
    imag2 = imag1b.copy()
    imag2[k] = v + 1.0
    self.assertEqual(imag1a, imag1a)
    self.assertEqual(imag1a, imag1b)
    self.assertEqual(imag2, imag2)
    self.assertTrue(imag1a != imag2)
    for opname in ('lt', 'le', 'gt', 'ge'):
        for op in opmap[opname]:
            self.assertRaises(TypeError, op, imag1a, imag2)
