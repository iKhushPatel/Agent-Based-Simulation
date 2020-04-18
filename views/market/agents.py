from mesa import Agent
import random
#Base class to handle movements of Agents
class Walker(Agent):
    
    grid = None
    x = None
    y = None
    agentType=None
    
    def __init__(self, unique_id, pos, model, agentType):
        super().__init__(unique_id, model)
        self.pos = pos
        self.agentType=agentType
        
    def walk(self):
        #In case of Self Isolation
        next_moves = self.model.grid.get_neighborhood(self.pos, True, True)
        next_move = self.random.choice(next_moves)
        #Move the Agent
        self.model.grid.move_agent(self, next_move)
            

class amazonprime(Walker):
    def __init__(self, unique_id, pos, model):
        super().__init__(unique_id, pos, model,"amazonprime")
    
    def step(self):
        self.walk()
        x, y = self.pos
        #Fetching the susceptibles in the neighbourhood
        this_cell = self.model.grid.get_cell_list_contents([self.pos])
        users_amazonprime = [obj for obj in this_cell if isinstance(obj, amazonprime)]
        users_disneyplus = [obj for obj in this_cell if isinstance(obj, disneyplus)]
        users_netflix = [obj for obj in this_cell if isinstance(obj, netflix)]
        
        # weight_amazonprime = self.quality_amazonprime * self.content_amazonprime
        # weight_netflix = self.quality_netflix * self.content_netflix
        # weight_disneyplus = self.quality_disneyplus * self.content_disneyplus

        # print(weight_amazonprime, weight_netflix, weight_disneyplus)
        if(len(users_amazonprime) > len(users_netflix) and len(users_amazonprime) > len(users_disneyplus)):
            #amazonprime highest
            if(random.randrange(2) == 1):
                if(len(users_netflix) <= 0):
                    pass
                else:
                    tonetflix = self.random.choice(users_netflix)
                    #Recovering the Infected
                    newamazonprime= amazonprime(self.model.next_id(), self.pos, self.model)
                    self.model.grid.place_agent(newamazonprime, newamazonprime.pos)
                    self.model.schedule.add(newamazonprime)
                    #Removing the Infected
                    self.model.grid._remove_agent(self.pos, tonetflix)
                    self.model.schedule.remove(tonetflix)
            else:
                if(len(users_disneyplus) <= 0):
                    pass
                else:
                    todisneyplus = self.random.choice(users_disneyplus)
                    #Recovering the Infected
                    newamazonprime= amazonprime(self.model.next_id(), self.pos, self.model)
                    self.model.grid.place_agent(newamazonprime, newamazonprime.pos)
                    self.model.schedule.add(newamazonprime)
                    #Removing the Infected
                    self.model.grid._remove_agent(self.pos, todisneyplus)
                    self.model.schedule.remove(todisneyplus)
        elif(len(users_netflix) > len(users_amazonprime) and len(users_netflix) > len(users_disneyplus)):
            #amazonprime highest
            if(random.randrange(2) == 1):
                if(len(users_amazonprime) <= 0):
                    pass
                else:
                    toamazonprime = self.random.choice(users_amazonprime)
                    #Recovering the Infected
                    newnetflix= netflix(self.model.next_id(), self.pos, self.model)
                    self.model.grid.place_agent(newnetflix, newnetflix.pos)
                    self.model.schedule.add(newnetflix)
                    #Removing the Infected
                    self.model.grid._remove_agent(self.pos, toamazonprime)
                    self.model.schedule.remove(toamazonprime)
            else:
                if(len(users_disneyplus) <= 0):
                    pass
                else:
                    todisneyplus = self.random.choice(users_disneyplus)
                    #Recovering the Infected
                    newnetflix= netflix(self.model.next_id(), self.pos, self.model)
                    self.model.grid.place_agent(newnetflix, newnetflix.pos)
                    self.model.schedule.add(newnetflix)
                    #Removing the Infected
                    self.model.grid._remove_agent(self.pos, todisneyplus)
                    self.model.schedule.remove(todisneyplus)
        elif(len(users_disneyplus) > len(users_amazonprime) and len(users_disneyplus) > len(users_netflix)):
            #disneyplus highest
            if(random.randrange(2) == 1):
                if(len(users_amazonprime) <= 0):
                    pass
                else:
                    toamazonprime = self.random.choice(users_amazonprime)
                    #Recovering the Infected
                    newdisneyplus= disneyplus(self.model.next_id(), self.pos, self.model)
                    self.model.grid.place_agent(newdisneyplus, newdisneyplus.pos)
                    self.model.schedule.add(newdisneyplus)
                    #Removing the Infected
                    self.model.grid._remove_agent(self.pos, toamazonprime)
                    self.model.schedule.remove(toamazonprime)
            else:
                if(len(users_netflix) <= 0):
                    pass
                else:
                    tonetflix = self.random.choice(users_netflix)
                    #Recovering the Infected
                    newdisneyplus= disneyplus(self.model.next_id(), self.pos, self.model)
                    self.model.grid.place_agent(newdisneyplus, newdisneyplus.pos)
                    self.model.schedule.add(newdisneyplus)
                    #Removing the Infected
                    self.model.grid._remove_agent(self.pos, tonetflix)
                    self.model.schedule.remove(tonetflix)


        

class disneyplus(Walker):
    def __init__(self, unique_id, pos, model):
        super().__init__(unique_id, pos, model,"disneyplus")

    def step(self):
        self.walk()
        x, y = self.pos
        #Fetching the susceptibles in the neighbourhood
        this_cell = self.model.grid.get_cell_list_contents([self.pos])
        users_amazonprime = [obj for obj in this_cell if isinstance(obj, amazonprime)]
        users_disneyplus = [obj for obj in this_cell if isinstance(obj, disneyplus)]
        users_netflix = [obj for obj in this_cell if isinstance(obj, netflix)]
        
        # weight_amazonprime = self.quality_amazonprime * self.content_amazonprime
        # weight_netflix = self.quality_netflix * self.content_netflix
        # weight_disneyplus = self.quality_disneyplus * self.content_disneyplus

        # print(weight_amazonprime, weight_netflix, weight_disneyplus)
        if(len(users_amazonprime) > len(users_netflix) and len(users_amazonprime) > len(users_disneyplus)):
            #amazonprime highest
            if(random.randrange(2) == 1):
                if(len(users_netflix) <= 0):
                    pass
                else:
                    tonetflix = self.random.choice(users_netflix)
                    #Recovering the Infected
                    newamazonprime= amazonprime(self.model.next_id(), self.pos, self.model)
                    self.model.grid.place_agent(newamazonprime, newamazonprime.pos)
                    self.model.schedule.add(newamazonprime)
                    #Removing the Infected
                    self.model.grid._remove_agent(self.pos, tonetflix)
                    self.model.schedule.remove(tonetflix)
            else:
                if(len(users_disneyplus) <= 0):
                    pass
                else:
                    todisneyplus = self.random.choice(users_disneyplus)
                    #Recovering the Infected
                    newamazonprime= amazonprime(self.model.next_id(), self.pos, self.model)
                    self.model.grid.place_agent(newamazonprime, newamazonprime.pos)
                    self.model.schedule.add(newamazonprime)
                    #Removing the Infected
                    self.model.grid._remove_agent(self.pos, todisneyplus)
                    self.model.schedule.remove(todisneyplus)
        elif(len(users_netflix) > len(users_amazonprime) and len(users_netflix) > len(users_disneyplus)):
            #amazonprime highest
            if(random.randrange(2) == 1):
                if(len(users_amazonprime) <= 0):
                    pass
                else:
                    toamazonprime = self.random.choice(users_amazonprime)
                    #Recovering the Infected
                    newnetflix= netflix(self.model.next_id(), self.pos, self.model)
                    self.model.grid.place_agent(newnetflix, newnetflix.pos)
                    self.model.schedule.add(newnetflix)
                    #Removing the Infected
                    self.model.grid._remove_agent(self.pos, toamazonprime)
                    self.model.schedule.remove(toamazonprime)
            else:
                if(len(users_disneyplus) <= 0):
                    pass
                else:
                    todisneyplus = self.random.choice(users_disneyplus)
                    #Recovering the Infected
                    newnetflix= netflix(self.model.next_id(), self.pos, self.model)
                    self.model.grid.place_agent(newnetflix, newnetflix.pos)
                    self.model.schedule.add(newnetflix)
                    #Removing the Infected
                    self.model.grid._remove_agent(self.pos, todisneyplus)
                    self.model.schedule.remove(todisneyplus)
        elif(len(users_disneyplus) > len(users_amazonprime) and len(users_disneyplus) > len(users_netflix)):
            #disneyplus highest
            if(random.randrange(2) == 1):
                if(len(users_amazonprime) <= 0):
                    pass
                else:
                    toamazonprime = self.random.choice(users_amazonprime)
                    #Recovering the Infected
                    newdisneyplus= disneyplus(self.model.next_id(), self.pos, self.model)
                    self.model.grid.place_agent(newdisneyplus, newdisneyplus.pos)
                    self.model.schedule.add(newdisneyplus)
                    #Removing the Infected
                    self.model.grid._remove_agent(self.pos, toamazonprime)
                    self.model.schedule.remove(toamazonprime)
            else:
                if(len(users_netflix) <= 0):
                    pass
                else:
                    tonetflix = self.random.choice(users_netflix)
                    #Recovering the Infected
                    newdisneyplus= disneyplus(self.model.next_id(), self.pos, self.model)
                    self.model.grid.place_agent(newdisneyplus, newdisneyplus.pos)
                    self.model.schedule.add(newdisneyplus)
                    #Removing the Infected
                    self.model.grid._remove_agent(self.pos, tonetflix)
                    self.model.schedule.remove(tonetflix)

class netflix(Walker):

    def __init__(self, unique_id, pos, model):
        super().__init__(unique_id, pos, model,"netflix")
        
    def step(self):
        self.walk()
        x, y = self.pos
        #Fetching the susceptibles in the neighbourhood
        this_cell = self.model.grid.get_cell_list_contents([self.pos])
        users_amazonprime = [obj for obj in this_cell if isinstance(obj, amazonprime)]
        users_disneyplus = [obj for obj in this_cell if isinstance(obj, disneyplus)]
        users_netflix = [obj for obj in this_cell if isinstance(obj, netflix)]
        
        # weight_amazonprime = self.quality_amazonprime * self.content_amazonprime
        # weight_netflix = self.quality_netflix * self.content_netflix
        # weight_disneyplus = self.quality_disneyplus * self.content_disneyplus

        # print(weight_amazonprime, weight_netflix, weight_disneyplus)
        if(len(users_amazonprime) > len(users_netflix) and len(users_amazonprime) > len(users_disneyplus)):
            #amazonprime highest
            if(random.randrange(2) == 1):
                if(len(users_netflix) <= 0):
                    pass
                else:
                    tonetflix = self.random.choice(users_netflix)
                    #Recovering the Infected
                    newamazonprime= amazonprime(self.model.next_id(), self.pos, self.model)
                    self.model.grid.place_agent(newamazonprime, newamazonprime.pos)
                    self.model.schedule.add(newamazonprime)
                    #Removing the Infected
                    self.model.grid._remove_agent(self.pos, tonetflix)
                    self.model.schedule.remove(tonetflix)
            else:
                if(len(users_disneyplus) <= 0):
                    pass
                else:
                    todisneyplus = self.random.choice(users_disneyplus)
                    #Recovering the Infected
                    newamazonprime= amazonprime(self.model.next_id(), self.pos, self.model)
                    self.model.grid.place_agent(newamazonprime, newamazonprime.pos)
                    self.model.schedule.add(newamazonprime)
                    #Removing the Infected
                    self.model.grid._remove_agent(self.pos, todisneyplus)
                    self.model.schedule.remove(todisneyplus)
        elif(len(users_netflix) > len(users_amazonprime) and len(users_netflix) > len(users_disneyplus)):
            #amazonprime highest
            if(random.randrange(2) == 1):
                if(len(users_amazonprime) <= 0):
                    pass
                else:
                    toamazonprime = self.random.choice(users_amazonprime)
                    #Recovering the Infected
                    newnetflix= netflix(self.model.next_id(), self.pos, self.model)
                    self.model.grid.place_agent(newnetflix, newnetflix.pos)
                    self.model.schedule.add(newnetflix)
                    #Removing the Infected
                    self.model.grid._remove_agent(self.pos, toamazonprime)
                    self.model.schedule.remove(toamazonprime)
            else:
                if(len(users_disneyplus) <= 0):
                    pass
                else:
                    todisneyplus = self.random.choice(users_disneyplus)
                    #Recovering the Infected
                    newnetflix= netflix(self.model.next_id(), self.pos, self.model)
                    self.model.grid.place_agent(newnetflix, newnetflix.pos)
                    self.model.schedule.add(newnetflix)
                    #Removing the Infected
                    self.model.grid._remove_agent(self.pos, todisneyplus)
                    self.model.schedule.remove(todisneyplus)
        elif(len(users_disneyplus) > len(users_amazonprime) and len(users_disneyplus) > len(users_netflix)):
            #disneyplus highest
            if(random.randrange(2) == 1):
                if(len(users_amazonprime) <= 0):
                    pass
                else:
                    toamazonprime = self.random.choice(users_amazonprime)
                    #Recovering the Infected
                    newdisneyplus= disneyplus(self.model.next_id(), self.pos, self.model)
                    self.model.grid.place_agent(newdisneyplus, newdisneyplus.pos)
                    self.model.schedule.add(newdisneyplus)
                    #Removing the Infected
                    self.model.grid._remove_agent(self.pos, toamazonprime)
                    self.model.schedule.remove(toamazonprime)
            else:
                if(len(users_netflix) <= 0):
                    pass
                else:
                    tonetflix = self.random.choice(users_netflix)
                    #Recovering the Infected
                    newdisneyplus= disneyplus(self.model.next_id(), self.pos, self.model)
                    self.model.grid.place_agent(newdisneyplus, newdisneyplus.pos)
                    self.model.schedule.add(newdisneyplus)
                    #Removing the Infected
                    self.model.grid._remove_agent(self.pos, tonetflix)
                    self.model.schedule.remove(tonetflix)
    
# class appletv(Agent):
#     def __init__(self, unique_id, pos, model):
#         super().__init__(unique_id, pos, model, "appletv")
        
#     def step(self):
#         self.walk()
