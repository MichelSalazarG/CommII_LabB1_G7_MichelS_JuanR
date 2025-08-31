"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    """Acumulador continuo: suma acumulativa entre bloques"""

    def __init__(self):
        gr.sync_block.__init__(
            self,
            name='e_Acum_prueba',
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        # Estado interno: valor acumulado
        self._accum = 0.0

    def work(self, input_items, output_items):
        x = input_items[0]
        y = output_items[0]

        # Acumular manteniendo estado entre llamadas
        for i in range(len(x)):
            self._accum += x[i]
            y[i] = self._accum

        return len(y)
