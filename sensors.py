import paho.mqtt3.client as 



class Sensor():
    def __init__(self,posX: float = 0,posY: float = 0):
        self.posX=posX
        self.posY=posY  

    def get_posX(self):
        return self.posX    

    def get_posY(self):
        return self.posY

# light sensor
class LightSensor(Sensor):
    def __init__(self,niv_lum=0):
        super().__init__()
        self.niv_lum=niv_lum

    def get_light(self):
        #appeler la fonction get_lum() qui se trouve au niveau de la classe ClassRoom(Env)

        pass   

    def light_on_publish(self):
        #on_pulish sur le topic salle/luminosité pour informer les autres agents 
        pass     

# Motion Sensor
class MotionSensor(Sensor):
    def __init__(self,presence=False):
        super().__init__()
        self.presence=presence

    def get_presence(self):
        return self.presence

    def presence_on_publish(self):
        # signaler une presence et Maj de l'etat de la variable presence.
        pass


