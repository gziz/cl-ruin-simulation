# Cramer-Lundberg Model: Ruin Simulation

The Cramer-Lundberg model is a classic in risk theory.
The model approximates the probability of insolvency of an insurance company.

$$ X_t = u + ct - \sum_{i=1}^{N_t}Z_i $$

* Premiums at a constant rate $c>0$.
* Claims that arrive according to a Poisson process $N_t$ with the claim size following a gamma distribution $Z_i$.
* Initial capital $u$
* Capital at a given time $t$, $X(t)$

