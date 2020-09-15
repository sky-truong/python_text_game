class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()


class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass


class Death(object):

    quips = [
        """THUD! You open your eyes and find yourself on the floor.
        What a dream. You wonder what would have happened if you did
        differently.""",
        """BZZZZZ BZZZZZ BZZZZZ! You rummage to find your phone under
        the pillows and turn off the alarm. You blame the alarm for
        the bad choice but was it really the alarm's fault?""",
        """You wake up with a jolt. You're half glad it was all a
        dream, half regretful that you ended an adventure so lamely."""
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)


class HomeMorning(object):

    def enter(self):
        print(dedent("""
            It's summer. School is over. You can't find a job because
            there is a pandemic going on in the world. You've been
            doing the same things every day overand over. You're wandering
            around the house, you choose to go to:
            1. Living room
            2. Bed room
            3. Backyard
            """))

        area = input("> ").capitalize()

        if area == "Living room":
            return 'living_room'

        elif area == "Bed room":
            return 'bed_room'

        elif area == "Backyard":
            return 'backyard'

        else:
            print(dedent("""
                The summer heat and the boredom are getting to you.
                You decide to do 10 jumping jacks to clear your mind.
                """))
            return 'home_morning'

class HomeLivingRoom(object):

    def enter(self):
        print(dedent("""
            Let's see. You can either:
            1. Play game
            2. Do math
            3. Watch movies
            """))

        choice = input("> ").capitalize()

        if choice == "Play game":
            print(dedent("""
                You play game until you get a headache. Both your game
                console and your body are now overheated. You try to
                reason that you did make some progress and you feel
                alright with the wasted time.
                """))
            return 'home_night'

        elif choice == "Do math":
            print(dedent("""
                You do math problems until your brain shuts off and your
                vision gets dim. You feel satisfied. At least you contribute
                to your education. You wonder when you'll get to use
                these maths in real life.
                """))
            return 'home_night'

        elif choice == "Watch movies":
            print(dedent("""
                You watch movies until your eyes feel glued to the screen.
                The couch is now indented with your body shape. You can no
                longer process what's going on in the movies. You feel a
                bit entertained."""))
            return 'home_night'

        else:
            print(dedent("""
            The summer heat and the boredom are getting to you.
            You decide to do 10 jumping jacks to clear your mind.
            """))
            return 'living_room'

class HomeBedRoom(object):

    def enter(self):
        print(dedent("""
            Let's see. You can either:
            1. Do laundry
            2. Exercise
            """))

        choice = input("> ").capitalize()

        if choice == "Do laundry":
            print(dedent("""
                You feel energized and decide to clean up your room, too.
                The room smells great with fresh, laundered bedsheets
                and clothes. Everything is neat and organized. You feel
                proud of yourself.
                """))
            return 'home_night'

        elif choice == "Exercise":
            print(dedent("""
                You commit yourself to 5 sets of 15 squats, 15 lunges,
                10 push-ups, and 10 pull-ups. You are so out of shape
                and it takes forever to finish the exercise but you
                manage. You feel you can take on the world!
                """))
            return 'home_night'

        else:
            print(dedent("""
                The summer heat and the boredom are getting to you.
                You decide to do 10 jumping jacks to clear your mind.
                """))
            return 'bed_room'

class HomeBackyard(object):

    def enter(self):
        print(dedent("""
            It's a beautiful sunny day. You're glad you've decided
            to come outside. You pace around, checking on the plants
            and flowers. You play basketball and put your music on the
            speakers. You enjoy a day in the sun.
            """))
        return 'home_night'

class HomeNight(object):

    def enter(self):
        print(dedent("""
            After dinner, you check out the news to see if the situation
            is getting better. Parts of the world seem to get chaotic.
            You wonder how the pandemic is affecting the sick physically,
            and the healthy mentally. The world seems pretty unreal.

            You toss and turn in bed, waiting for sleep to come. Your
            mind slowly gets hazy and...BANG!!! You get up immediately.
            'What's that sound?'. You think it's from the backyard so
            you make your way there cautiously, holding the night lamp
            for assurance.

            There's a metallic egg-shaped capsule thing sitting on your
            lawn. As you approach, a door slides opens and you can hear
            a voice: 'Welcome to Space Retreat. Let's start your journey.'
            Curious and having nothing better to do. You enter the egg
            ship and hope for the best.
            """))

        return 'egg_ship'


class EggShip(object):

    def enter(self):
        print(dedent("""
            This ship is amazing. The ride is quiet. You don't feel
            sick in the stomach at all. You wonder why astronauts have
            to go through such intensive trainings. The whole ship is
            transparent from the inside so you can see everything around.
            It's like you're floating around in space.

            'Destination: Planet Red in 5 minutes.' The voice you
            heard in ship announces. Time for your first planet!
            """))

        return 'planet_red'


class PlanetRed(object):

    def enter(self):
        print(dedent("""
            The ship lowering into what looks like a parking zone. There
            are many other funny looking ship: cones, mugs, pots, etc.
            Maybe the technology is so advanced that aerodynamics
            do not even matter anymore?

            'If you want to be picked up, tap twice on the bracelet.
            There has to be 5 meter radius clearance for landing.
            Else come back to the this location. Enjoy your exploration.'
            You notice that there is a silver bracelet on your left wrist.
            You have no idea when you got it, but it'll be convenient if
            it starts to rain.

            You join the line up in front of the entrance gate. The
            'people' here are a mix and match of what you've seen in
            sci-fi movies. Maybe the design folks have travelled to
            these planets as well, but keep it a secret? You wonder if
            you should sketch the 'people' you see here and make some
            money when you get back to Earth.

            It's finally your turn at the booth. The agent looks like a
            giant rabbit. A very well-dressed with a nice fitted vest
            and a modern pair of glasses. The agent looks at you and
            said: 'Ah, a first time traveller. Welcome to Planet Red.
            You've come on a perfect day. Enjoy your stay.' Being a
            polite person, you respond:

            1. "What a smart rabbit you are! How did you know it's my
            first time here?""

            2. "Well, thank you very much for your warm welcome Mr. Rabbit.
            I shall."

            3. "Can I take a picture with you? I want to show everyone
            when I get back to Earth."

            (Enter a number)
            """))

        choice = int(input("> "))

        if choice == 1:
            print(dedent("""
                The rabbit agent is not impressed: 'The universal ID
                shows everything. Also, do not call people here with
                your Earthling's classification. We're called different
                here.'

                Embarrassed, you stutter your thanks and get on quickly.
                """))
            return 'planet_red_city'

        elif choice == 2:
            print(dedent("""
                The rabbit agent is amused: 'Please do not call people
                here with your Earthling's classification. We're called
                different here.'

                Curious. You ask for the correct way of calling.
                Apparently, the agent's race is called Tibbar.
                """))
            return 'planet_red_city'

        elif choice == 3:
            print(dedent("""
                The rabbit agent is happy: 'Of course!' You snap a quick
                selfie with the agent.

                Now you can brag about space travel to your friends and
                family when you get back to Earth.
                """))
            return 'planet_red_city'

        else:
            print(dedent("""
                The rabbit agent looks confused. He doesn't understand
                what you're talking about. Everyone behind you seems
                impatient.

                You are forced to move on without articulating anything
                properly. People probably think you're an idiot.
                """))
            return 'planet_red_city'

class PlanetRedCity(object):

    def enter(self):
        print(dedent("""
            The city is bustling with activities and noise. Everything
            is so very lively. This must be a popular tourist planet. You
            look at the street signs and decide to go down:
            1. Food street
            2. Beach street
            3. Merchant street
            """))

        choice = input("> ").capitalize()

        if choice == "Food street":
            print(dedent("""
                The delicious aroma in the air makes your stomach rumble
                loudly. You don't have any money but you're in luck!
                They're handing out samples. You can't wait to try out
                every stall.
                """))
            return 'planet_red_event'

        elif choice == "Beach street":
            print(dedent("""
                Instead of saltiness, the air at the beach smells like
                crushed mint leaves. The ocean has a pinkish color.
                You look for a place to sit to enjoy the fresh air and
                the sea breeze.
                """))
            return 'planet_red_event'

        elif choice == "Merchant street":
            print(dedent("""
                There are constant exchanges of bargaining, advertising
                and trading. Everything looks so exotic and the energetic
                atmosphere fills you with excitement. You can't decide
                which stall to check out first.
                """))
            return 'planet_red_event'

        else:
            print(dedent("""
                Mhmmm...where to go? Let's try that again.
                """))
            return 'planet_red_city'

class PlanetRedEvent(object):

    def enter(self):
        print(dedent("""
            Suddenly, the ground starts shaking violently. You struggle
            to balance yourself as you see big cracks forming on the
            ground. A giant mole looking creature leaps out from the
            crack right in front of you and yells: 'Fight or Forfeit!'.
            From the corner of your eye, you can see more giant mole
            creatures yelling the same thing to other tourists and local
            inhabitants. Amidst all the screaming responses and confusion,
            you reply:
            """))

        reply = input("> ").capitalize()

        if reply == "Fight":
            print(dedent("""
                Very well. I challenge you to 3 rounds of rock, paper and
                scissors. Let's go! Rock, Paper, Scissors:
                """))

            round = 1
            win = loss = 0
            while round < 3:
                choice = input("> ").capitalize()
                result = RockPaperScissor(choice)

                if result:
                    win += 1
                else:
                    loss += 1

                round += 1


            return 'planet_red_end'

        elif reply == "Forfeit":
            print(dedent("""
                'How boring! Well, it's your decision.' The mole says
                disappointedly. It puts a large bag over your head and
                spins you around.
                """))
            return 'planet_red_end'

        else:
            print(dedent("""
                What was that? Let's try again.
                """))
            return 'planet_red_event'

class PlanetRedEnd(object):

    def enter(self):
        print(dedent("""
            After their antics, the moles wave everyone goodbye and jump
            back in the cracks. 'See you next month!', they say. Everyone
            is laughing and chatting about the event. Apparently, it's
            some sort of monthly game on Planet Red. You remember how the
            agent welcomed you coming on a 'perfect day'.

            Time to go and explore another planet and check more interesting
            events!
            """))
        return 'planet_k'

class PlanetK(object):

    def enter(self):
        print(dedent("""
            Your next destination is Planet K. It's a complete chaos at
            the parking zone. Many ships are taking off as you're coming
            down. There are smokes in the distance to different directions.
            Maybe the event here is a bit more intense?

            You find people wearing brown cloaks running around in the city,
            trying to put off fires from burning houses. One runs towards
            you: 'If you've come to visit, this is a bad time. Our King's
            orb is out of control and no one knows if we'll survive this
            disaster. Many citizens and visitors have gone to the castle
            offering help, but no one has returned and the situation is
            only getting worse. Leave while you still can!'

            Being a good-hearted explorer, you ask for direction to the
            castle and head there immediately! You have to get there on
            foot as no one is around the direct air traffic and accidents
            might happen.

            The citizen gives you some food to eat on the way. First, you
            have to cross a wooden bridge to the north of the city.
            """))
        return 'planet_k_planet'

class PlanetKBridge(object):

    def enter(self):
        print(dedent("""
            It's one of those classic wobbly, damaged bridge that has
            ropes as handrails. Some of the steps are also missing. You
            start to cross carefully, trying not to look down below.

            When you reach the middle of the bridge, a small flock of
            pigeons fly by and perch on the ropes a bit ahead of you.
            You can feel their stare and it makes you uneasy.
            You decide to:
            1. Shoo them away.
            2. Let them be.
            3. Reach into your pockets.

            (Enter a number)
            """))

        choice = int(input("> "))

        if choice == 1:
            print(dedent("""
                The birds get angry and they start pecking at you. You
                try to cover yourself but lose your footing and fall over
                the bridge.
                """))
            return 'death'

        elif choice == 2:
            print(dedent("""
                The birds keep staring at you as you pass them by. You
                cross the bridge without further problem.
                """))
            self.fed = False

        elif choice == 3:
            print(dedent("""
                You find some food scraps and throw them behind you.
                The birds fly over and nibble at them. You cross the
                bridge without further problem.
                """))
            self.fed = True

        else:
            print("What was that? Let's try again.")
            return 'planet_k_bridge'

        print(dedent("""
            You reach the other side of the bridge. As you approach the
            forest, the pigeons fly over and perch on the branches ahead
            of you.
            """))

        if self.fed:
            print(dedent("""
                'As thanks for giving us food, we'll give you a this token
                and a tip. One always lies and one always tells the truth.
                It gives you a second chance for the forest challenge.
                Goodluck!'

                You thank and pigeons and enter the forest.
                """))

        else:
            print(dedent("""
                The pigeons keep staring at you as you enter the forest.
                Do you have something on your face?
                """))

class PlanetKForest(object):

    def __init__(self):
        self.bridge = PlanetKBridge()

    def enter(self):
        self.bridge.enter()

        print(dedent("""
            The forest is actually quite nice. It reminds you of the
            hiking on Earth. You trod leisurely and can see the end of
            the forest in view. This is easier than you thought!

            Out of nowhere, there is a thudering roar and a 2-headed lion
            jumps right next to you. The heads speak at the same time:
            'You can only continue if you can solve our riddle. Else, you'll
            become dinner. Let the riddle begin:'

            The left head growls: 'I'm not a liar.'

            The right head goes: 'We both speak the truth.'

            'Choose the one that speaks the truth:'
            1. Left
            2. Right
            3. Both
            4. None

            """))

        choice = input("> ").capitalize()

        if choice == 'Left':
            print(dedent("""
                'Very good. You can move on. I hope you can help the
                King.'
                """))
            return 'planet_k_castle'

        elif choice == 'Right' and self.bridge.fed:
            print(dedent("""
                'Too bad. I guess you aren't very bright. But I see you
                have a token from the pigeons so I'll give a second chance.
                Here is the question: For dinner, I want to pick 2 dishes
                out of pork, fish, lamb, beef, rabbit, and deer. How many
                different combinations can I have?'
                """))

                answer = int(input("> "))

                if answer == 15:
                    print(dedent(""""
                        'Very good. You can move on. I hope you can help the
                        King.'
                        """))
                    return planet_k_castle

                else:
                    print(dedent("""
                        'Wrong again. Your journey ends here. Goodbye.'
                        As soon as the lion finishes speaking. The ground
                        below your feet disappears. You've been standing on
                        a trap the whole time.
                        """))
                    return 'death'

        else:
            print(dedent("""
                'Wrong again. Your journey ends here. Goodbye.'
                As soon as the lion finishes speaking. The ground
                below your feet disappears. You've been standing on
                a trap the whole time.
                """))
            return 'death'

class PlanetKCastle(object):

    def enter(self):
        print(dedent("""
            You can see people in fancy-looking robes running around.
            There are books and scrolls lying everywhere on the ground.
            Are they trying to look for some kind of ancient spell?

            As you present yourself to the King, he let out a sigh:
            "Another adventurer. Many have come before you and all have
            failed. But whatever, try your luck."

            A guard then leads you to a separate room that has a really
            futuristic look, the kind you would see in a sci-fi set in
            the future movie. In the middle of the room is "the orb".
            It looks like a floating spherical computer.

            Apparently, this planet is powered on a single powerful
            computer. The older generations were highly intelligent.
            They built the super computer in order to make life easier,
            but fearing that people would go lazy, they decided
            to put in a calibration system that tests their successors
            knowledge to make sure next generations keep learning and
            improve. Murphy's law happened, the citizens shunned the
            ancients' knowledge, started to believe in magic, basically
            advanced backwards...

            "But I'm from Earth. I won't be able to answer questions about
            your planet.", you voice your concern.

            "Oh you can tell the orb your planet and it will ask you
            relevant questions. The ancients set up the orb to collect
            wisdom from as many living planets in the galaxy as it could.
            I guess they predicted our failure in maintaining the orb and
            placed hope in a traveller to aid us.", the guard explains.

            
            """))

class PlanetKEscape(object):

    def enter(self):
        pass


class Finished(object):

    def enter(self):
        pass
