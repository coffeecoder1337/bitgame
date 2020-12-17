import kivy
from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class Test(App):
    def __init__(self):
        App.__init__(self)
        self.sound_clap = SoundLoader.load("sound1.wav")
        self.sound_clap.volume = 0.3
        self.sound_crash = SoundLoader.load("sound2.wav")
        self.sound_crash.volume = 0.3
        self.sound_timend = SoundLoader.load("sound3.wav")
        self.sound_timend.volume = 0.3
        self.sound_kick = SoundLoader.load("sound4.wav")
        self.sound_kick.volume = 0.3

    def clap(self, *args):
        self.sound_clap.play()

    def crash(self, *args):
        self.sound_crash.play()
    
    def timend(self, *args):
        self.sound_timend.play()
    
    def kick(self, *args):
        self.sound_kick.play()
        
    def build(self):
        btn_clap = Button(text="clap")
        btn_clap.bind(on_press=self.clap)
        btn_crash = Button(text="crash")
        btn_crash.bind(on_press=self.crash)
        btn_timend = Button(text="timend")
        btn_timend.bind(on_press=self.timend)
        btn_kick = Button(text="kick")
        btn_kick.bind(on_press=self.kick)

        layout = GridLayout(cols=2)

        layout.add_widget(btn_clap)
        layout.add_widget(btn_crash)
        layout.add_widget(btn_timend)
        layout.add_widget(btn_kick)

        return layout

app = Test()
app.run()
