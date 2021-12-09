from pyAmakCore.classes.agent import Agent
import time


class Shutters(Agent):
    
    
    def __init__(self,amas,posX: float = 0,posY: float =0,openlvl =100):
        super().__init__(amas)
        print("on cycle begin Shetters")
        print("on_perceive Shutters")
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

    def on_cycle_begin(self):
        self.on_perceive()

    def on_cycle_end(self) -> None:
        print("Agent Shutters Cycle finished")

    def on_perceive(self) -> None:
        self.on_act()
        self.current_time+=1


    def on_act(self):

        if self.current_time <= 18 :
            self.status="Open"
            if self.current_time==0:
                print("Status",self.status, " à ","7 h")
        else:
            self.status="Close" 
            if self.current_time==33:
                print("Status",self.status, " à "," 19 h")


        """
        if self.current_time >6 and self.current_time <= 18 :
            self.status="Open"
            print("Status",self.status, " à ",self.current_time," h")
        else:
            self.status="Close" 
            if self.current_time==24:
                print("Status",self.status, " à ","00h")
            elif self.current_time>24:
                self.current_time=1
                print("Status",self.status, " à ",self.current_time," h")
                self.current_time+=1
            else:    
                print("Status",self.status, " à ",self.current_time," h")        
        """
     
