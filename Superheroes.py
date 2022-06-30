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
