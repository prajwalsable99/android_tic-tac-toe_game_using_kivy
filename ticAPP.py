import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

s="X"
n=0
class ticGame(GridLayout):
    l=None
   

    def __init__(self, **kwargs):
        super(ticGame, self).__init__(**kwargs)
        self.cols = 3
        
        self.add_widget(Label(text="tic_tae_toe\nby prajwal"))
        self.add_widget(Label(text="player: x"))
        self.add_widget(Label(text="player :O"))

        self.l=[None for i in range(9)]
        self.s="X"
        self.add_t()

        self.add_widget(Label(text="----"))

        self.results="prajsa99@gmail.com"
        self.res=Label(text=self.results)
        self.add_widget(self.res)

        self.add_widget(Label(text="----"))
        
 
        
    def add_t(self):

        for i in range(0,9):
            tile = Button(text="_")
            tile.bind(on_press=self.getxo)
            self.l[i]=tile
           
            self.add_widget(tile)

            
    def _restart_board(self):
        for i in self.l:
            
            i.text = '_'
        
    def win(self):
        global n
        #x
        if self.l[0].text==self.l[1].text==self.l[2].text and self.l[0].text!="_":
            n=0
            return self.l[0].text

        elif self.l[3].text==self.l[4].text==self.l[5].text and self.l[3].text!="_":
            n=0
            return self.l[3].text
        
        elif self.l[6].text==self.l[7].text==self.l[8].text and self.l[6].text!="_":
            n=0
            return self.l[6].text
        #dia

        elif self.l[0].text==self.l[4].text==self.l[8].text and self.l[0].text!="_":
            n=0
            return self.l[0].text
        
        elif self.l[2].text==self.l[4].text==self.l[6].text and self.l[2].text!="_":
            n=0
            return self.l[2].text
        #y
        elif self.l[0].text==self.l[3].text==self.l[6].text and self.l[0].text!="_":
            n=0
            return self.l[0].text

        elif self.l[1].text==self.l[4].text==self.l[7].text and self.l[1].text!="_":
            n=0
            return self.l[1].text

        elif self.l[2].text==self.l[5].text==self.l[8].text and self.l[2].text!="_":
            n=0
            return self.l[2].text
        #no
        else:

            return "no"
        
        
   
    def getxo(self,event):

        global s
        global n
        print(n)
        
        if n==9:
            n=0
            self._restart_board()
        

            

          
            

        if event.text=="_" and s=="X" :
            event.text="X"
            s="O"
            
            n=n+1
            
            
            
            
        if event.text=="_" and s=="O"  :
            event.text="O"
            s="X"
           
            n=n+1
        if self.win()=="X" : 
            print("winner is",self.win())
            self.res.text=f"player X WON"
            
            self._restart_board()
        
        if  self.win()=="O":
            print("winner is",self.win())
            self.res.text=f"player O WON"
            
            self._restart_board()
   
            
            
            
            

        

        
            
        
        
            
    

class ticApp(App):
    def build(self):
        return ticGame()

   


ticApp().run()
