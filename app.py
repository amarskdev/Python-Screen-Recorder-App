# Screen recording app 

# This is a simple which let you record screen and save

# In this project we are using opencv, numpy, pyautogui and time module.

# Author Details 
# Name  :  Er. Amar kumar 
# Email :  amarkumar9685079691@gmail.com 

# Start of a source code

import numpy as np
import pyautogui as pt
from tkinter import *
import datetime
import time
import threading
import cv2

class ScreenRecorder:
    _screen_width = None
    _screen_height = None
    _hours = 0
    _minutes = 0
    _seconds = 0
    _videoObj = None
    _fps = 20
    _filename = None
    _recording = False
    _window = None
    _frame = None
    _label = None
    _time_label = None
    _target = 'screen'
    _TimeCounter_Label = None
    _frame_message = None
    _record_button_start = None
    _record_button_stop = None

    def __init__(self):
        self._screen_width, self._screen_height = pt.size()
        self._fps = 20
        self._window = Tk()
        self._window.title("Screen Recorder APP")
        self._window.geometry("600x400")  # Adjusted window size for better layout
        self._window.resizable(width=False, height=False)
        self._window.configure(bg='#0288d1')  # Green background for a fresh look
        
        # Frame for the main content
        self._frame = Frame(self._window, bg='#0288d1', bd=10, relief=RAISED)
        self._frame.pack(padx=20, pady=20, fill=BOTH, expand=True)
        
        # Add padding for the main content inside the frame
        self._frame.grid_propagate(False)

    def _getDisplayTime(self):
        if self._recording:
            if self._seconds == 60:
                self._minutes += 1
                self._seconds = 0
            if self._minutes == 60:
                self._hours += 1
                self._minutes = 0
            self._TimeCounter_Label.config(text=f'{self._hours:02}:{self._minutes:02}:{self._seconds:02}')
            self._seconds += 1
            self._TimeCounter_Label.after(1000, self._getDisplayTime)

    def _resetDisplayTime(self):
        self._hours = 0
        self._minutes = 0
        self._seconds = 0

    def _startRecording(self):
        self._recording = True
        self._resetDisplayTime()

        Button_Rec_thread = threading.Thread(target=self._recordingProcess)
        Thread_Counter = threading.Thread(target=self._getDisplayTime)
        Thread_Screen = threading.Thread(target=self._recordScreen)

        if self._recording:
            Button_Rec_thread.start()
            Thread_Counter.start()
        if self._target == 'screen':
            Thread_Screen.start()

    def _stopRecording(self):
        self._recording = False
        self._clearObjects()
        exit(0)

    def _recordingProcess(self):
        if self._recording:
            self._record_button_start['state'] = DISABLED
            self._label['text'] = 'Press q to quit and save recording'
            self._record_button_stop['state'] = NORMAL
        else:
            self._record_button_start['state'] = NORMAL

    def _clearObjects(self):
        self._videoObj.release()
        cv2.destroyAllWindows()

    def _recordScreen(self):
        current_time = datetime.datetime.now().strftime("%H%M%S")
        file_format = 'avi'
        self._filename = f'recording_{current_time}.{file_format}'
        prev_time = time.time()
        fourcc = cv2.VideoWriter_fourcc(*'MJPG')
        self._videoObj = cv2.VideoWriter(self._filename, fourcc, self._fps, (self._screen_width, self._screen_height))

        print("Recording Started......")
        print("Please type q or ctrl + c to stop recording!")

        try:
            while self._recording:
                image = pt.screenshot()
                rec_frame = np.array(image)
                rec_frame = cv2.cvtColor(rec_frame, cv2.COLOR_RGB2BGR)
                self._videoObj.write(rec_frame)
                cv2.imshow('screen recording', rec_frame)

                current_time = time.time()
                if current_time - prev_time < 1.0 / self._fps:
                    continue

                prev_time = current_time

                if cv2.waitKey(1) & 0xFF == ord("q"):
                    self._recording = False
                    break
        except Exception as e:
            print(f"Program exit: Error code {e}")
        except KeyboardInterrupt:
            self._clearObjects()
        finally:
            self._clearObjects()

    def startup(self):

        # Time counter label
        self._TimeCounter_Label = Label(self._frame, text='Record Time: 00:00:00', font=('Arial', 20, 'bold'), bg="#303F9F", fg="white", width=32)
        self._TimeCounter_Label.grid(row=0, column=0, padx=20, pady=20)

          # Record button style
        self._record_button_start = Button(self._frame, text="Start Recording", command=self._startRecording, font=('Arial', 16, 'bold'), bg="#FF9800", fg="white", activebackground="#E65100", relief=RAISED, width=20, height=2)
        self._record_button_start.grid(row=1, column=0, padx=10, pady=10)

        # Stop button style
        self._record_button_stop = Button(self._frame, text="Stop Recording", command=self._stopRecording, font=('Arial', 16, 'bold'), bg="#FF9800", fg="white", activebackground="#E65100", relief=RAISED, width=20, height=2)
        self._record_button_stop.grid(row=2, column=0, padx=10, pady=10)

        # Initially disable the stop button
        self._record_button_stop['state'] = DISABLED

        # Frame for message
        self._frame_message = Frame(self._window, bg="#0288d1")
        self._frame_message.pack(fill=X)

        # Message label with updated style
        self._label = Label(self._frame_message, text="Lets Record Your screen", font=('Arial', 14, 'italic'), bg="#0288d1", fg="white")
        self._label.pack(padx=20, pady=10)

        self._window.mainloop()


if __name__ == '__main__':
    app = ScreenRecorder()
    app.startup()

