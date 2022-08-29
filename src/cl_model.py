import random
import numpy as np

class CL:
    
    def __init__(self,config):
        self.config = config
        
    # Generar un tamaño de reclamo $
    def create_claim_sz(self, size: int): #where size is n_claims
        
        shape = self.config.get('claim_sz_shape')
        scale = self.config.get('claim_sz_scale')

        return np.random.gamma(shape=shape, scale=scale, size=size)

        
    # Generar número de reclamos por un dia
    def create_claims_cnt(self):
        lambd = self.config.get('claim_rate_lambd')
        scale = 1/lambd
        total_time = 0
        claims_cnt = 0
        
        while total_time < 1:

            time_interval = np.random.exponential(scale=scale)
            total_time += time_interval
            claims_cnt += 1

        return claims_cnt

    # Generar total($) reclamos por un dia
    def compute_claims_total(self):
        n_claims = self.create_claims_cnt()

        total = self.create_claim_sz(size=n_claims).sum()

        return total

    # Correr una simulación
    def simulate(self):
        u = self.config.get('u')
        c = self.config.get('c')
        time_steps = self.config.get('time_steps')

        X = [u]
        for _ in range(time_steps):    
            X.append(X[-1] + c - self.compute_claims_total())

        return X

    # Correr n simulaciones
    def generate_simulations(self, n):
        simulations = []
        for _ in range(n):
            curr_sim = self.simulate()
            simulations.append(curr_sim)
        return simulations


        