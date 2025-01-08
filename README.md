# gefxml_reader
Package om geotechnische sonderingen of boringen in GEF, BRO-XML, Dino XML, SON of SIKB0101-XML te lezen en visualiseren


## Dependecies
* matplotlib
* numpy
* pandas
* pyproj

## Instruction
Installeer de package:  
`pip install geotexxx` of `conda install conda-forge::geotexxx`  
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
* korrelgrootteverdelingen: `figs = test.plot_korrelgrootte_verdelingen()`
* samendrukkingsproeven: `figs = test.plot_samendrukkingsproeven()`
* schuifsterkteproef: `figs = test.plot_schuifsterkteproef()`

# Interpret a CPT
Maak een lege CPT en een lege boring:  
`cpt = Cpt()` en `bore = Bore()`    
Lees een bestand:  
`cpt.load_gef(filename)` of `cpt.load_xml(filename)`
Doe de interpretatie:  
`cpt.interpret()`
Maak een boorstaat:  
`bore.from_cpt(cpt)`
Maak de figuur:  
`fig = bore.plot(save_fig=False)`

## Vragen of opmerkingen?
Stuur een bericht aan Thomas van der Linden, bijvoorbeeld via [LinkedIn](https://www.linkedin.com/in/tjmvanderlinden/)

## Resultaten?
Heb je mooie resultaten gemaakt met deze applicatie? We vinden het heel leuk als je ze deelt (en Thomas tagt)