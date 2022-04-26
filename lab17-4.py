# Author CCG 4/29/22

class tv_remote: # def class
    def __init__(self, channel=0, volume_level=0, on=False): # default values for tv
        self.channel = channel
        self.volume_level = volume_level
        self.on = on
    def __str__(self): # if else for print statement
        if self.on == True:
            return "The TV is at channel {0} at {1} volume.".format(self.channel, self.volume_level)
        else:
            return "The TV is not turned on."
    def turn_on(self): # def functions for the remote
        self.on = True
    def turn_off(self):
        self.on = False
    def volume_up(self, value):
        self.volume_level += value
    def volume_down(self, value):
        self.volume_level -= value
    def channel_up(self, value):
        self.channel += value
    def channel_down(self, value):
        self.channel -= value

# calling the functions
my_remote = tv_remote()
my_remote.on = True
my_remote.turn_on()
my_remote.turn_off()
my_remote.volume_up(10)
my_remote.volume_down(5)
my_remote.channel_up(10)
my_remote.channel_down(2)
my_remote.turn_on()
print(my_remote)

