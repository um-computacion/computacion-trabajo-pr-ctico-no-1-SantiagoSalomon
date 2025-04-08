import unittest

def decimal_a_romano(num):
    
    if not 1 <= num <= 3999:
        return "El número tiene que estar entre 1 y 3999. Intente denuevo."
    
    numeros = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    letras = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    
    resultado = ''
    i = 0
    
    while num > 0:
        
        repeticiones = num // numeros[i]
        resultado += letras[i] * repeticiones
        num %= numeros[i]
        
        i += 1
    return resultado

class TestConversorRomano(unittest.TestCase):
    
    def test_numeros_basicos(self):
        """Prueba los números básicos del 1 al 10"""
        self.assertEqual(decimal_a_romano(1), "I")
        self.assertEqual(decimal_a_romano(2), "II")
        self.assertEqual(decimal_a_romano(3), "III")
        self.assertEqual(decimal_a_romano(4), "IV")
        self.assertEqual(decimal_a_romano(5), "V")
        self.assertEqual(decimal_a_romano(6), "VI")
        self.assertEqual(decimal_a_romano(7), "VII")
        self.assertEqual(decimal_a_romano(8), "VIII")
        self.assertEqual(decimal_a_romano(9), "IX")
        self.assertEqual(decimal_a_romano(10), "X")
    
    def test_numeros_decenas(self):
        """Prueba números que utilizan símbolos de decenas (X, L, C)"""
        self.assertEqual(decimal_a_romano(14), "XIV")
        self.assertEqual(decimal_a_romano(40), "XL")
        self.assertEqual(decimal_a_romano(49), "XLIX")
        self.assertEqual(decimal_a_romano(50), "L")
        self.assertEqual(decimal_a_romano(90), "XC")
        self.assertEqual(decimal_a_romano(99), "XCIX")
    
    def test_numeros_centenas(self):
        """Prueba números que utilizan símbolos de centenas (C, D, M)"""
        self.assertEqual(decimal_a_romano(100), "C")
        self.assertEqual(decimal_a_romano(400), "CD")
        self.assertEqual(decimal_a_romano(500), "D")
        self.assertEqual(decimal_a_romano(900), "CM")
        self.assertEqual(decimal_a_romano(999), "CMXCIX")
    
    def test_numeros_miles(self):
        """Prueba números que utilizan símbolos de miles (M)"""
        self.assertEqual(decimal_a_romano(1000), "M")
        self.assertEqual(decimal_a_romano(1984), "MCMLXXXIV")
        self.assertEqual(decimal_a_romano(2023), "MMXXIII")
        self.assertEqual(decimal_a_romano(3549), "MMMDXLIX")
        self.assertEqual(decimal_a_romano(3999), "MMMCMXCIX")
    
    def test_limites(self):
        """Prueba los límites del rango válido"""
        self.assertEqual(decimal_a_romano(1), "I")
        self.assertEqual(decimal_a_romano(3999), "MMMCMXCIX")
        self.assertEqual(decimal_a_romano(0), "El número tiene que estar entre 1 y 3999. Intente denuevo.")
        self.assertEqual(decimal_a_romano(4000), "El número tiene que estar entre 1 y 3999. Intente denuevo.")
        self.assertEqual(decimal_a_romano(-5), "El número tiene que estar entre 1 y 3999. Intente denuevo.")
    
    def test_casos_especiales(self):
        """Prueba casos que combinan diferentes reglas de la numeración romana"""
        self.assertEqual(decimal_a_romano(444), "CDXLIV")
        self.assertEqual(decimal_a_romano(1999), "MCMXCIX")
        self.assertEqual(decimal_a_romano(2888), "MMDCCCLXXXVIII")
        self.assertEqual(decimal_a_romano(3333), "MMMCCCXXXIII")



if __name__ == "__main__":
    unittest.main()