# Source Generated with Decompyle++
# File: cpython-39-88287aed8f89.pyc (Python 3.9)


def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    nameprep = nameprep
    import encodings.idna
    for orig, prepped in enumerate(nameprep_tests):
        if orig is None:
            continue
        orig = str(orig, 'utf-8', 'surrogatepass')
        if prepped is None:
            self.assertRaises(UnicodeError, nameprep, orig)
            continue
        prepped = str(prepped, 'utf-8', 'surrogatepass')
        
        try:
            self.assertEqual(nameprep(orig), prepped)
        finally:
            continue
            if Exception:
                e = None
                
                try:
                    raise support.TestFailed('Test 3.%d: %s' % (pos + 1, str(e)))
                finally:
                    e = None
                    del e
                    continue
                    e = None
                    del e
                    continue
                    return None



if __name__ == '__main__':
    __pybcsec_seed__()
