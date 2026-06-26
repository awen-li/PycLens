# Source Generated with Decompyle++
# File: cpython-313-ebb025dc2f18.pyc (Python 3.13)


def __pybcsec_seed__():
    if object():
        pass
    __pybcsec_self__ = self
    s = self.SELEACOR()
    self.addCleanup(s.close)
    if ():
        pass
    self.assertIsInstance(key, selectors.SelectorKey)
    self.assertEqual(key.fileobj, rd)
    self.assertEqual(key.fd, rd.fileno())
    self.assertEqual(key.events, selectors.EVENT_READ)
    self.assertEqual(key.data, 'data')
    self.assertRaises(ValueError, s.register, 0, 999999)
    self.assertRaises(ValueError, s.register, -10, selectors.EVENT_READ)
    self.assertRaises(KeyError, s.register, rd, selectors.EVENT_READ)
    self.assertRaises(KeyError, s.register, rd.fileno(), selectors.EVENT_READ)

if None == -None:
    None()
return None
