
from pyAmakCore.classes.agent import Agent
from  classroom import Classroom


class SmartLight(Agent):
    
    
    def __init__(self,amas,posX: float = 0,posY: float =0,niv_lum = 0):
        print("Create agent ")
        super().__init__(amas)
        self.posX = posX
        self.posY = posY
        self.niv_lum = niv_lum
        self.niv_lum_pred = niv_lum
        self.InitialLightLvl=0
        self.current_time = 0

    def get_posX(self):
        return self.posX

    def get_posY(self):
        return self.posY

    def on_cycle_begin(self) :
        print("on cycle begin Light")
        self.on_perceive()
        
    def on_cycle_end(self) -> None:
        print("Agent Cycle finished")

    def on_perceive(self):
        print("on perceive Light")
        if self.current_time<33:
            self.niv_lum = Classroom.global_bright[self.current_time]*100
            self.niv_lum_pred = Classroom.global_bright[self.current_time-1]*100
            self.on_act()
        else:
            self.on_cycle_end()    

    def on_act(self):
    	#ajuster la luminosité en fonction des capteurs incluts dedans  
        if self.niv_lum<20 :
            self.InitialLightLvl = 100  
            Classroom.global_bright[self.current_time] += 20/100
            print("New Value",Classroom.global_bright[self.current_time])
        elif self.niv_lum>60:
            self.InitialLightLvl = 0
            Classroom.global_bright[self.current_time] -= 20/100
        else:
            ecart=self.niv_lum-self.niv_lum_pred
            if ecart>0:
                self.InitialLightLvl-=ecart
                Classroom.global_bright[self.current_time] -= ecart/100
            else:
                self.InitialLightLvl+=ecart
                Classroom.global_bright[self.current_time] += ecart/100
        self.current_time +=1

