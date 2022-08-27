import random
import numpy as np

class CL:

    def __init__(self,config):
        self.config = config
        
    # Generar un tamaño de reclamo $
    def create_claim_sz(self):
        mu = self.config.get('claim_sz_mu')
        lambd = 1/mu
        #return random.gammavariate(self.alpha, self.beta)
        return random.expovariate(lambd=lambd)
        
    # Generar número de reclamos por un dia
    def create_claims_cnt(self):
        lambd = self.config.get('claim_rate_lambd')
        total_time = 0
        claims_cnt = 0
        
        while total_time < 1:
            prob = np.random.uniform()
            time_interval = (-np.log(prob)) / lambd
            total_time += time_interval
            claims_cnt += 1

        return claims_cnt

    # Generar total($) reclamos por un dia
    def compute_claims_total(self):
        n_claims = self.create_claims_cnt()

        total = 0
        for _ in range(n_claims):
            total += self.create_claim_sz()

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