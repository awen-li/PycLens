# Source Generated with Decompyle++
# File: cpython-312-eb581a73e180.pyc (Python 3.12)


def __pybcsec_seed__():
    self = object()
    __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = bytearray(b'hello')
    b.remove(ord('l'))
    self.assertEqual(b, b'helo')
    b.remove(ord('l'))
    self.assertEqual(b, b'heo')
    None(self.assertRaises, (lambda : b.remove(ord('l'))))
    None(self.assertRaises, (lambda : b.remove(400)))
    None(self.assertRaises, (lambda : b.remove('e')))
    b.remove(ord('o'))
    b.remove(ord('h'))
    self.assertEqual(b, b'e')
    None(self.assertRaises, (lambda : b.remove(b'e')))
    b.remove(Indexable(ord('e')))
    self.assertEqual(b, b'')
    c = bytearray([
        126,
        127,
        128,
        129])
    c.remove(127)
    self.assertEqual(c, bytes([
        126,
        128,
        129]))
    c.remove(129)
    self.assertEqual(c, bytes([
        126,
        128]))
# WARNING: Decompyle incomplete

if __name__ == '__main__':
    __pybcsec_seed__()
    return None
