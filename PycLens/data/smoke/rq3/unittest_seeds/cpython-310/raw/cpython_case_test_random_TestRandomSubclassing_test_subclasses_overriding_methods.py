# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_random.py
# case: TestRandomSubclassing_test_subclasses_overriding_methods

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class SubClass1(random.Random):

        def random(self):
            called.add('SubClass1.random')
            return random.Random.random(self)

        def getrandbits(self, n):
            called.add('SubClass1.getrandbits')
            return random.Random.getrandbits(self, n)
    called = set()
    SubClass1().randrange(42)
    self.assertEqual(called, {'SubClass1.getrandbits'})

    class SubClass2(random.Random):

        def random(self):
            called.add('SubClass2.random')
            return random.Random.random(self)
    called = set()
    SubClass2().randrange(42)
    self.assertEqual(called, {'SubClass2.random'})

    class SubClass3(SubClass2):

        def getrandbits(self, n):
            called.add('SubClass3.getrandbits')
            return random.Random.getrandbits(self, n)
    called = set()
    SubClass3().randrange(42)
    self.assertEqual(called, {'SubClass3.getrandbits'})

    class SubClass4(SubClass3):

        def random(self):
            called.add('SubClass4.random')
            return random.Random.random(self)
    called = set()
    SubClass4().randrange(42)
    self.assertEqual(called, {'SubClass4.random'})

    class Mixin1:

        def random(self):
            called.add('Mixin1.random')
            return random.Random.random(self)

    class Mixin2:

        def getrandbits(self, n):
            called.add('Mixin2.getrandbits')
            return random.Random.getrandbits(self, n)

    class SubClass5(Mixin1, random.Random):
        pass
    called = set()
    SubClass5().randrange(42)
    self.assertEqual(called, {'Mixin1.random'})

    class SubClass6(Mixin2, random.Random):
        pass
    called = set()
    SubClass6().randrange(42)
    self.assertEqual(called, {'Mixin2.getrandbits'})

    class SubClass7(Mixin1, Mixin2, random.Random):
        pass
    called = set()
    SubClass7().randrange(42)
    self.assertEqual(called, {'Mixin1.random'})

    class SubClass8(Mixin2, Mixin1, random.Random):
        pass
    called = set()
    SubClass8().randrange(42)
    self.assertEqual(called, {'Mixin2.getrandbits'})
