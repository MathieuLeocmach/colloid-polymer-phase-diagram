# colloid_polymer_phase_diagram

Phase behaviour of Colloid+Polymer mixture according to generalized free volume theory
see Gerard J Fleer and Remco Tuinier, Advances in Colloid and Interface Science 143, 1-47 (2008).

The code was originally written by Mathieu Leocmach in package [colloids](https://github.com/MathieuLeocmach/colloids).

## Install

The most convenient way would be: `pip colloid_polymer_phase_diagram`

## How to Use It

```python
from colloid_polymer_phase_diagram import phase

qR = 0.072
q = phase.qR2q(qR)
fc, pivc = phase.CarnahanStarling().critical_point(q)
print(f'At critical point colloid volume fraction is {phase.f2vf(fc):0.3f} and osmotic insertion work is {pivc:0.3f} kT')

import numpy as np
pivs = 1./np.linspace(1./pivc, 1./3500)
sp = phase.CarnahanStarling().spinodalGL(q, pivs)

plt.figure('reservoir')
plt.plot(phase.f2vf(sp[:,1]), sp[:,0])
plt.plot(phase.f2vf(sp[:,2]), sp[:,0])
plt.scatter(phase.f2vf(fc), pivc, c='k')
plt.xlabel(r'$\varphi$')
plt.ylabel(r'$\Pi v$')

plt.figure('experimental')
plt.plot(phase.f2vf(sp[:,1]), phase.piv2y(sp[:,0], qR) * phase.alpha(sp[:,1], q))
plt.plot(phase.f2vf(sp[:,2]), phase.piv2y(sp[:,0], qR) * phase.alpha(sp[:,2], q))
plt.scatter(phase.f2vf(fc), phase.piv2y(pivc, qR) * phase.alpha(fc, q), c='k')
plt.xlabel(r'$\varphi$')
plt.ylabel(r'$y$')
plt.ylim(0,1.4)
```
