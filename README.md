# Cramer-Lundberg Model: Ruin Simulation

The Cramer-Lundberg model is a classic in risk theory.
The model approximates the probability of insolvency of an insurance company.

$$ X_t = u + ct - \sum_{i=1}^{N_t}Z_i $$

* Premiums at a constant rate $c>0$.
* Claims that arrive according a Poisson process $N_t$ with the size following a gamma distribution $Z_i$.
* Initial capital $u$
* Capital at given time $X_t$

