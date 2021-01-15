# TV controller
# Create a simple prototype of a TV controller in Python. It’ll use the following commands:
# first_channel() - turns on the first channel from the list.
# last_channel() - turns on the last channel from the list.
# turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
# next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
# previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
# current_channel() - returns the name of the current channel.
# is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes", if the channel N or 'name' exists in the list, or "No" - in the other case.
# The default channel turned on before all commands is №1.
# Your task is to create the TVController class and methods described above.
# CHANNELS = ["BBC", "Discovery", "TV1000"]
# class TVController:
# controller = TVController(CHANNELS)
# controller.first_channel() == "BBC"
# controller.last_channel() == "TV1000"
# controller.turn_channel(1) == "BBC"
# controller.next_channel() == "Discovery"
# controller.previous_channel() == "BBC"
# controller.current_channel() == "BBC"
# controller.is_exist(4) == "No"
# controller.is_exist("BBC") == "Yes"
# ```

channels = ["BBC", "Discovery", "TV1000", "History", "MTV"]


class TVController:
    def __init__(self, channels):
        self.channels = channels
        self.default_ch = 0

    def first_channel(self):
        channel = self.channels[0]
        self.default_ch = 0
        print(channel)

    def last_channel(self):
        channel = self.channels[-1]
        self.default_ch = 0
        print(channel)

    def turn_channel(self, number):
        number = int(number)
        try:
            channel = self.channels[number-1]
            print(channel)
        except IndexError:
            print(f'channel #{number} is not in channel list')

    def next_channel(self):
        self.default_ch += 1
        if self.default_ch > len(self.channels) - 1:
            self.default_ch = 0
            print(self.channels[self.default_ch])
        else:
            print(self.channels[self.default_ch])

    def previous_channel(self):
        if self.default_ch == 0:
            self.default_ch = len(self.channels)
        self.default_ch -= 1
        print(self.channels[self.default_ch])

    def current_channel(self):
        print(f'The current channel is - {self.channels[self.default_ch]}')

    def is_exist(self, ch):
        res = False
        if type(ch) is str:
            for value in self.channels:
                if value.lower() == ch.lower():
                    res = True
        elif type(ch) is int:
            if ch in range(len(self.channels)+1):
                res = True
        if res:
            print('Yes')
        else:
            print('NO')


tv = TVController(channels)
tv.current_channel()
#tv.first_channel()
#tv.last_channel()
#tv.turn_channel(5)
#tv.next_channel()
#tv.first_channel()
#tv.next_channel()
#tv.next_channel()
#tv.first_channel()
#tv.next_channel()
#print(tv.default_ch)
#tv.previous_channel()
#tv.previous_channel()
#tv.previous_channel()
#tv.previous_channel()
#print(tv.default_ch)
#tv.previous_channel()
#tv.previous_channel()
#tv.previous_channel()
#tv.current_channel()
tv.is_exist(5)
tv.turn_channel(3)
#print(tv.default_ch)
