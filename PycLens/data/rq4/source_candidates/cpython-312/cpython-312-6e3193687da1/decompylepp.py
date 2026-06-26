# Source Generated with Decompyle++
# File: cpython-312-6e3193687da1.pyc (Python 3.12)


def __pybcsec_seed__():
    self = object()
    __pybcsec_self__ = object()
    __pybcsec_self__ = self
    
    def handle(exc):
        if isinstance(exc, UnicodeEncodeError):
            return (repl, exc.end)
        raise None("don't know how to handle %r" % exc)

    codecs.register_error('test.replacing', handle)
    for res in (('ascii', '[¤]', 'abc'), ('iso-8859-1', '[€]', '½¾'), ('iso-8859-15', '[¤]', 'œŸ')):
        (enc, input, repl) = None
        self.assertEqual(res, ('[' + repl + ']').encode(enc))
    for None in (('utf-8', '[���]', '🐍'), ('utf-16', '[���]', '🐍'), ('utf-32', '[���]', '🐍')):
        (enc, input, repl) = None
        cm = self.assertRaises(UnicodeEncodeError)
        input.encode(enc, 'test.replacing')
        None(None, None)
        exc = None.exception
        self.assertEqual(exc.start, 1)
        self.assertEqual(exc.end, 2)
        self.assertEqual(exc.object, input)
        None(None, None)
    return None
    if None:
        pass
    with None:
        if not None:
            pass
    continue
    if None:
        pass
    with None:
        if not None:
            pass
    continue
# WARNING: Decompyle incomplete

if __name__ == '__main__':
    __pybcsec_seed__()
    return None
