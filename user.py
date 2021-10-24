from dtw import dtw
from config import *
import librosa.display
from numpy.linalg import norm
import sounddevice as sd
from scipy.io.wavfile import write
from tkinter import *
from tkinter import messagebox


def sign_up_click():
    """Create sign_up window"""
    SignUp().mainloop()


class MainApp(Tk):
    def __init__(self):
        super().__init__()
        self.title(APP_NAME)
        self.geometry(main_geometry)

        self.frame = Frame(self).pack(pady=10)

        self.label = Label(self.frame, text=MAIN_LABEL).pack(side=TOP)
        self.log_in = Button(self.frame, text=LOG_IN_BTN, command=self.compare).pack(side=RIGHT, padx=20)
        self.sign_up = Button(self.frame, text=SIGN_UP_BTN, command=sign_up_click).pack(side=LEFT, padx=20)

    def compare(self, name='current_user'):
        """
        Compares 2 records
        :param name: String
        :return: None
        """
        messagebox.showinfo(title=RECORDING_MESSAGE_NAME, message=RECORDING_MESSAGE)
        voice = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
        sd.wait()
        write(f'{name}.wav', fs, voice)

        y1, sr1 = librosa.load('new_user.wav')
        y2, sr2 = librosa.load('current_user.wav')

        mfcc1 = librosa.feature.mfcc(y1, sr1)
        mfcc2 = librosa.feature.mfcc(y2, sr2)

        dist, cost, acc_cost, path = dtw(mfcc1.T, mfcc2.T, dist=lambda x, y: norm(x - y, ord=1))

        if float(dist) < SENSIVITY:
            messagebox.showinfo(title=RECORDING_MESSAGE_SUCCESS, message=SUCCESS)
            if ENDING_DESTROY:
                self.destroy()
        else:
            messagebox.showerror(title=RECORDING_ERROR, message=ERROR)


class SignUp(Tk):
    def __init__(self):
        """Initialize a SignUp window class"""
        super().__init__()
        self.title(SIGN_UP_NAME)
        self.geometry(sign_up_geometry)

        Label(self, text=POSITION).pack()
        Entry(self).pack()
        Label(self, text=FIO).pack()
        Entry(self).pack()
        Label(self, text=SMTH).pack()
        Entry(self).pack()

        Button(self, text=RECORD_VOICE, command=self.record_voice).pack()
        Button(self, text=BACK_TO_MAIN_MENU, command=self.back_click).pack()

    def back_click(self) -> None:
        """Destroy current window"""
        self.destroy()

    def record_voice(self, name: str = 'new_user') -> None:
        """
        Record new user voice to register him
        :param name: String
        :return: None
        """
        messagebox.showinfo(title=RECORDING_MESSAGE_NAME, message=RECORDING_MESSAGE)
        voice = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
        sd.wait()
        write(f'{name}.wav', fs, voice)
        self.back_click()
        messagebox.showinfo(title=RECORDING_SUCCESS, message=RECORDING_MESSAGE_SUCCESS)


app = MainApp().mainloop()
