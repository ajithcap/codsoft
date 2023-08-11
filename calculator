from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):
        self.history = ''
        self.result = ''
        
        main_layout = BoxLayout(orientation='vertical')
        
        input_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.2))
        self.history_input = TextInput(
            font_size=24,
            readonly=True,
            halign='right',
            multiline=True
        )
        self.result_input = TextInput(
            font_size=32,
            readonly=True,
            halign='right',
            multiline=False
        )
        input_layout.add_widget(self.history_input)
        input_layout.add_widget(self.result_input)
        
        main_layout.add_widget(input_layout)
        
        buttons_layout = GridLayout(cols=4, spacing=10, size_hint=(1, 0.6))
        
        buttons = [
            ('7', 'number'), ('8', 'number'), ('9', 'number'), ('/', 'operator'),
            ('4', 'number'), ('5', 'number'), ('6', 'number'), ('*', 'operator'),
            ('1', 'number'), ('2', 'number'), ('3', 'number'), ('-', 'operator'),
            ('C', 'clear'), ('0', 'number'), ('=', 'equal'), ('+', 'operator')
        ]
        
        for button_text, button_type in buttons:
            button = Button(
                text=button_text,
                background_color=self.get_button_color(button_type),  # Set button color based on type
                color=(1, 1, 1, 1)  # White text color
            )
            button.bind(on_press=self.on_button_press)
            buttons_layout.add_widget(button)
        
        main_layout.add_widget(buttons_layout)
        
        return main_layout
    
    def on_button_press(self, instance):
        button_text = instance.text
        if button_text == '=':
            try:
                self.result = str(eval(self.history))
            except Exception:
                self.result = 'Error'
        elif button_text == 'C':
            self.history = ''
            self.result = ''
        else:
            self.history += button_text
    
        self.history_input.text = self.history
        self.result_input.text = self.result
    
    def get_button_color(self, button_type):
        if button_type == 'number':
            return (0.4, 0.4, 0.4, 1)  # Dark gray for number buttons
        elif button_type == 'operator':
            return (0.2, 0.7, 0.2, 1)  # Green for operator buttons
        elif button_type == 'clear':
            return (0.7, 0.2, 0.2, 1)  # Red for clear button
        elif button_type == 'equal':
            return (0.2, 0.2, 0.7, 1)  # Blue for equal button

if __name__ == '__main__':
    app = CalculatorApp()
    app.run()
