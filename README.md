# Compute Fricative Features

### Cálculo de características acústicas em fricativas

Minha humilde contribuição para o trabalho de Wellington Araujo Mendes Junior.

Data: 03/08/2022
Autor: Adelino P. Silva
mail: adelinocpp@gmail.com, adelinocpp@gmail.com, adelino@ufmg.br
tel: +55 31 98801-3605

---
Rotina para a leitura de arquivos do tipo .TextgGrid (praat) e calculo de taxas espectrais como:

1. HNR (de Signal_Analysis.features.signal)
2. Centro de gravidade espectral do tipo 1, 2 e 2/3, (vide link abaixo) e
3. Low-frequency-to-total intensities ratio (LTF), vide GRADOVILLE (2021).

Centro de gravidade praat:
https://www.fon.hum.uva.nl/praat/manual/Spectrum__Get_centre_of_gravity___.html

```
GRADOVILLE, M. S., Validity in measurements of fricative voicing: Evidence from 
Argentine Spanish. In: Selected proceedings of the 5th Conference on Laboratory 
Approaches to Romance Phonology. Somerville, MA: Cascadilla Proceedings Project,  p. 59-74.
```


----
##### Contribuições básicas de funções:

**textgrid_to_interval_matrix:** decompõe o arquivo .Textgrid em uma matriz de intervalos **spectral_ratios:** calcula os centros de gravidade e LTF

Livre para uso e modificações. Em caso de dúvidas entre em contato.

##### Como citar

```
@misc{Silva2022,
title={Compute Fricative Features},
author={Adelino Pinheiro Silva},
howPublished={\url{https://github.com/fcampelo/Design-and-Analysis-of-Experiments}},
year={2022},
note={Versão 1.0.1, Creative Commons BY-NC-SA 4.0.},
}
```

