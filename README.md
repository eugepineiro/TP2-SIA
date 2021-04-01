# TP2-SIA 2021 1er C.
Proyecto hecho en Python para encontrar las mejores configuraciones (altura y equipamiento) de un personaje utilizando algoritmos genéticos.

```
Integrantes:
- Eugenia Sol Piñeiro
- Scott Lin
- Nicolás Comerci Wolcanyik
```
### Requerimientos previos
- Python 3

### Instalación
1. Como primera instancia clonar el proyecto en algun directorio de preferencia:
```bash
$> git clone https://github.com/eugepineiro/TP2-SIA
```
2. Dentro de la carpeta del proyecto, instalar los módulos requeridos que se encuentran en requirements.txt:
```bash
$> pip3 install -r requirements.txt
```
### Configuración y ejecución
Dentro del archivo `config.json`, que está en el directorio raíz del proyecto, se encuentran todos los parámetros posibles de configuración:
- "class": clase de personaje para el cual se busca optimar su configuración (warrior, archer, defender, spy)
- "methods": abarca los métodos de selección, cruza y mutación con los respectivos parámetros que utiliza cada uno:
    - "crossover": tipo de cruza que se quiere hacer (one_point, two_points, annular, uniform)
    - "mutation": tipo de mutación que se quiere hacer (complete, limited_multigen, uniform_multigen, one_gen)
    - "mutation_params": contiene los parámetros que se van a utilizar para los métodos de mutación:
        - "limited_multigen_limit": parámetros que indica el límite de genes que se va a mutar en la mutación de tipo limited_multigen
    - "selection_a": tipo de selección que se quiere hacer para una porción de la población (elite, roulette, universal, ranking, boltzmann, d_tournaments, p_tournaments)
    - "selection_b": tipo de selección que se quiere hacer para la otra porción de la población (elite, roulette, universal, ranking, boltzmann, d_tournaments, p_tournaments)
    - "selection_prob": indica que porcentaje de la población se selecciona con selection_a y que porcentaje se selecciona con selection_b con la ecuación: ```selection_prob * selection_a + (1-selection_prob) * selection_b``` (número entre [0,1])
    - "replacement_a": tipo de selección que se quiere hacer para reemplazar una porción de la población (elite, roulette, universal, ranking, boltzmann, d_tournaments, p_tournaments)
    - "replacement_b": tipo de selección que se quiere hacer para reemplazar la otra porción de la población (elite, roulette, universal, ranking, boltzmann, d_tournaments, p_tournaments)
    - "replacement_prob": indica que porcentaje de la población se reemplaza con replacement_a y que porcentaje se reemplaza con replacement_b con la ecuación: ```replacement_prob * replacement_a + (1-replacement_prob) * replacement_b``` (numero entre [0,1])
    - "selection_params": contiene los parámetros que se van a utilizar para los métodos de selección:
        - "p_tournaments_threshold": establece el threshold para el método de selección p_tournaments (número entre [0,1])
        - "d_tournaments_m": establece la cantidad de personajes de los cuales se selecciona en cada iteracion del método de selección d_tournaments
        - "boltzmann_temp": contiene los parámetros que se van a utilizar para el método de selección boltzmann:
            - "t0": establece la temperatura inicial 
            - "tc": establece la temperatura base
            - "k": establece la constante de la temperatura
- "cutting_condition": abarca los métodos de corte y los parámetros qeu recibe cada uno:
    - "method": método de corte (time, generation, content, structure, solution)
    - "parameter": condición de corte
- "individual_mutation_probability": probabilidad de mutación de un individuo (número entre [0,1])
- "implementation": implementación que se utiliza para reemplazar los individuos de una generación (fill_all, fill_parent)
- "population_amount": tamaño de la población
- "individuals_amount": cantidad de individuos que se selecciona en cada iteración
- "path_to_files": #TODO

Una vez configurados todos los parámentros, ejecutar el siguiente comando para correr el proyecto:
```bash
$> python3 main.py
```
Una vez arrancado el programa, se abrirá una ventana mostrando gráficos en tiempo real con información sobre el desempeño de los individuos en cada generación, junto con la diversidad genética de cada generación
![window](https://lh3.googleusercontent.com/NoA3Gk3pOge3QPoAJsVDJS7u-cTq2KM5XOzM19gruSc7z8x-AeAaicix109kxunX-KBsdlLUzwNb_cVOyk8vovjtJGZN7275vJKIMYHF-83SClkqRRgjnd_7wYOBtmexRgtj5Tnh=w2400)

### Posibles configuraciones de ejecución: `config.json`
```json
{
    "class": "warrior",
    "implementation": "fill_all",
    "population_amount": 1000,
    "individuals_amount": 500,
    "individual_mutation_probability": 0.2,
    "methods": {
        "crossover": "two_points",
        "mutation": "one_gen", 
        "mutation_params": {
            "limited_multigen_limit": 3
        },
        "selection_a": "elite",
        "selection_b": "roulette",
        "selection_prob": 0.2, 
        "replacement_a": "elite",
        "replacement_b": "d_tournaments",
        "replacement_prob": 0.4,
        "selection_params": {
            "p_tournaments_threshold": 0.7, 
            "d_tournaments_m": 50,
            "boltzmann_temp": {
                "t0": 50,
                "tc": 10, 
                "k": 0.3
            } 
        }
    },
    "cutting_condition": {
        "method": "generation",
        "parameter": 100
    }, 
    "dataset_path": {
        "weapons": "TP2/allitems/armas.tsv",
        "helmets": "TP2/allitems/cascos.tsv",
        "gloves": "TP2/allitems/guantes.tsv",
        "boots": "TP2/allitems/botas.tsv",
        "armors": "TP2/allitems/pecheras.tsv"
    } 
}
```
