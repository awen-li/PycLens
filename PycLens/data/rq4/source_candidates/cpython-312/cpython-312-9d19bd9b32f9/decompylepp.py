# Source Generated with Decompyle++
# File: cpython-312-9d19bd9b32f9.pyc (Python 3.12)


def __pybcsec_seed__():
    self = object()
    __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = array.array(self.typecode, self.example) + array.array(self.typecode, self.example[::-1])
    self.assertEqual(a, array.array(self.typecode, self.example + self.example[::-1]))
    b = array.array(self.badtypecode())
    self.assertRaises(TypeError, a.__add__, b)
    self.assertRaises(TypeError, a.__add__, 'bad')

if __name__ == '__main__':
    __pybcsec_seed__()
    return None
