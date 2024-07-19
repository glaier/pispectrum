import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import serial
import threading

class SpectrumAnalyzer:
    def __init__(self, master):
        self.master = master
        self.master.title("Spectrum Analyzer")
        self.figure = Figure(figsize=(6, 4), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.ax.set_title('RF Signal Spectrum')
        self.ax.set_xlabel('Frequency')
        self.ax.set_ylabel('Amplitude')
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.master)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.serial_port = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)
        self.data = []

        self.update_spectrum()

    def update_spectrum(self):
        if self.serial_port.in_waiting > 0:
            line = self.serial_port.readline().decode('utf-8').rstrip()
            # Process the received data to extract frequency and amplitude information
            # Append the data to self.data
            # For example, self.data.append((frequency, amplitude))
        self.ax.clear()
        self.ax.plot([d[0] for d in self.data], [d[1] for d in self.data])
        self.canvas.draw()
        self.master.after(100, self.update_spectrum)

if __name__ == "__main__":
    root = tk.Tk()
    app = SpectrumAnalyzer(master=root)
    root.mainloop()
