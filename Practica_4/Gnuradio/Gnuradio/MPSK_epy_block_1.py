import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    """Bloque PSD sin matplotlib - Calcula la densidad espectral de potencia"""

    def __init__(self, N_ensayos=1000000, Ec=0, N_FFT=1024, Titulo="PSD", Tmax=1e-6, Fmuestreo=1e6):
        gr.sync_block.__init__(
            self,
            name='PSD Block',
            in_sig=[np.complex64],  # Solo entrada
            out_sig=None             # Sin salida
        )

        # Parámetros del bloque
        self.N_ensayos = int(N_ensayos)
        self.Ec = Ec
        self.N_FFT = int(N_FFT)
        self.Titulo = Titulo
        self.Tmax = Tmax
        self.Fmuestreo = Fmuestreo

    def work(self, input_items, output_items):
        data = input_items[0]

        if len(data) == 0:
            return 0

        # Calcula FFT y PSD (en dB)
        fft_data = np.fft.fftshift(np.fft.fft(data, self.N_FFT))
        psd = 10 * np.log10(np.abs(fft_data)**2 / self.N_FFT)

        # Puedes imprimir parte de la PSD si quieres verificar
        print(f"[{self.Titulo}] PSD (primeros 5 valores): {psd[:5]} dB")

        # Si luego quieres enviar esta info a un archivo o a otro bloque,
        # aquí es donde puedes implementarlo.

        return len(data)
