# Source Generated with Decompyle++
# File: cpython-310-987b9fe188ce.pyc (Python 3.10)


def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    
    class S(str):
        pass

    s = S('xxx')
    self.assertEqual('%s' % s, '__str__ overridden')
    self.assertEqual('{}'.format(s), '__str__ overridden')

if __name__ == '__main__':
    __pybcsec_seed__()
    return None
