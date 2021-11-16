from pyAmakCore.classes.communicating_agent import CommunicatingAgent


class SmartLight(CommunicatingAgent):
    
    
    def __init__(self,posX: float = 0,posY: float =0,niv_lum = 0):
        super().__init__(amas)
        self.posX = posX
        self.posY = posY
        self.niv_lum = niv_lum
        self.sensorLightLvl=100

    def get_posX(self):
        return self.posX

    def get_posY(self):
        return self.posY

    def get_niv_lum(self):
        return self.get_niv_lum

    def light_on_subscribe(self):
    	#souscrir sur le topic salle/luminosité
    	pass

    def light_on_message(self):
    	#ajuster la luminosité en fonction des capteurs 
    	#self.niv_lum=100-sensorLightLvl (valeur_envoyee_par_LightSensor
    	#a definir plutard

        pass