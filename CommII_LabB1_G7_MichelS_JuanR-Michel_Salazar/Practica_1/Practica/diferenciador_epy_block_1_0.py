import numpy as np
from gnuradio import gr

class differentiator(gr.sync_block):
    def __init__(self):
        gr.sync_block.__init__(self,
            name="eDiff",
            in_sig=[np.float32],
            out_sig=[np.float32])
        self.prev = 0.0  # valor anterior de la señal

    def work(self, input_items, output_items):
        x = input_items[0]
        y = output_items[0]

        # Diferenciación discreta: y[n] = x[n] - x[n-1]
        y[0] = x[0] - self.prev
        for i in range(1, len(x)):
            y[i] = x[i] - x[i-1]

        # Guardar último valor para la próxima llamada
        self.prev = x[-1]

        return len(y)
