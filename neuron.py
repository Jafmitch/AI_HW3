import numpy as np
from dataclasses import dataclass, field


@dataclass
class neuron:
    input: np.ndarray = field(init=False,
                              default_factory=lambda: np.array([],
                                                               dtype=float).T)
    weight: np.ndarray = field(init=False,
                               default_factory=lambda: np.array([],
                                                                dtype=float))
    output: np.ndarray = field(init=False,
                               default_factory=lambda: np.array([],
                                                                dtype=float))
