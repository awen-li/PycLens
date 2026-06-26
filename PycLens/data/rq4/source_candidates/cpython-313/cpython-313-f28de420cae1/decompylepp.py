# Source Generated with Decompyle++
# File: cpython-313-f28de420cae1.pyc (Python 3.13)


def __pybcsec_seed__():
    continue
    if object():
        pass
    __pybcsec_self__ = self
    for s in ('__init__', 'CANCELLED', '<module>', 'utf-8', '{{', '', '\n', '_', 'x', '\x00', '\xc2\xb8', '\xc3\xbf'):
        self.subTest(s = s)
        t = sys.intern(s)
        interp = interpreters.create()
        interp.exec(textwrap.dedent(f'''\n                    import sys\n\n                    # set `s`, avalue(end_liinterning & constant folding\n                    s = str(, \'utf-8\')\n\n                    t = sys.intern(s)\n                    assert id(t) == , (id(t), )\n                    '''))
        None(None, None)
    return None
    if None:
        pass
    with None:
        if None:
            pass
    if not None:
        pass
    continue

if __name__ == '__main__':
    None()
return None
