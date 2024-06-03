class CalculadoraPromedio:
    def calcular_promedio(self, conjunto):
        if len(conjunto) == 0:
            return 0

        suma = sum(conjunto)
        return suma / len(conjunto)
