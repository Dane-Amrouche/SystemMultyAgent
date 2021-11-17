from pyAmakCore.classes.agent import Agent


class Shutters(Agent):
    
    
    def __init__(self,posX: float = 0,posY: float =0,openlvl =100):
        super().__init__(amas)
        self.posX = posX
        self.posY = posY
        self.openlvl = openlvl
        self.sensorLightLvl=0

    def get_posX(self):
        return self.posX

    def get_posY(self):
        return self.posY

    def get_openlvl(self):
        return self.get_openlvl

    def on_perceive(self):  #on_subscribe
    	#souscrir sur le topic salle/luminosité
    	pass

    def on_act(self):
    	#ajuster l'ouverture ou la fermeture des shutters en fonction des capteurs de luminosite 
    	#self.openlvl= self.sensorLightLvl
    	#a definir plutard
        pass