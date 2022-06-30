import tipos

class Superheroes():
    lista_ids= []
    def __init__(self,id,alias,secret_identity,movements,type,cost,energy,health):
        if isinstance(id, int):
            if id not in Superheroes.lista_ids:
                self.id = id
                Superheroes.lista_ids.append(self.id)
            else:
                raise ValueError("The parameter Superheroes_id should be a new id not taken by other Superhero.")
        else:
            raise TypeError("The parameter id should be a int.")

        if isinstance(alias, str):
            self.nombre = alias
        else:
            raise TypeError("The parameter alias_name should be a String.")

        if isinstance(secret_identity, str):
            self.secret_identity = secret_identity
        else:
            raise TypeError("The parameter secret_identity should be a string.")

        if isinstance(movements, list):
            self.movements = movements
        else:
            raise TypeError("The parameter movements should be a list.")

        if isinstance(type, tipos.types):
            self.type = type
        else:
            raise TypeError("The parameter type should be in types.")

        if isinstance(cost, int):
            self.cost = cost
        else:
            raise ValueError("The parameter cost should be a int.")

        if isinstance(energy, int):
            self.energy = energy
        else:
            raise ValueError("The parameter energy should be a int.")

        if isinstance(health, int):
            if 1 <= health <= 1000:
                self.health = health
            else:
                raise ValueError("The parameter health_points should be > 0 and <= 1000.")
        else:
            raise TypeError("The parameter health_points should be a int.")

    def __del__(self):
         Superheroes.lista_ids.remove(self.id)

    def get_id(self):
        
        return self.id


    def get_alias(self):
        
        return self.get_alias


    def get_secret_identity(self):
        
        return self.secret_identity


    def get_movements(self):
        
        return self.movements


    def get_type(self):
        
        return self.type


    def get_cost(self):
    
        return self.cost

    def get_energy(self):

        return self.energy

    def get_health(self):

        return self.health


    def set_alias(self, superhero_alias_to_be_set):
        
        if isinstance(superhero_alias_to_be_set, str):
            self.alias = superhero_alias_to_be_set
        else:
            raise TypeError("The parameter superhero_alias_to_be_set should be a String.")

    def set_secret_identity(self, superhero_secret_identity_to_be_set):
        
        if isinstance(superhero_secret_identity_to_be_set, str):
            self.secret_identity = superhero_secret_identity_to_be_set
        else:
            raise TypeError("The parameter superhero_secret_identity_to_be_set should be a String.")
    
    def set_movements(self, superhero_movements_to_be_set):
        
        if isinstance(superhero_movements_to_be_set, list):
            self.movements = superhero_movements_to_be_set
        else:
            raise TypeError("The parameter superhero_movements_to_be_set should be a String.")


    def set_type(self, type_to_be_set):
        
        if isinstance(type_to_be_set, types):
            self.type = type_to_be_set
        else:
            raise TypeError("The parameter type should be in types.")


    def set_cost(self, cost_to_be_set):
      
        if isinstance(cost_to_be_set, int):
           self.cost = cost_to_be_set
        else:
            raise TypeError("The parameter cost_to_be_set should be a int.")

    def set_energy(self, energy_to_be_set):
      
        if isinstance(energy_to_be_set, int):
           self.energy = energy_to_be_set
        else:
            raise TypeError("The parameter energy_to_be_set should be a int.")

    def set_health(self, health_to_be_set):

        if isinstance(health_to_be_set, int):
            if 1 <= health_to_be_set <= 1000:
                self.health = health_to_be_set
            else:
                raise ValueError("The parameter health_to_be_set should be > 0 and <= 1000.")
        else:
            raise TypeError("The parameter health_to_be_set should be a int.")

    def is_alive(self):
        
        return not bool(self.health == 0)

    def die(self):
        self.health = 0
        return self.health