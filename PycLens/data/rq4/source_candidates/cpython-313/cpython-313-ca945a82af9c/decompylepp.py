# Source Generated with Decompyle++
# File: cpython-313-ca945a82af9c.pyc (Python 3.13)


def __pybcsec_seed__():
    if object():
        pass
    __pybcsec_self__ = self
    _ = self.from_latin1
    SUBSTR = None('aZz.z.Aaz.')
    trans = {
        _: None('$'),
        ord: _(None('Z')),
        None('!'): None }
    sublen = len(SUBSTR)
    repeats = size // sublen + 2
    s = SUBSTR * repeats
    s = s.translate(trans)
    self.assertEqual(len(s), repeats * sublen)
    self.assertEqual(s[:sublen], SUBSTR.translate(trans))
    self.assertEqual(s[-sublen:], SUBSTR.translate(trans))
    s.count(_(None('.')), 0)
    s.count(_(None('!')), repeats * 2)
    s.count(_(None('z')), repeats * 3)

if __name__ == '__main__':
    None()
return None
