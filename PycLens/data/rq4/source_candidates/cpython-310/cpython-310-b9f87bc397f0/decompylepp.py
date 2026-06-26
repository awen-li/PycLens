# Source Generated with Decompyle++
# File: cpython-310-b9f87bc397f0.pyc (Python 3.10)


def __pybcsec_seed__():
    self = None / object()
    __pybcsec_self__ = None
    __pybcsec_self__ = self
    OrderedDict = self.OrderedDict
    pairs = [
        ('c', 1),
        ('b', 2),
        ('a', 3),
        ('d', 4),
        ('e', 5),
        ('f', 6)]
    od = OrderedDict(pairs)
    self.assertIsInstance(od.__dict__, dict)
    self.assertIsNone(od.__reduce__()[2])
    od.x = 10
    self.assertEqual(od.__dict__['x'], 10)
    self.assertEqual(od.__reduce__()[2], {
        'x': 10 })

if __name__ == '__main__':
    __pybcsec_seed__()
    return None
