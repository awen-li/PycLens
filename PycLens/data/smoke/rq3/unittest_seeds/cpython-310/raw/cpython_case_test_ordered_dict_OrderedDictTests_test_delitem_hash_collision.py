# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ordered_dict.py
# case: OrderedDictTests_test_delitem_hash_collision

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    OrderedDict = self.OrderedDict

    class Key:

        def __init__(self, hash):
            self._hash = hash
            self.value = str(id(self))

        def __hash__(self):
            return self._hash

        def __eq__(self, other):
            try:
                return self.value == other.value
            except AttributeError:
                return False

        def __repr__(self):
            return self.value

    def blocking_hash(hash):
        MINSIZE = 8
        i = hash & MINSIZE - 1
        return (i << 2) + i + hash + 1
    COLLIDING = 1
    key = Key(COLLIDING)
    colliding = Key(COLLIDING)
    blocking = Key(blocking_hash(COLLIDING))
    od = OrderedDict()
    od[key] = ...
    od[blocking] = ...
    od[colliding] = ...
    od['after'] = ...
    del od[blocking]
    del od[colliding]
    self.assertEqual(list(od.items()), [(key, ...), ('after', ...)])
