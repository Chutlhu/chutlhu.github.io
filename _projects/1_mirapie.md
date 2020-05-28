---
title: mirapie
layout: project
tagline: "Music Interference RemoAl in Python"
description: "Blablabla"
permalink: /projects/mirapie
klass: software
image: images/projects/mirapie/mirapie_thumbnail.jpg
banner: images/projects/mirapie/mirapie_banner.jpg
thumbnail: images/projects/mirapie/mirapie_thumbnail.jpg
links:
  - icon: github
    url: https://github.com/Chutlhu/mirapie
  - icon: book
    url: http://www.aes.org/e-lib/browse.cfm?elib=18751
  - icon: book
    url: https://ieeexplore.ieee.org/abstract/document/8462621
hidden: true
---

In live multitrack recordings, each instrument is usually captured by dedicated close microphones. Unfortunately, it is also captured by other microphones intended for other sources, leading to so-called *interferences*, aka *cross-talk* or *microphone leakage*.<br>
Reducing this interference is desirable because it opens new perspectives for the engineering of live recordings.

##### Interference Reduction in Python

MIRAPIE is a python algorithm developed in MULTISPEECH (a joint project-team between INRIA and LORIA) under the supervision of [Antoine Liuktus](https://members.loria.fr/ALiutkus/) and it the context of the D2YC2 project.<br>
It is based on on the expression of interference reduction as source separation problem within the Gaussian Source Separation framework.

The code is available on [github](https://github.com/Chutlhu/mirapie).

**Partnerships**
- [DYCI2 Project](http://repmus.ircam.fr/dyci2/home)
- [Montreux Jazz Festivals Archive](https://www.montreuxjazzfestival.com/)

![Pipeline]({{site.url}}/images/projects/mirapie/mirapie_pipeline.png)


##### Related publications

- [Interference reduction on full-length live recordings](http://www.aes.org/e-lib/browse.cfm?elib=18751), D. Di Carlo, A. Liutkus, and K. Déguernel, in *IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*, 2018.
- [Gaussian framework for interference reduction in live recordings](https://ieeexplore.ieee.org/abstract/document/8462621), D. Di Carlo, Diego, K. Déguernel and A. Liutkus, in *AES International Conference on Semantic Audio*, 2017
- [Gaussian Framework for Interference Reduction in Live Recordings](https://hal.inria.fr/hal-01870918), D. Di Carlo, Diego (supervised by N. Orio, A. Liutkus), Universitá degli Studi di Padova, 2017

##### The Mixing Matrix


![Mixing]({{site.url}}/images/projects/mirapie/mirapie_thumbnail1.png)
