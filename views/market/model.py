from mesa import Model
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector

from market.agents import amazonprime, netflix, disneyplus
#from market.agents import appletv
from market.schedule import RandomActivationByType


class market(Model):
    height = 30
    width = 30

    initial_amazonprime = 25
    initial_netflix = 50
    #initial_appletv = 15
    initial_disneyplus = 10
    content_amazonprime = 5
    content_netflix = 5
    content_disneyplus = 5
    quality_amazonprime = 5
    quality_disneyplus = 10
    quality_netflix = 15

    verbose = False

    description = 'A model for simulating spread of Corona Virus using SIR modelling.'

    def __init__(self, height=30, width=30,
                 initial_amazonprime=25, 
                 initial_netflix=50, 
                 #initial_appletv=15, 
                 initial_disneyplus = 10,
                 content_disneyplus = 5,
                 content_netflix = 5,
                 content_amazonprime = 5,
                 quality_amazonprime = 5,
                 quality_disneyplus = 10,
                 quality_netflix = 15
                ):
        super().__init__()
        # Set parameters
        self.height = height
        self.width = width
        self.initial_amazonprime = initial_amazonprime
        #self.initial_appletv = initial_appletv
        self.initial_disneyplus = initial_disneyplus
        self.initial_netflix = initial_netflix
        
        self.schedule = RandomActivationByType(self)
        self.grid = MultiGrid(self.height, self.width, torus=True)
        self.content_amazonprime = content_amazonprime
        self.content_disneyplus = content_disneyplus
        self.content_netflix = content_netflix

        self.quality_amazonprime = quality_amazonprime
        self.quality_disneyplus = quality_disneyplus
        self.quality_netflix = quality_netflix
        #Collecting the data for Agents
        self.datacollector = DataCollector(
            {"amazonprime": lambda m: m.schedule.get_type_count(amazonprime),
             "netflix": lambda m: m.schedule.get_type_count(netflix),
             "disneyplus": lambda m: m.schedule.get_type_count(disneyplus)
             #"appletv": lambda m: m.schedule.get_type_count(appletv)
            })

        #Creating newamazonprime
        for i in range(self.initial_amazonprime):
            x = self.random.randrange(self.width)
            y = self.random.randrange(self.height)
            newamazonprime = amazonprime(self.next_id(), (x, y), self)
            self.grid.place_agent(newamazonprime, (x, y))
            self.schedule.add(newamazonprime)

        #Creating netflix
        for i in range(self.initial_netflix):
            x = self.random.randrange(self.width)
            y = self.random.randrange(self.height)
            newnetflix = netflix(self.next_id(), (x, y), self)
            self.grid.place_agent(newnetflix, (x, y))
            self.schedule.add(newnetflix)
        
        #Creating disneyplus
        for i in range(self.initial_disneyplus):
            x = self.random.randrange(self.width)
            y = self.random.randrange(self.height)
            newdisneyplus = disneyplus(self.next_id(), (x, y), self)
            self.grid.place_agent(newdisneyplus, (x, y))
            self.schedule.add(newdisneyplus)
        
        # #Creating appletv
        # for i in range(self.initial_appletv):
        #     x = self.random.randrange(self.width)
        #     y = self.random.randrange(self.height)
        #     newappletv = appletv(self.next_id(), (x, y), self)
        #     self.grid.place_agent(newappletv, (x, y))
        #     self.schedule.add(newappletv)

        self.running = True
        self.datacollector.collect(self)

    def step(self):
        self.schedule.step()
        self.datacollector.collect(self)
        if self.verbose:
            print([self.schedule.time,
                   self.schedule.get_type_count(amazonprime),
                   self.schedule.get_type_count(netflix),
                   #self.schedule.get_type_count(appletv),
                   self.schedule.get_type_count(disneyplus)])

    def run_model(self, step_count=200):
        if self.verbose:
            print('Initial number amazonprime: ',
                  self.schedule.get_type_count(amazonprime))
            print('Initial number netflix: ',
                  self.schedule.get_type_count(netflix))
            # print('Initial number appletv: ',
            #       self.schedule.get_type_count(appletv))
            print('Initial number disneyplus: ',
                  self.schedule.get_type_count(disneyplus))

        for i in range(step_count):
            self.step()

        if self.verbose:
            print('')
            print('Final number amazonprime: ',
                  self.schedule.get_type_count(amazonprime))
            print('Final number netflix: ',
                  self.schedule.get_type_count(netflix))
            # print('Final number appletv: ',
            #       self.schedule.get_type_count(appletv))
            print('Final number disneyplus: ',
                  self.schedule.get_type_count(disneyplus))

