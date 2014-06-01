class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

rolling_stone = Song(["Once upon a time you dressed so fine \n" 
					"You threw the bums a dime in your prime, didn't you? \n"
					"People'd call, say, 'Beware doll, you're bound to fall' \n"
					"You thought they were all kiddin' you \n"
					"You used to laugh about \n"
					"Everybody that was hangin' out \n"
					"Now you don't talk so loud \n"
					"Now you don't seem so proud \n"
					"About having to be scrounging for your next meal.\n"])


rolling_stone.sing_me_a_song()
