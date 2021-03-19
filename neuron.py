import numpy as np
from dataclasses import dataclass, field


@dataclass
class Neuron:
    input: np.ndarray = field(init=False,
                              default_factory=lambda: np.array([],
                                                               dtype=float))
    weight: np.ndarray = field(init=False,
                               default_factory=lambda: np.array([],
                                                                dtype=float))
    z: np.ndarray = field(init=False,
                               default_factory=lambda: np.array([],
                                                                dtype=float))
    a: np.ndarray = field(init=False,
                               default_factory=lambda: np.array([],
                                                                dtype=float))
    grad_weight: np.ndarray = field(init=False,
                               default_factory=lambda: np.array([],
                                                                dtype=float))
    grad_z: np.ndarray = field(init=False,
                               default_factory=lambda: np.array([],
                                                                dtype=float))
    grad_a: np.ndarray = field(init=False,
                               default_factory=lambda: np.array([],
                                                                dtype=float))
