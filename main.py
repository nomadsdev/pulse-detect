import numpy as np
import pyaudio
from scipy.fft import fft
import time
import argparse

class F:
    def __init__(self, c, s, r):
        self.c, self.s, self.r = c, s, r
        self.a = pyaudio.PyAudio()
        self.st = self.__init_s()

    def __init_s(self):
        return self.a.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=self.s,
            input=True,
            frames_per_buffer=self.c
        )

    def __r(self):
        f = []
        t0 = time.time()
        while time.time() - t0 < self.r:
            try:
                d = self.st.read(self.c)
                f.append(d)
            except IOError as e:
                print(f"E: {e}")
                break
        return b''.join(f)

    def __cf(self, d):
        a = np.frombuffer(d, dtype=np.int16)
        ff = fft(a)
        f = np.fft.fftfreq(len(a), 1 / self.s)
        m = np.abs(ff)
        return f[np.argmax(m[:len(a) // 2])]

    def m(self):
        print("R...")
        try:
            while True:
                d = self.__r()
                f = self.__cf(d)
                print(f"DF: {f:.2f} Hz")
                time.sleep(self.r)
        except KeyboardInterrupt:
            print("S...")
        finally:
            self.__c()

    def __c(self):
        self.st.stop_stream()
        self.st.close()
        self.a.terminate()

def p():
    parser = argparse.ArgumentParser(description="A.")
    parser.add_argument('-f', action='store_true', help="E")
    parser.add_argument('-t', type=int, default=1, help="D in s")
    return parser.parse_args()

if __name__ == "__main__":
    a = p()
    if a.f:
        m = F(c=1024, s=44100, r=a.t)
        m.m()
    else:
        print("M not E. Use '-f'.")