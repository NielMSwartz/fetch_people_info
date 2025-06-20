from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from search_logic import search_info

Builder.load_file("main.kv")

class RootWidget(BoxLayout):
    def search(self):
        name = self.ids.name_input.text
        result = search_info(name)
        
        if result:
            output = "\n".join([f"{key}: {value}" for key, value in result.items()])
        else:
            output = "No Match Found"
            
        self.ids.result_label.text = output
    
class ExcelSearchApp(App):
    def build(self):
        return RootWidget()
    
if __name__ == "__main__":
    ExcelSearchApp().run()


    
