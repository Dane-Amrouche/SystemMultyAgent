from pyAmakCore.classes.communicating_agent import CommunicatingAgent


class Shutters(CommunicatingAgent):
    
    
    def __init__(self,posX: float = 0,posY: float =0,openlvl = 100):
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

    def light_on_subscribe(self):
    	#souscrir sur le topic salle/luminosité
    	pass

    def light_on_message(self):
    	#ajuster l'ouverture ou la fermeture des shutters en fonction des capteurs de luminosite 
    	#self.openlvl= self.sensorLightLvl
    	#a definir plutard

        pass