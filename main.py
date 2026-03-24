name: Build Runamo APK
on: [push, workflow_dispatch]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      # 1. Сохтани файли main.py (Коди барнома)
      - name: Create main.py
        run: |
          cat <<EOF > main.py
          from kivy.app import App
          from kivy.uix.screenmanager import ScreenManager, Screen
          from kivy.uix.boxlayout import BoxLayout
          from kivy.uix.label import Label
          from kivy.uix.button import Button
          from kivy.uix.textinput import TextInput
          from kivy.core.window import Window
          from kivy.utils import get_color_from_hex

          class WelcomeScreen(Screen):
              def on_enter(self):
                  self.clear_widgets()
                  layout = BoxLayout(orientation='vertical', padding=40, spacing=20)
                  layout.add_widget(Label(text="ХУШ ОМАДЕД!", font_size='24sp', color=(0,0,0,1), bold=True))
                  self.name_input = TextInput(hint_text="НОМ ВА НАСАБИ ОМӮЗГОР", multiline=False, size_hint_y=None, height='50dp')
                  layout.add_widget(self.name_input)
                  btn = Button(text="ДОХИЛ ШУДАН", background_color=get_color_from_hex('#4CAF50'), size_hint_y=None, height='50dp')
                  btn.bind(on_release=self.go_to_menu)
                  layout.add_widget(btn)
                  self.add_widget(layout)

              def go_to_menu(self, instance):
                  if self.name_input.text:
                      App.get_running_app().user_name = self.name_input.text
                      self.manager.current = 'menu'

          class MenuScreen(Screen):
              def on_enter(self):
                  self.clear_widgets()
                  layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
                  layout.add_widget(Label(text="ИНТИХОБИ ХИЗМАТРАСОНӢ", color=(0,0,0,1)))
                  btn1 = Button(text="СОХТАНИ НАҚШАИ ДАРС", background_color=get_color_from_hex('#FFFFFF'), color=(0,0,0,1))
                  btn1.bind(on_release=lambda x: setattr(self.manager, 'current', 'result'))
                  layout.add_widget(btn1)
                  self.add_widget(layout)

          class ResultScreen(Screen):
              def on_enter(self):
                  self.clear_widgets()
                  layout = BoxLayout(orientation='vertical', padding=30)
                  layout.add_widget(Label(text=f"УСТОД {App.get_running_app().user_name}\nНАҚША ОМОДА ШУД!", color=(0,0,0,1), halign='center'))
                  self.add_widget(layout)

          class RunamoApp(App):
              user_name = ""
              def build(self):
                  sm = ScreenManager()
                  sm.add_widget(WelcomeScreen(name='welcome'))
                  sm.add_widget(MenuScreen(name='menu'))
                  sm.add_widget(ResultScreen(name='result'))
                  return sm

          if __name__ == '__main__':
              RunamoApp().run()
          EOF

      # 2. Сохтани файли buildozer.spec (Танзимот)
      - name: Create buildozer.spec
        run: |
          cat <<EOF > buildozer.spec
          [app]
          title = RUNAMO
          package.name = runamo
          package.domain = org.runamo
          source.dir = .
          source.include_exts = py,png,jpg,kv,atlas
          version = 1.0
          requirements = python3,kivy
          orientation = portrait
          osx.python_version = 3
          osx.kivy_version = 1.9.1
          fullscreen = 0
          android.api = 33
          android.minapi = 21
          android.sdk = 23
          android.ndk = 25b
          android.archs = arm64-v8a
          EOF

      # 3. Сохтани APK
      - name: Build with Buildozer
        uses: ArtemSerebrenninkov/buildozer-action@v1
        with:
          buildozer_version: master

      # 4. Боргузории APK барои зеркашӣ
      - name: Upload APK
        uses: actions/upload-artifact@v3
        with:
          name: Runamo-APK-File
          path: bin/*.apk



























































































