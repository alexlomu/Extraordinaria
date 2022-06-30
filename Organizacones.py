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



