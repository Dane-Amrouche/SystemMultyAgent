#my amas

from light import SmartLight
from pyAmakCore.classes.amas import Amas
from classroom import Classroom
from light import SmartLight
from shutters import Shutters
import time


class MyAmas(Amas):
   
    NbrLights=8
   

    def __init__(self,environment : Classroom):
        super().__init__(environment)
        print("created AMAS")
    
        
        
    
    def on_initialization(self):
        print("intialized AMAS")
        #self.env.on_initialization()

    def on_initial_agents_creation(self):
        agents=[]
       
        for i in range(6):
            print("Create agent Smart_Light", i)
            agents.append(SmartLight(self)) 

        for i in range(4):
            print("Create agent Shutters", i)
            agents.append(Shutters(self))     
        

        self.add_agents(agents)
        self.add_pending_agent()

    


    def on_cycle_begin(self):
        print("Launch agent light")
        print("Launch agent shutters")
        for i in range(33):
            #time.sleep(0.5)
            self.get_environment().on_cycle_begin()
            
            for x in self.get_agents() :
                x.on_cycle_begin()

            
            for x in self.get_agents() :
                x.on_perceive() 
           
        self.on_cycle_end()
        


    def on_cycle_end(self) -> None:
        print("on_cycle_end amas") 
        #for i in range(34) :
         #   print("current_time {} ,Light_Level {}".format(i ,Classroom.global_bright[i]))

t = Classroom()
c=MyAmas(t)
c.on_cycle_begin()
