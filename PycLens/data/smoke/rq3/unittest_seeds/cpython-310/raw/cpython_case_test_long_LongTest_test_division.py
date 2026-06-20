# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_long.py
# case: LongTest_test_division

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    digits = list(range(1, MAXDIGITS + 1)) + list(range(KARATSUBA_CUTOFF, KARATSUBA_CUTOFF + 14))
    digits.append(KARATSUBA_CUTOFF * 3)
    for lenx in digits:
        x = self.getran(lenx)
        for leny in digits:
            y = self.getran(leny) or 1
            self.check_division(x, y)
    self.check_division(1231948412290879395966702881, 1147341367131428698)
    self.check_division(815427756481275430342312021515587883, 707270836069027745)
    self.check_division(627976073697012820849443363563599041, 643588798496057020)
    self.check_division(1115141373653752303710932756325578065, 1038556335171453937726882627)
    self.check_division(922498905405436751940989320930368494, 949985870686786135626943396)
    self.check_division(768235853328091167204009652174031844, 1091555541180371554426545266)
    self.check_division(20172188947443, 615611397)
    self.check_division(1020908530270155025, 950795710)
    self.check_division(128589565723112408, 736393718)
    self.check_division(609919780285761575, 18613274546784)
    self.check_division(710031681576388032, 26769404391308)
    self.check_division(1933622614268221, 30212853348836)
