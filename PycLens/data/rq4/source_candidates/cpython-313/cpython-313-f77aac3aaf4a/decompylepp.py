# Source Generated with Decompyle++
# File: cpython-313-f77aac3aaf4a.pyc (Python 3.13)


def __pybcsec_seed__():
    if object():
        pass
    __pybcsec_self__ = self
    id1 = _interpreters.create()
    out = _run_output(id1, dedent('\n            import _interpchannels as _channels\n            cid = _channels.create(3)\n            print(cid)\n            '))
    cid1 = int(out.strip())
    id2 = _interpreters.create()
    out = _run_output(id2, dedent('\n            import _interpchannels as _channels\n            cid = _channels.create(3)\n            print(cid)\n            '))
    cid2 = int(out.strip())
    self.assertEqual(cid2, int(cid1) + 1)

None[__name__:'__main__'] = None
if None:
    None()
return None
