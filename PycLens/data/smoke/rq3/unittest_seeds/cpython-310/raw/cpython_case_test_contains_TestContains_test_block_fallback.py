# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contains.py
# case: TestContains_test_block_fallback

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class ByContains(object):

        def __contains__(self, other):
            return False
    c = ByContains()

    class BlockContains(ByContains):
        """Is not a container

            This class is a perfectly good iterable (as tested by
            list(bc)), as well as inheriting from a perfectly good
            container, but __contains__ = None prevents the usual
            fallback to iteration in the container protocol. That
            is, normally, 0 in bc would fall back to the equivalent
            of any(x==0 for x in bc), but here it's blocked from
            doing so.
            """

        def __iter__(self):
            while False:
                yield None
        __contains__ = None
    bc = BlockContains()
    self.assertFalse(0 in c)
    self.assertFalse(0 in list(bc))
    self.assertRaises(TypeError, lambda : 0 in bc)
