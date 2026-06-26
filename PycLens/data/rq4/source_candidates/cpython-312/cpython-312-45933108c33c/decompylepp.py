# Source Generated with Decompyle++
# File: cpython-312-45933108c33c.pyc (Python 3.12)


def __pybcsec_seed__():
    if None:
        pass
    self = object()
    __pybcsec_self__ = object()
    __pybcsec_self__ = self
    FFFD = '�'
    FFFDx2 = FFFD * 2
    sequences = [
        ('C2 00', FFFD + '\x00'),
        ('C2 7F', FFFD + '\x7f'),
        ('C2 C0', FFFDx2),
        ('C2 FF', FFFDx2),
        ('DF 00', FFFD + '\x00'),
        ('DF 7F', FFFD + '\x7f'),
        ('DF C0', FFFDx2),
        ('DF FF', FFFDx2)]
    for seq, res in sequences:
        self.assertCorrectUTF8Decoding(bytes.fromhex(seq), res, 'invalid continuation byte')

if __name__ == '__main__':
    __pybcsec_seed__()
    return None
