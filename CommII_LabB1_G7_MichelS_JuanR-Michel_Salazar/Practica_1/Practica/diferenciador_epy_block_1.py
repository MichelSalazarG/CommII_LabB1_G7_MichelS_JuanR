import numpy as np

from gnuradio import gr



class differentiator(gr.sync_block):

    def __init__(self, Ts=1.0, threshold=0.0):

        super().__init__(

            name="eDiff",

            in_sig=[np.float32],

            out_sig=[np.float32],

        )

        self.Ts = float(Ts)

        self.th = float(threshold)

        self.set_history(2)  # garantiza tener x[n-1] disponible



    def work(self, input_items, output_items):

        x = input_items[0]      # len(x) = len(y) + (history-1) = len(y) + 1

        y = output_items[0]



        diffs = (x[1:] - x[:-1]) / self.Ts  # derivada discreta



        if self.th > 0.0:

            np.copyto(y, np.where(np.abs(diffs) > self.th, diffs, 0.0))

        else:

            np.copyto(y, diffs)



        return len(y)
