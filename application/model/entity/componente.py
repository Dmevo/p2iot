
class Componente:

    def __init__(self, ozonio, particula, monoxido_carbono, oxido_nitroso, gas, temperatura, umidade, data):
        self.ozonio = ozonio
        self.particula = particula
        self.monoxido_carbono = monoxido_carbono
        self.oxido_nitroso = oxido_nitroso
        self.gas = gas
        self.temperatura = temperatura
        self.umidade = umidade
        self.data = data

    def set_ozonio(self, ozonio):
        self.ozonio = ozonio

    def get_ozonio(self):
        return self.ozonio

    def set_particula(self, particula):
        self.particula = particula

    def get_particula(self):
        return self.particula

    def set_carbono(self, carbono):
        self.monoxido_carbono = carbono

    def get_carbono(self):
        return self.monoxido_carbono

    def set_nitroso(self, nitroso):
        self.oxido_nitroso = nitroso
    
    def get_nitroso(self):
        return self.oxido_nitroso

    def set_gas(self, gas):
        self.gas = gas

    def get_gas(self):
        return self.gas

    def set_temperatura(self, temperatura):
        self.temperatura = temperatura
    
    def get_temperatura(self):
        return self.temperatura

    def set_umidade(self, umidade):
        self.umidade = umidade

    def get_umidade(self):
        return self.umidade

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data