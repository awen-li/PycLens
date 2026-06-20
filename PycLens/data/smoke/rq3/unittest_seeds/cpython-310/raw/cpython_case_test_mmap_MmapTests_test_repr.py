# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mmap.py
# case: MmapTests_test_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    open_mmap_repr_pat = re.compile('<mmap.mmap closed=False, access=(?P<access>\\S+), length=(?P<length>\\d+), pos=(?P<pos>\\d+), offset=(?P<offset>\\d+)>')
    closed_mmap_repr_pat = re.compile('<mmap.mmap closed=True>')
    mapsizes = (50, 100, 1000, 1000000, 10000000)
    offsets = tuple((mapsize // 2 // mmap.ALLOCATIONGRANULARITY * mmap.ALLOCATIONGRANULARITY for mapsize in mapsizes))
    for (offset, mapsize) in zip(offsets, mapsizes):
        data = b'a' * mapsize
        length = mapsize - offset
        accesses = ('ACCESS_DEFAULT', 'ACCESS_READ', 'ACCESS_COPY', 'ACCESS_WRITE')
        positions = (0, length // 10, length // 5, length // 4)
        with open(TESTFN, 'wb+') as fp:
            fp.write(data)
            fp.flush()
            for (access, pos) in itertools.product(accesses, positions):
                accint = getattr(mmap, access)
                with mmap.mmap(fp.fileno(), length, access=accint, offset=offset) as mm:
                    mm.seek(pos)
                    match = open_mmap_repr_pat.match(repr(mm))
                    self.assertIsNotNone(match)
                    self.assertEqual(match.group('access'), access)
                    self.assertEqual(match.group('length'), str(length))
                    self.assertEqual(match.group('pos'), str(pos))
                    self.assertEqual(match.group('offset'), str(offset))
                match = closed_mmap_repr_pat.match(repr(mm))
                self.assertIsNotNone(match)
