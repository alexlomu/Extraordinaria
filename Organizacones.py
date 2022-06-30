class Organizacion():
    def __init__(self,nombre,superheroes,salud,ataque,defensa):
        if isinstance(nombre, str):
            self.nombre = nombre
        else:
            raise TypeError("The parameter organizacion_name should be a String.")

        if isinstance(superheroes, list):
            for i in superheroes:
                if isinstance(superheroes[i], str):
                    self.superheroes = superheroes
                else:
                    raise TypeError("The parameters in superheroes should be strings.")
                if superheroes == "":
                    print("Debe haber mínimo un superheroe en la organización.")
        else:
            raise TypeError("The parameter organizacion_superheroes should be a list.")
        
        if isinstance(salud, list):
            for i in salud:
                if 1 <= salud[i] <= 100:
                    self.salud = salud
                else:
                    raise ValueError("The parameters in health_points should be > 0 and <= 100.")
        else:
            raise TypeError("The parameter health_points should be a list.")

        if isinstance(ataque, list):
            for i in ataque:
                if 1 <= ataque[i] <= 10:
                    self.ataque = ataque
                else:
                    raise ValueError("The parameters in attack_rating should be > 0 and <= 10.")
        else:
            raise TypeError("The parameter attack_rating should be a list.")

        if isinstance(defensa, list):
            for i in defensa:
                if 1 <= defensa[i] <= 10:
                    self.defensa = defensa
            else:
                raise ValueError("The parameters in defense_rating should be > 0 and <= 10.")
        else:
            raise TypeError("The parameter defense_rating should be a list.")

    def __str__(self):
        
        human_readable_string = ("La organización" + str(self.nombre) +
                                 " con los superheroes " + str(self.superheroes) +
                                 " con la salud " + str(self.salud) +
                                 " con el ataque " + str(self.ataque) +
                                 " con la defensa " + str(self.defensa))

        return human_readable_string

    def get_nombre(self):
        
        return self.nombre


    def get_superheroes(self):
        
        return self.superheroes


    def get_salud(self):
        
        return self.salud


    def get_ataque(self):
        
        return self.ataque


    def get_defensa(self):
        

        return self.defensa

    def set_nombre(self, organization_name_to_be_set):
        
        if isinstance(organization_name_to_be_set, str):
            self.nombre = organization_name_to_be_set
        else:
            raise TypeError("The parameter organization_name_to_be_set should be a String.")


    def set_arma(self, superheroe_type_to_be_set):
        
        if isinstance(superheroe_type_to_be_set, list):
            self.arma = superheroe_type_to_be_set
        else:
            raise TypeError("The parameter superheroe_type_to_be_set should be a list.")


    def set_ataque(self, ataque_to_be_set):
      
        if isinstance(ataque_to_be_set, list):
            for i in ataque_to_be_set:
                if 1 <= ataque_to_be_set[i] <= 10:
                    self.ataque = ataque_to_be_set
                else:
                    raise ValueError("The parameters in attack_rating_to_be_set should be > 0 and <= 10.")
        else:
            raise TypeError("The parameter attack_rating_to_be_set should be a list.")


    def set_defensa(self, defensa_to_be_set):
        
        if isinstance(defensa_to_be_set, list):
            for i in defensa_to_be_set:
                if 1 <= defensa_to_be_set[i] <= 10:
                    self._defensa = defensa_to_be_set
                else:
                    raise ValueError("The parameters in defense_rating_to_be_set should be > 0 and <= 10.")
        else:
            raise TypeError("The parameter defense_rating_to_be_set should be a list.")

    def is_undefeated(self):
        for i in self.salud:
            if self.salud== 0:
                var = True
            else:
                var = False
        return not bool(var)

    def surrender(self):
        for i in self.salud:
            self.salud[i] == 0
