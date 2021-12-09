from pyAmakCore.classes.agent import Agent



class Shutters(Agent):
    
    
    def __init__(self,amas,posX: float = 0,posY: float =0,openlvl =100):
        super().__init__(amas)
        self.posX = posX
        self.posY = posY
        self.openlvl = openlvl
        self.sensorLightLvl=0
        self.current_time = 0
        self.status="Close"

    def get_posX(self):
        return self.posX

    def get_posY(self):
        return self.posY

    def get_openlvl(self):
        return self.get_openlvl

#    def on_cycle_begin(self):
 #       print("on cycle begin Shetters")
  #      self.on_perceive()
   # def on_cycle_end(self) -> None:
    #    print("Agent Shutters Cycle finished")

    def on_perceive(self) -> None:
        print("on_perceive Shutters")
        self.current_time+=1
        self.on_act()


    def on_act(self):
        if self.current_time < 33 :
            self.status="Open"
            print("Status",self.status)
        else:
            self.status="Close"    
            print("Status",self.status)
