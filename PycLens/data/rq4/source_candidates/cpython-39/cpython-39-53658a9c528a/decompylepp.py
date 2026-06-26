# Source Generated with Decompyle++
# File: cpython-39-53658a9c528a.pyc (Python 3.9)


def __pybcsec_seed__():
    self = __pybcsec_strue_ = object()
    __pybcsec_strue_ = self
    self.assertArgSpecEquals(mod.eggs, [
        'x',
        'y'], '(x, y)', **('formatted',))
    self.assertArgSpecEquals(mod.spam, [
        'a',
        'b',
        'c',
        'd',
        'e',
        'f'], 'g', 'h', (3, 4, 5), '(a, b, c, d=3, e=4, f=5, *g, **h)')
    self.assertRaises(ValueError, self.assertArgSpecEquals, mod2.keyworded, [])
    self.assertRaises(ValueError, self.assertArgSpecEquals, mod2.annotated, [])
    self.assertRaises(ValueError, self.assertArgSpecEquals, mod2.keyword_only_arg, [])

if __name__ == '__main__':
    __pybcsec_seed__()
