# Source Generated with Decompyle++
# File: cpython-312-d66de4f360b9.pyc (Python 3.12)


def __pybcsec_seed__():
    self = object()
    __pybcsec_self__ = object()
    __pybcsec_self__ = self
    trace = []
    
    def g():
        if None:
            pass
    # WARNING: Decompyle incomplete

    gi = g()
    next(gi)
    for x in range(3):
        y = gi.send(42)
        trace.append(f'''Should not have yielded: {y!s}''')
    self.fail('was able to send into non-generator')
    self.assertEqual(trace, [
        'starting g',
        'finishing g'])
    return None
    if None:
        pass
    if AttributeError:
        e = None
        self.assertIn('send', e.args[0])
        e = None
        del e
        continue
        e = None
        del e

if __name__ == '__main__':
    __pybcsec_seed__()
    return None
