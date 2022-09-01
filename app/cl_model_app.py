import random
import numpy as np

class CL:

    def __init__(self,config):
        self.config = config
        self.create_claim_sz = np.vectorize(self.create_claim_sz)


    # Generar un tamaño de reclamo $
    def create_claim_sz(self, size: int): #where size is n_claims
        
        shape = self.config.get('claim_sz_shape')
        scale = self.config.get('claim_sz_scale')
        print(shape)
        print(scale)
        return - np.random.gamma(shape=shape, scale=scale, size=size).sum()

        
    # Generar número de reclamos por un dia
    def create_claims_cnt(self):
        time_steps = self.config.get('time_steps')
        lambd = self.config.get('claim_rate_lambd')
        print(time_steps)
        print(lambd)
        return np.random.poisson(lam=lambd, size=time_steps)


    # Generar total($) reclamos por un dia
    def compute_claims_total(self):

        array_claims = self.create_claims_cnt()
        array_daily_total = self.create_claim_sz(array_claims)

        return array_daily_total


    # Correr una simulación
    def simulate(self):
        u = self.config.get('u')
        c = self.config.get('c')
        print(c)
        time_steps = self.config.get('time_steps')

        array_daily_total = self.compute_claims_total()
        array_daily_total_cum = array_daily_total.cumsum()

        primes_cum = np.repeat(c, time_steps).cumsum()
        array_daily_total_cum = np.add(array_daily_total_cum, primes_cum)
        
        array_daily_total_cum = np.add(array_daily_total_cum, u)
        array_daily_total_cum = np.insert(array_daily_total_cum, 0, u)

        return array_daily_total_cum


    def generate_simulations(self, n):
        simulations = []
        for idx in range(n):
            curr_sim = self.simulate()
            simulations.append(curr_sim)

        return simulations