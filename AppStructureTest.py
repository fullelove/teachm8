from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.properties import (NumericProperty, ReferenceListProperty, ObjectProperty)
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle, Ellipse

Builder.load_string("""
<CoursesScreen>:
    FloatLayout: 
                
        Label:
            text: "Stephanie's Courses"
            font_size: 18
            color: '#6897bb'
            pos_hint: {'x': -0.3, 'y': 0.4}
                            
        Button:
            text: "Physics"
            size_hint: (0.75, 0.2)
            pos_hint: {'x': 0.125, 'y': 0.65}
            bold: True
            background_color: '#6897bb'
            on_press: root.manager.current = 'GCSE_Physics'
                   
        Button:
            text: "Chemistry"
            size_hint: (0.75, 0.2)
            pos_hint: {'x': 0.125, 'y': 0.4}
            bold: True
            background_color: '#6897bb'
            
        Button:
            text: "Business"
            size_hint: (0.75, 0.2)
            pos_hint: {'x': 0.125, 'y': 0.15}
            bold: True
            background_color: '#6897bb'           

        Button:
            text: "Courses"
            size_hint: (0.25, 0.075)
            pos_hint: {'x': 0, 'y': 0}
            bold: True
            background_color: '#6897bb'
            on_press: root.manager.current = 'Courses'
               
        Button:
            text: "Social"
            size_hint: (0.25, 0.075)
            pos_hint: {'x': 0.25, 'y': 0}
            bold: True
            background_color: '#6897bb'
            on_press: root.manager.current = 'Social'  
                
        Button:
            text: "Quests"
            size_hint: (0.25, 0.075)
            pos_hint: {'x': 0.5, 'y': 0}
            bold: True
            background_color: '#6897bb'
               
        Button:
            text: "Settings"
            size_hint: (0.25, 0.075)
            pos_hint: {'x': 0.75, 'y': 0}
            bold: True
            background_color: '#6897bb'

        Button:
            text: "Home"
            size_hint: (0.075, 0.075)
            pos_hint: {'x': 0.9, 'y': 0.9}
            bold: True
            background_color: '#6897bb'         
            #on_press: root.manager.current = 'Courses'    
        
<GCSEPhysicsScreen>:          
    FloatLayout:
           
        Label:
            text: "Physics Course"
            font_size: 18
            color: '#6897bb'
            pos_hint: {'x': -0.3, 'y': 0.4}

        Button:
            text: "Courses"
            size_hint: (0.25, 0.075)
            pos_hint: {'x': 0, 'y': 0}
            bold: True
            background_color: '#6897bb'
            on_press: root.manager.current = 'Courses'
               
        Button:
            text: "Social"
            size_hint: (0.25, 0.075)
            pos_hint: {'x': 0.25, 'y': 0}
            bold: True
            background_color: '#6897bb'
            on_press: root.manager.current = 'Social'  
                
        Button:
            text: "Quests"
            size_hint: (0.25, 0.075)
            pos_hint: {'x': 0.5, 'y': 0}
            bold: True
            background_color: '#6897bb'
                
        Button:
            text: "Settings"
            size_hint: (0.25, 0.075)
            pos_hint: {'x': 0.75, 'y': 0}
            bold: True
            background_color: '#6897bb'
        
        Button:
            text: "Home"
            size_hint: (0.075, 0.075)
            pos_hint: {'x': 0.9, 'y': 0.9}
            bold: True
            background_color: '#6897bb'
            #on_press: root.manager.current = 'Courses'   


        Button:
            text: "lesson 1"
            size_hint: (0.075, 0.075)
            pos_hint: {'x': 0.6, 'y': 0.8}
            bold: True
            background_color: '#FF0000'
            #on_press: root.manager.current = 'Courses'
                  
        Button:
            text: "lesson 2"
            size_hint: (0.075, 0.075)
            pos_hint: {'x': 0.5, 'y': 0.7}
            bold: True
            background_color: '#FF0000'
            #on_press: root.manager.current = 'Courses'
            
        Button:
            text: "lesson 3"
            size_hint: (0.075, 0.075)
            pos_hint: {'x': 0.4, 'y': 0.6}
            bold: True
            background_color: '#FF0000'
            #on_press: root.manager.current = 'Courses'


        Button:
            text: "lesson 4"
            size_hint: (0.075, 0.075)
            pos_hint: {'x': 0.5, 'y': 0.5}
            bold: True
            background_color: '#FF0000'
            #on_press: root.manager.current = 'Courses'



        Button:
            text: "lesson 5"
            size_hint: (0.075, 0.075)
            pos_hint: {'x': 0.6, 'y': 0.4}
            bold: True
            background_color: '#FF0000'
            #on_press: root.manager.current = 'Courses'

        Button:
            text: "lesson 6"
            size_hint: (0.075, 0.075)
            pos_hint: {'x': 0.5, 'y': 0.3}
            bold: True
            background_color: '#FF0000'
            #on_press: root.manager.current = 'Courses'

        Button:
            text: "lesson 7"
            size_hint: (0.075, 0.075)
            pos_hint: {'x': 0.4, 'y': 0.2}
            bold: True
            background_color: '#FF0000'
            #on_press: root.manager.current = 'Courses'

        Button:
            text: "lesson 8"
            size_hint: (0.075, 0.075)
            pos_hint: {'x': 0.5, 'y': 0.1}
            bold: True
            background_color: '#FF0000'
            #on_press: root.manager.current = 'Courses'

        Button:
            text: "Time Challenge"
            size_hint: (0.075, 0.075)
            pos_hint: {'x': 0.6, 'y': 0.6}
            bold: True
            background_color: '#FFD700'
            #on_press: root.manager.current = 'Courses'


        Button:
            text: "Time Challenge"
            size_hint: (0.075, 0.075)
            pos_hint: {'x': 0.4, 'y': 0.4}
            bold: True
            background_color: '#FFD700'
            #on_press: root.manager.current = 'Courses'

<SocialScreen>:          
    FloatLayout:
           
        Label:
            text: "Stephanie's Social"
            font_size: 18
            color: '#6897bb'
            pos_hint: {'x': -0.3, 'y': 0.4}

        Button:
            text: "Courses"
            size_hint: (0.25, 0.075)
            pos_hint: {'x': 0, 'y': 0}
            bold: True
            background_color: '#6897bb'
            on_press: root.manager.current = 'Courses'
               
        Button:
            text: "Social"
            size_hint: (0.25, 0.075)
            pos_hint: {'x': 0.25, 'y': 0}
            bold: True
            background_color: '#6897bb'
            on_press: root.manager.current = 'Social'  
                
        Button:
            text: "Quests"
            size_hint: (0.25, 0.075)
            pos_hint: {'x': 0.5, 'y': 0}
            bold: True
            background_color: '#6897bb'
                
        Button:
            text: "Settings"
            size_hint: (0.25, 0.075)
            pos_hint: {'x': 0.75, 'y': 0}
            bold: True
            background_color: '#6897bb'
        
        Button:
            text: "Home"
            size_hint: (0.075, 0.075)
            pos_hint: {'x': 0.9, 'y': 0.9}
            bold: True
            background_color: '#6897bb'
            #on_press: root.manager.current = 'Courses' 

        Button:
            text: "Messages"
            size_hint: (0.1, 0.09)
            pos_hint: {'x': 0.9, 'y': 0.8}
            bold: True
            background_color: '#FFD700'
            #on_press: root.manager.current = 'Courses'    

        Button:
            text: "Shop"
            size_hint: (0.1, 0.09)
            pos_hint: {'x': 0.9, 'y': 0.68}
            bold: True
            background_color: '#FFD700'
            #on_press: root.manager.current = 'Courses'
            
        Button:
            text: "8 Day Streak!"
            size_hint: (0.1, 0.09)
            pos_hint: {'x': 0.9, 'y': 0.56}
            bold: True
            background_color: '#FFD700'
            #on_press: root.manager.current = 'Courses'
            
        Button:
            text: "Shop"
            size_hint: (0.1, 0.09)
            pos_hint: {'x': 0.9, 'y': 0.44}
            bold: True
            background_color: '#FFD700'
            #on_press: root.manager.current = 'Courses'                        

        Button:
            text: "Customise My Avatar"
            size_hint: (0.1, 0.09)
            pos_hint: {'x': 0.9, 'y': 0.32}
            bold: True
            background_color: '#FFD700'
            #on_press: root.manager.current = 'Courses'

        Button:
            text: "Post Status"
            size_hint: (0.1, 0.09)
            pos_hint: {'x': 0.9, 'y': 0.2}
            bold: True
            background_color: '#FFD700'
            #on_press: root.manager.current = 'Courses'


""")




class CoursesScreen(Screen):
    pass
    

class GCSEPhysicsScreen(Screen):
    pass

class SocialScreen(Screen):
    pass

    


class AppStructureTest(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(CoursesScreen(name = 'Courses'))
        sm.add_widget(GCSEPhysicsScreen(name = 'GCSE_Physics'))
        sm.add_widget(SocialScreen(name = 'Social'))
        return sm


if __name__ == '__main__':
    AppStructureTest().run()
