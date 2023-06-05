# gefxml_reader

Application to read geotechnical CPT and bore data in GEF or BRO XML format

## Dependecies
See environment.yml

## Instruction
Importeer de package:  
`from geotexxx.gefxml_reader import Cpt, Bore`  
Maak een leeg object:  
`test = Cpt()` or `test = Bore()`    
Lees een bestand:  
`test.load_gef(filename)` or `test.load_xml(filename)`  
Maak een plot in map ./output:  
`test.plot()`  

[gefxml_viewer](https://github.com/Amsterdam/gefxml_viewer.git) biedt een grafische interface om sonderingen en boringen incl. eenvoudige labproeven te plotten.

# Complexe proeven
Beschikbaar:
* korrelgrootteverdeling: figs = test.plot_korrelgrootte_verdelingen()
* samendrukkingsproeven: figs = plot_samendrukkingsproeven()

## Vragen of opmerkingen?
1. Stuur een bericht aan Thomas van der Linden, bijvoorbeeld via [LinkedIn](https://www.linkedin.com/in/tjmvanderlinden/)

## Resultaten?
1. Heb je mooie resultaten gemaakt met deze applicatie? We vinden het heel leuk als je ze deelt (en Thomas tagt)