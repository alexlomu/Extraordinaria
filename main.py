from Organizacones import *
from Escenarios import *
from Superheroes import *

def main():
    print("=================================================================.")
    print("Test Case 1: Create an Oganization.")
    print("=================================================================.")
    
    

    if organizacion_1.get_nombre() == "Avengers":
        print("Test PASS. The parameter organization_name has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if organizacion_1.get_superheroes() == ["IronMan", "Capitán América", "Thor"]:
        print("Test PASS. The parameter superheroes has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if organizacion_1.get_salud() == [100, 200, 500]:
        print("Test PASS. The parameter health_points has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if organizacion_1.get_ataque() == [8, 7, 9]:
        print("Test PASS. The parameter attack_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if organizacion_1.get_defensa() == [7, 7, 10]:
        print("Test PASS. The parameter defense_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().") 
   



if __name__ == "__main__":
    main()