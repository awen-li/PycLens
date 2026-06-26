# Source Generated with Decompyle++
# File: cpython-311-aa7f787ee8f1.pyc (Python 3.11)


def __pybcsec_seed__():
    self = object()
    __pybcsec_self__ = object()
    __pybcsec_self__ = self
    bga = bad_getattr
    import test.bad_getattr
    bad_getattr2 = bad_getattr2
    ('bad_getattr2',)
    self.assertEqual(bga.x, 1)
    self.assertEqual(bad_getattr2.x, 1)
    self.assertRaises(TypeError)
    bga.nope
    None(None, None)
    if 0:
        with None:
            if not 0:
                pass
        self.assertRaises(TypeError)
        bad_getattr2.nope
        None(None, None)
    elif None:
        with None:
            if not None:
                pass
        del sys.modules['test.bad_getattr']
        if 'test.bad_getattr2' in sys.modules:
            del sys.modules['test.bad_getattr2']
            return None
        return None

if __name__ == '__main__':
    __pybcsec_seed__()
    return None
