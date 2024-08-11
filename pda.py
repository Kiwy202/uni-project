class Operacion:
    def _init_(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def exponencial(self, a, b):
        return a ** b

    def primo(self, c):
        primos = []
        for num in range(2, c + 1):
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primos.append(num)
        return primos

# Crear un objeto de la clase Operacion
operacion = Operacion()

# Llamar al método exponencial
print(operacion.exponencial(2, 3)) # 8

# Llamar al método primo
print(operacion.primo(10)) # [2, 3, 5, 7]