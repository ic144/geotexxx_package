# gefxml_reader
Package om geotechnische sonderingen of boringen in GEF, BRO XML of SIKB0101 XML te lezen en visualiseren


## Dependecies
Zie environment.yml

## Instruction
Installeer de package:  
`pip install geotexxx` of `conda install -c conda-forge geotexxx`  
Importeer de package:  
`from geotexxx.gefxml_reader import Cpt, Bore`  
Maak een leeg object:  
`test = Cpt()` of `test = Bore()`    
Lees een bestand:  
`test.load_gef(filename)` of `test.load_xml(filename)`  
Maak een plot in map ./output:  
`test.plot()`  

[gefxml_viewer](https://github.com/Amsterdam/gefxml_viewer.git) biedt een grafische interface om sonderingen en boringen incl. eenvoudige labproeven te plotten.

# Complexe proeven
Beschikbaar:
* korrelgrootteverdeling: `figs = test.plot_korrelgrootte_verdelingen()`
* samendrukkingsproeven: `figs = test.plot_samendrukkingsproeven()`

## Vragen of opmerkingen?
Stuur een bericht aan Thomas van der Linden, bijvoorbeeld via [LinkedIn](https://www.linkedin.com/in/tjmvanderlinden/)

## Resultaten?
Heb je mooie resultaten gemaakt met deze applicatie? We vinden het heel leuk als je ze deelt (en Thomas tagt)