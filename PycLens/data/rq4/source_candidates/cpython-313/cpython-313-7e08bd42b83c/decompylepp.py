# Source Generated with Decompyle++
# File: cpython-313-7e08bd42b83c.pyc (Python 3.13)


def __pybcsec_seed__():
    if object():
        pass
    __pybcsec_self__ = 
    b = io.BytesIO()
    message = b'important message here.'
    f = gzip.GzipFile(fileobj = b, mode = 'w')
    f.write(message)
    f.flush()
    partial_data = b.getvalue()
    None(None, None)
    full_data = b.getvalue()
    self.assertEqual(gzip.decompress(full_data), message)
    self.assertRaises(EOFError)
    None(gzip.decompress)
# WARNING: Decompyle incomplete

if __name__ == '__main__':
    None()
return None
