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


# calling the functions
my_remote = tv_remote()
my_remote.on = True
print(my_remote)
