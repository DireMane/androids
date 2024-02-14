from kivy.lang import Builder
from PIL import Image, ImageFilter
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.tab import (
    MDTabsItemIcon,
    MDTabsItemText,
    MDTabsItem,
)
from kivymd.uix.pickers import MDModalDatePicker
from kivy.properties import StringProperty
KV = '''
MDScreen:
    md_bg_color: app.theme_cls.backgroundColor
    
    GridLayout:
        cols: 3
        row_default_height: "48dp"
        row_force_default: True
        spacing: "8dp"
        
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint: None, None
        width: root.width * 0.8
        
        MDTextField:
            mode: "outlined"
            size_hint_x: None
            width: "240dp"
            MDTextFieldLeadingIcon:
                icon: "radio-handheld"
            MDTextFieldHintText:
                text: "Номер Р/С"
            MDTextFieldTrailingIcon:
                icon: "information"
            MDTextFieldMaxLengthText:
                max_text_length: 5

        MDTextField:
            mode: "outlined"
            size_hint_x: None
            width: "240dp"
            MDTextFieldLeadingIcon:
                icon: "ethernet-cable"
            MDTextFieldHintText:
                text: "IP"
            MDTextFieldTrailingIcon:
                icon: "information"
            MDTextFieldMaxLengthText:
                max_text_length: 15
            
        MDTextField:
            mode: "outlined"
            size_hint_x: None
            width: "140dp"
            
            MDTextFieldHintText:
                text: "Port"
            MDTextFieldTrailingIcon:
                icon: "information"
            MDTextFieldMaxLengthText:
                max_text_length: 5
        BoxLayout:
            orientation: 'horizontal'
            spacing: "8dp"
            padding: "30dp"
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            MDLabel:
                text: "Маска"
                size_hint_x: None
                width: "80dp"
                valign: "middle"
        
            MDSwitch:
                pos_hint: {'center_x': .5, 'center_y': .5}
                
    MDButton:
        text: "My Button"
        pos_hint: {'right': 1, 'top': 1}  
        size_hint: None, None
        anchor_y: 'top'
        on_release: app.show_date_picker()
        MDButtonIcon:
            style: "standard"
            icon: 'calendar'
    MDSlider:
        step: 10
        value: 50
    MDButton:
        style: "elevated"
        pos_hint: {"center_x": .5, "center_y": .2}

        MDButtonIcon:
            icon: "plus"

        MDButtonText:
            text: "Отправить"
'''

class Example(MDApp):
    background_image = StringProperty("background.jpg")
    background_image_blurred = StringProperty("background_blurred.jpg")

    def build(self):
        self.theme_cls.primary_palette = "Olive"
        return Builder.load_string(KV)

    def show_date_picker(self):
        date_dialog = MDModalDatePicker()
        date_dialog.open()

Example().run()
