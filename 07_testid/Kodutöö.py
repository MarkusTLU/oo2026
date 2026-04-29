import unittest

class Hoiupõrsas:
    saldo = 0

    def lisa_raha(self, summa):
        self.saldo += summa

    def get_saldo(self):
        return self.saldo

class TestHoiupõrsas(unittest.TestCase):
    h = Hoiupõrsas()

    def test_algus(self):
        self.assertEqual(self.h.get_saldo(), 0)

    def test_lisa_raha(self):
        self.h.lisa_raha(10)
        self.assertEqual(self.h.get_saldo(), 10)

    def test_lisa_veel_raha(self):
        self.h.lisa_raha(5)
        self.assertEqual(self.h.get_saldo(), 15)

suite = unittest.TestLoader().loadTestsFromTestCase(TestHoiupõrsas)
runner = unittest.TextTestRunner(verbosity=0)
result = runner.run(suite)
print(f"Tests run: {result.testsRun}")