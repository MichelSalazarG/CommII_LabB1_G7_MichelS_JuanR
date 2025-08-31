import numpy as np
from gnuradio import gr

class blk(gr.sync_block):

    def __init__(self):  
        gr.sync_block.__init__(
            self,
            name='Promedios_de_tiempos',
            in_sig=[np.float32],
            out_sig=[np.float32, np.float32, np.float32, np.float32, np.float32]
        )
        # Acumuladores globales
        self.acum_sum = 0
        self.acum_sum2 = 0
        self.acum_var = 0
        self.Ntotales = 0

    def work(self, input_items, output_items):
        x = input_items[0]    
        y0, y1, y2, y3, y4 = output_items  

        N = len(x)
        self.Ntotales += N

        # -------------------
        # Media aritmética
        # -------------------
        self.acum_sum += np.sum(x)
        promedio = self.acum_sum / self.Ntotales
        y0[:] = promedio

        # -------------------
        # Media cuadrática (E[x²])
        # -------------------
        self.acum_sum2 += np.sum(x**2)
        media_cuadratica = self.acum_sum2 / self.Ntotales
        y1[:] = media_cuadratica

        # -------------------
        # RMS
        # -------------------
        rms = np.sqrt(media_cuadratica)
        y2[:] = rms

        # -------------------
        # Potencia promedio (en dB)
        # -------------------
        potencia_db = 10 * np.log10(media_cuadratica + 1e-12)  # evitar log(0)
        y3[:] = potencia_db

        # -------------------
        # Desviación estándar
        # -------------------
        self.acum_var += np.sum((x - promedio) ** 2)
        desviacion = np.sqrt(self.acum_var / self.Ntotales)
        y4[:] = desviacion

        return len(x)
