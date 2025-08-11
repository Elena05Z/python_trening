from task_9_checks import Checks


class CheckBox(Checks):
    def __init__(self, text):
        super().__init__(text)


class RadioButton(Checks):
    def __init__(self, text):
        super().__init__(text)


class TextInput(Checks):
    def __init__(self, text):
        super().__init__(text)


class Dropdown(Checks):
    def __init__(self, text):
        super().__init__(text)


checkbox = CheckBox("Checkbox text")
radio_button = RadioButton("Radio button text")
text_input = TextInput("Text input placeholder")
dropdown = Dropdown("Dropdown options")


print(checkbox.check_text())          
print(radio_button.check_text())      
print(text_input.check_text())        
print(dropdown.check_text())          
