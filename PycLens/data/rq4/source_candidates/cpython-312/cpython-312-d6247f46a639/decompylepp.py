# Source Generated with Decompyle++
# File: cpython-312-d6247f46a639.pyc (Python 3.12)


def __pybcsec_seed__():
    __pybcsec_self__ = object()
    __pybcsec_self__ = self
    name = 'my record'
    level = 13
    fn = None
    lno = None
    msg = None
    args = None
    exc_info = None
    func = None
    sinfo = None
    extra = {
        'valid_key': 'some value' }
    result = self.logger.makeRecord(name, level, fn, lno, msg, args, exc_info, extra = extra, sinfo = sinfo)
    self.assertIn('valid_key', result.__dict__)

if __name__ == '__main__':
    __pybcsec_seed__()
    return None
