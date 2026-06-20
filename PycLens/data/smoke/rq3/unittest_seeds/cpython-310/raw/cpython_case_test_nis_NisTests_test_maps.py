# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_nis.py
# case: NisTests_test_maps

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        maps = nis.maps()
    except nis.error as msg:
        self.skipTest(str(msg))
    try:
        maps.remove('passwd.adjunct.byname')
    except ValueError:
        pass
    done = 0
    for nismap in maps:
        mapping = nis.cat(nismap)
        for (k, v) in mapping.items():
            if not k:
                continue
            if nis.match(k, nismap) != v:
                self.fail("NIS match failed for key `%s' in map `%s'" % (k, nismap))
            else:
                done = 1
                break
        if done:
            break
