# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestIntFlag_test_unique_composite

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class TestFlag(IntFlag):
        one = auto()
        two = auto()
        three = auto()
        four = auto()
        five = auto()
        six = auto()
        seven = auto()
        eight = auto()

        def __eq__(self, other):
            return self is other

        def __hash__(self):
            return hash(self._value_)
    seen = set()
    failed = False

    def cycle_enum():
        nonlocal failed
        try:
            for i in range(256):
                seen.add(TestFlag(i))
        except Exception:
            failed = True
    threads = [threading.Thread(target=cycle_enum) for _ in range(8)]
    with threading_helper.start_threads(threads):
        pass
    self.assertFalse(failed, 'at least one thread failed while creating composite members')
    self.assertEqual(256, len(seen), 'too many composite members created')
