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

| Parámetro| Descripción                    | Opciones|
| ------------- | ------------------------------ | ------------- |
|"class"     |  Clase de personaje para el cual se busca optimar su aptitud  | warrior, archer, defender, spy |
| "implementation" |   implementación que se utiliza para reemplazar los individuos de la generación actual | fill_all, fill_parent |
| "population_amount" |  tamaño de la población | número entero |
| "individuals_amount" |  cantidad de individuos que se selecciona en cada iteración | número entero |
| "individual_mutation_probability" |  probabilidad de mutación de un individuo | número entre [0,1] |
|"methods"  |abarca los métodos de selección, cruza y mutación con los respectivos parámetros que utiliza cada uno | |
|   | "crossover":  tipo de cruza que se quiere hacer | one_point, two_points, annular, uniform |
|   | "mutation":  tipo de mutación que se quiere hacer |complete, limited_multigen, uniform_multigen, one_gen |
|   | "mutation_params":  "limited_multigen_limit": cantidad de genes que se eligen en limited_multigen | número entero entre [2, 5 ] |
|   | "selection_a":  tipo de selección que se quiere hacer para una porción de la población | elite, roulette, universal, ranking, boltzmann, d_tournaments, p_tournaments |
|   | "selection_b":  tipo de selección que se quiere hacer para el resto de la población | elite, roulette, universal, ranking, boltzmann, d_tournaments, p_tournaments |
|   |"selection_prob": indica qué porcentaje de la población se selecciona con selection_a y qué porcentaje se selecciona con selection_b con la ecuación: `selection_prob * selection_a + (1-selection_prob) * selection_b`| número entre [0,1]|
|   | "replacement_a":  tipo de selección que se quiere hacer para reemplazar una porción de la población | elite, roulette, universal, ranking, boltzmann, d_tournaments, p_tournaments |
|   | "replacement_b":  tipo de selección que se quiere hacer para el resto de la población | elite, roulette, universal, ranking, boltzmann, d_tournaments, p_tournaments |
|   |"replacement_prob": indica qué porcentaje de la población se reemplaza con replacement_a y qué porcentaje se reemplaza con replacement_b con la ecuación: `replacement_prob * replacement_a + (1-replacement_prob) * replacement_b`| número entre [0,1]|
|  "selection_params" | parámetros que se van a utilizar para los métodos de selección |  | 
|   | "p_tournaments_threshold": threshold para el método de selección p_tournaments | número entre [0.5, 1] |
|   | "d_tournaments_m": establece la cantidad de personajes de los cuales se selecciona en cada iteracion del método de selección d_tournaments | número < tamaño de la población |
|   | "boltzmann_temp": contiene los parámetros que se van a utilizar para la función de temperatura del método de selección boltzmann: `tc + (t0 - tc) exp(-k*t)` | "t0": temperatura inicial, "tc": temperatura cota, "k": constante de la temperatura |
| "cutting_condition" | abarca los métodos de corte y los parámetros que recibe cada uno | |
|  | "method": "time" | "parameter": tiempo en segundos|
|  | "method": "generation" | "parameter": cantidad de generaciones | 
|  | "method": "content" | "parameter": cantidad de generaciones en las que el mejor fitness no cambia |
|  | "method": "structure" | "parameter": porcentaje de la población que no cambia en una cantidad de generaciones, la cual se puede establecer con la opción ""structure_max_generations" |
|  | "method": "solution" | "parameter": valor de fitness medio que se considera como solución aceptable |
| "dataset_path" |  path de cada archivo donde se encuentran los items de los personajes | |
|   | "weapons" | path al archivo de armas |
|   |  "helmets" | path al archivo de  cascos|
|   | "gloves" | path al archivo de guantes |
|   | "boots" | path al archivo de botas |
|   | "armors" | path al archivo de pecheras |

Una vez configurados todos los parámentros, ejecutar el siguiente comando para correr el proyecto:
```bash
$> python3 main.py
```
Una vez arrancado el programa, se abrirá una ventana mostrando gráficos en tiempo real con información sobre el desempeño de los individuos en cada generación, junto con la diversidad genética de cada generación. (Se considera diversidad la cantidad de individuos que difieren en altura y equipamiento considerando un delta de precisión de 0.01)
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
        "crossover": "uniform",
        "mutation": "uniform_multigen", 
        "mutation_params": {
            "limited_multigen_limit": 5
        },
        "selection_a": "boltzmann",
        "selection_b": "d_tournaments",
        "selection_prob": 0.7, 
        "replacement_a": "elite",
        "replacement_b": "universal",
        "replacement_prob": 0.6,
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
        "parameter": 100, 
        "structure_max_generations": 5 
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
```json
{
    "class": "spy",
    "implementation": "fill_parent",
    "population_amount": 600,
    "individuals_amount": 400,
    "individual_mutation_probability": 0.5,
    "methods": {
        "crossover": "uniform",
        "mutation": "one_gen", 
        "mutation_params": {
            "limited_multigen_limit": 5
        },
        "selection_a": "elite",
        "selection_b": "p_tournaments",
        "selection_prob": 0.2, 
        "replacement_a": "ranking",
        "replacement_b": "universal",
        "replacement_prob": 0.6,
        "selection_params": {
            "p_tournaments_threshold": 0.6, 
            "d_tournaments_m": 50,
            "boltzmann_temp": {
                "t0": 50,
                "tc": 10, 
                "k": 0.3
            } 
        }
    },
    "cutting_condition": {
        "method": "solution",
        "parameter": 24, 
        "structure_max_generations": 100 
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
