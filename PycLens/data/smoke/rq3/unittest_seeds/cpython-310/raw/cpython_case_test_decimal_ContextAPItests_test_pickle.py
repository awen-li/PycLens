# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: ContextAPItests_test_pickle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        Context = self.decimal.Context
        savedecimal = sys.modules['decimal']
        sys.modules['decimal'] = self.decimal
        c = Context()
        e = pickle.loads(pickle.dumps(c, proto))
        self.assertEqual(c.prec, e.prec)
        self.assertEqual(c.Emin, e.Emin)
        self.assertEqual(c.Emax, e.Emax)
        self.assertEqual(c.rounding, e.rounding)
        self.assertEqual(c.capitals, e.capitals)
        self.assertEqual(c.clamp, e.clamp)
        self.assertEqual(c.flags, e.flags)
        self.assertEqual(c.traps, e.traps)
        combinations = [(C, P), (P, C)] if C else [(P, P)]
        for (dumper, loader) in combinations:
            for (ri, _) in enumerate(RoundingModes):
                for (fi, _) in enumerate(OrderedSignals[dumper]):
                    for (ti, _) in enumerate(OrderedSignals[dumper]):
                        prec = random.randrange(1, 100)
                        emin = random.randrange(-100, 0)
                        emax = random.randrange(1, 100)
                        caps = random.randrange(2)
                        clamp = random.randrange(2)
                        sys.modules['decimal'] = dumper
                        c = dumper.Context(prec=prec, Emin=emin, Emax=emax, rounding=RoundingModes[ri], capitals=caps, clamp=clamp, flags=OrderedSignals[dumper][:fi], traps=OrderedSignals[dumper][:ti])
                        s = pickle.dumps(c, proto)
                        sys.modules['decimal'] = loader
                        d = pickle.loads(s)
                        self.assertIsInstance(d, loader.Context)
                        self.assertEqual(d.prec, prec)
                        self.assertEqual(d.Emin, emin)
                        self.assertEqual(d.Emax, emax)
                        self.assertEqual(d.rounding, RoundingModes[ri])
                        self.assertEqual(d.capitals, caps)
                        self.assertEqual(d.clamp, clamp)
                        assert_signals(self, d, 'flags', OrderedSignals[loader][:fi])
                        assert_signals(self, d, 'traps', OrderedSignals[loader][:ti])
        sys.modules['decimal'] = savedecimal
