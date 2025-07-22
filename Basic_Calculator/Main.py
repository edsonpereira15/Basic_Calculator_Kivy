from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):
        self.operators = ['+', '-', '*', '/']
        self.last_was_operator = None
        self.last_was_button = None
        main_layout = BoxLayout(orientation='vertical')
        self.solution = TextInput(
            multiline=False,
            readonly=True,
            halign='right',
            font_size=55
        )
        
        main_layout.add_widget(self.solution)
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['.', '0', 'C', '+'],
        ]
        
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text=label,
                    pos_hint={'center_x': 0.5, 'center_y': 0.5},
                )
                if label in self.operators:
                    button.background_color = (0,0,211,1)  # Azul para operadores
                button.bind(on_press=self.on_button_press)  # Dentro do loop interno
                h_layout.add_widget(button)  # Dentro do loop interno
            main_layout.add_widget(h_layout)
        
        equals_button = Button(
            text='=',
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            background_color=(0, 0, 0, 1)  # Preto
        )
        equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button)

        return main_layout
        
    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text
        
        if button_text == 'C':
            self.solution.text = ""
        else:
            if current and (
                self.last_was_operator and button_text in self.operators):
                return
            elif current == '' and button_text in self.operators:
                return
            else:
                new_text = current + button_text
                self.solution.text = new_text
                self.last_was_operator = button_text in self.operators
                     
    def on_solution(self, instance):
        text = self.solution.text
        if text:
                text = str(eval(self.solution.text))
                self.solution.text = text

    
if __name__ == '__main__':
    CalculatorApp().run()
