---
title: musi pi jan lawa moli (rules of chess)
authors:
  - jan Lentan
date: 2020-10-05
tags: null
license: MIT OR CC-BY-SA-3.0 OR CC-BY-SA-4.0
sources:
  - https://lipu-sona.pona.la/lentan/chess
preprocessing:
notes: Removed English translation in HTML comments.
---

## musi pi jan lawa moli

musi pi jan lawa moli li musi supa.

jan tu li utala kepeken musi ni tawa ni: ona li wile anpa e ijo musi "jan lawa" pi jan ante.

## supa musi

supa musi li jo e nasin 8 tan monsi tawa sinpin. sin la, ona li jo e nasin poka
8 tan poka tawa poka ante. nasin en nasin poka li kama wan la, ma
li lon. tan ni, ma 64 li lon.

nasin wan li jo e ma 8. nanpa ona li sama nanpa pi nasin poka ona. tan ni, "ma
\#3 pi nasin \#2" li ma ni: ona li lon nasin \#2, ona li lon nasin poka \#3.

o lukin noka e sitelen pi musi supa:

```
             poka pi jan musi pimeja
         -- +--+--+--+--+--+--+--+--+
    nasin ^ |  |  |  |  |  |  |  |  | nasin nanpa luka tu wan (8)
   sinpin | +--+--+--+--+--+--+--+--+
          | |  |  |  |  |  |  |  |  | nasin nanpa luka tu (7)
    (tawa | +--+--+--+--+--+--+--+--+
      jan | |  |  |  |  |  |  |  |  |
     musi | +--+--+--+--+--+--+--+--+
    walo) | |  |  |  |  |  |  |  |  |
          | +--+--+--+--+--+--+--+--+
          | |  |  |  |  |  |  |  |  | ...
          | +--+--+--+--+--+--+--+--+
          | |  |  |  |  |  |  |  |  | ...
          | +--+--+--+--+--+--+--+--+
          | |  |  |  |  |  |  |  |  | nasin nanpa tu (2)
    nasin | +--+--+--+--+--+--+--+--+
    monsi V |  |  |  |  |  |  |  |  | nasin nanpa wan (1)
         -- +--+--+--+--+--+--+--+--+
             ^     poka pi jan     ^
             |      musi walo      |
             |                     |
 nasin poka nanpa wan     nasin poka nanpa luka tu wan
```

nasin "monsi" li nasin tawa poka pi jan musi sama.
nasin "sinpin" li nasin tawa poka pi jan musi ante.

ma li kule walo, li kule pimeja. nasin kule pi ma li ni:

ma \#1 pi nasin \#1 li pimeja. ma li lon poka pi ma pimeja la, ona li walo.  ma
li lon poka pi ma walo la, ona li pimeja.

nasin ante la, ma li lon sinpin anu monsi pi ma pimeja la, ona li walo. ma
li lon sinpin anu monsi pi ma walo la, ona li pimeja.

```
    +--+--+--+--+--+--+--+--+
    |XX|  |XX|  |XX|  |XX|  |
    +--+--+--+--+--+--+--+--+
    |  |XX|  |XX|  |XX|  |XX|
    +--+--+--+--+--+--+--+--+
    |XX|  |XX|  |XX|  |XX|  |
    +--+--+--+--+--+--+--+--+
    |  |XX|  |XX|  |XX|  |XX|
    +--+--+--+--+--+--+--+--+
    |XX|  |XX|  |XX|  |XX|  |
    +--+--+--+--+--+--+--+--+
    |  |XX|  |XX|  |XX|  |XX|
    +--+--+--+--+--+--+--+--+
    |XX|  |XX|  |XX|  |XX|  |
    +--+--+--+--+--+--+--+--+
    |  |XX|  |XX|  |XX|  |XX|
    +--+--+--+--+--+--+--+--+
```

sitelen ni la, ma mute li jo e sitelen "XX". ma ni li walo.

## ijo musi en tawa ona

jan wan li kama jan musi walo. jan ante li kama jan musi pimeja.

jan musi li jo e ijo musi ona pi kule sama.

ijo musi ni li **jan utala** luka tu wan, li **jan utala lon soweli tawa** tu,
li **soweli suli utala** tu, li **tomo kiwen tawa** tu, li **jan lawa meli**
wan, li **jan lawa** wan.

musi open la, tenpo walo li lon.

tenpo walo la, jan musi walo li ken tawa e ijo musi. 
ona li pini tawa e musi ijo la, tenpo pimeja li lon.

tenpo pimeja la, jan musi pimeja li ken tawa e ijo musi.
ona li pini tawa e musi ijo la, tenpo walo li lon.

jan musi li ken tawa e ijo musi lon tenpo ona taso.

jan musi li ken tawa e ijo musi pi kule sama.

jan musi li ken tawa e ijo musi wan taso.

jan musi li ken tawa e ijo musi la, jan musi ken ala tawa ala e ijo musi.

jan musi li ken tawa e ijo musi kepeken nasin pi ijo musi ni taso.

ijo musi li ken ala tawa ma ni: ijo musi pi kule sama li lon ona.

ijo musi li ken anpa e ijo musi pi kule ante. ni la, ona li weka e ijo musi
ante, li tawa lon ma ona.

ijo musi ante li lon insa pi nasin ona la, ijo musi "jan utala lon soweli tawa"
taso li ken tawa ma ni.

ijo musi weka li ken ala tawa.

## nasin pi ijo musi

**jan utala** li ken tawa ma sinpin wan. 

* sin la, tenpo musi ale la, ona li tawa ala la, ona li ken tawa ma sinpin
  tu.

* ona li ken ala tawa ma sinpin ni: ijo musi ante li lon ma ni anu insa nasin
  tawa ma ni.

* jan utala li ken anpa e ijo musi ni: ona li lon ma sinpin wan en poka wan. ma
  ni li jo e ijo musi pi kule ante la, jan utala li ken pali e ni: weka e ijo
  musi tan ma ni, tawa ma ni.

* jan utala pimeja li lon nasin \#1 la, anu jan utala walo li lon ma
  nasin \#8 la, ona li kama ijo musi ante. jan musi ona ken wile
  ante wan:

  * ona li kama jan utala lon soweli tawa
  * ona li kama soweli suli utala
  * ona li kama tomo kiwen tawa
  * ona li kama jan lawa meli.

```
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |-c-| c |-c-|   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   | C |   |   |
+---+---+---+---+---+---+---+---+
|   |   |-b-| b |-b-|   |   |   |
+---+---+---+---+---+---+---+---+
|   | a |   | B |   |   |   |   |
+---+---+---+---+---+---+---+---+
|-a-| a |-a-|   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   | A |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
```
sitelen ni la, jan utala li lon ma pi sitelen "A", "B" en "C" suli. ona li ken
tawa ma pi sitelen "a", "b" anu "c" lili. ona li ken anpa e ijo musi lon ma
pi sitelen "-a-", "-b-" anu "-c-". jan utala pi sitelen "A" suli li tawa ala lon
musi ni. tan ni, ona li ken tawa ma sinpin tu.

**jan utala lon soweli tawa** (nimi ante: "soweli tawa") li ken tawa ma tu lon
nasin wan en ma wan lon nasin poka pi nasin nanpa wan.

* ijo musi pi kule ante li lon ma ni, ona li ken anpa e ijo musi ni.

```
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   | X |   | X |   |   |
+---+---+---+---+---+---+---+---+
|   |   | X |   |   |   | X |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   | O |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   | X |   |   |   | X |   |
+---+---+---+---+---+---+---+---+
|   |   |   | X |   | X |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
```
sitelen ni la, jan utala lon soweli tawa li lon ma pi sitelen "O". ona li ken
tawa ma pi sitelen "X".

**soweli suli utala** (nimi ante: "lawa sewi" anu "soweli suli") li ken tawa
lon nasin ni: o tawa ma sinpin wan anu ma monsi wan, o tawa ma poka wan. ona li
ken tawa ma mute lon nasin ni.

* ijo musi ante li lon insa pi nasin ona la, ona li ken ala tawa ma ni.

```
+---+---+---+---+---+---+---+---+
| X |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   | X |   |   |   |   |   | X |
+---+---+---+---+---+---+---+---+
|   |   | X |   |   |   | X |   |
+---+---+---+---+---+---+---+---+
|   |   |   | X |   | X |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   | O |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   | X |   | X |   |   |
+---+---+---+---+---+---+---+---+
|   |   | X |   |   |   | X |   |
+---+---+---+---+---+---+---+---+
|   | X |   |   |   |   |   | X |
+---+---+---+---+---+---+---+---+
```
sitelen ni la, soweli suli utala li lon ma pi sitelen "O". ona li ken
tawa ma pi sitelen "X".

**tomo kiwen tawa** (nimi ante: "tomo utala") li ken tawa lon nasin ni: o tawa
ma sinpin wan anu ma monsi wan anu ma poka wan. ona li ken tawa ma mute lon
nasin ni.

* ijo musi ante li lon insa pi nasin ona la, ona li ken ala tawa ma ni.

```
+---+---+---+---+---+---+---+---+
|   |   |   |   | X |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   | X |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   | X |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   | X |   |   |   |
+---+---+---+---+---+---+---+---+
| X | X | X | X | O | X | X | X |
+---+---+---+---+---+---+---+---+
|   |   |   |   | X |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   | X |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   | X |   |   |   |
+---+---+---+---+---+---+---+---+
```

sitelen ni la, tomo kiwen tawa li lon ma pi sitelen "O". ona li ken
tawa ma pi sitelen "X".

**jan lawa meli** (nimi ante: "lawa meli") li ken tawa lon nasin pi soweli suli
utala anu lon nasin pi tomo kiwen tawa.

* ijo musi ante li lon insa pi nasin ona la, ona li ken ala tawa ma ni.

```
+---+---+---+---+---+---+---+---+
| X |   |   |   | X |   |   |   |
+---+---+---+---+---+---+---+---+
|   | X |   |   | X |   |   | X |
+---+---+---+---+---+---+---+---+
|   |   | X |   | X |   | X |   |
+---+---+---+---+---+---+---+---+
|   |   |   | X | X | X |   |   |
+---+---+---+---+---+---+---+---+
| X | X | X | X | O | X | X | X |
+---+---+---+---+---+---+---+---+
|   |   |   | X | X | X |   |   |
+---+---+---+---+---+---+---+---+
|   |   | X |   | X |   | X |   |
+---+---+---+---+---+---+---+---+
|   | X |   |   | X |   |   | X |
+---+---+---+---+---+---+---+---+
```
sitelen ni la, jan lawa meli li lon ma pi sitelen "O". ona li ken
tawa ma pi sitelen "X".

**jan lawa** (nimi ante: "lawa mije") li ken tawa ma wan lon nasin ale.

* ijo musi li anpa e jan lawa, jan musi ona li anpa. o awen e jan lawa sina.

```
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   | X | X | X |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   | X | O | X |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   | X | X | X |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
```
sitelen ni la, jan lawa li lon ma pi sitelen "O". ona li ken
tawa ma pi sitelen "X".

## ma open pi ijo musi 

```
+---+---+---+---+---+---+---+---+
|TKT|LST|SSU|JLM|JL |SSU|LST|TKT|
+---+---+---+---+---+---+---+---+
|JU |JU |JU |JU |JU |JU |JU |JU |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|ju |ju |ju |ju |ju |ju |ju |ju |
+---+---+---+---+---+---+---+---+
|tkt|lst|ssu|jlm|jl |ssu|lst|tkt|
+---+---+---+---+---+---+---+---+
```
open musi la, ijo musi ale li lon ma open ona.

**jan utala walo** ale li lon ma 8 pi nasin \#2. **jan utala pimeja** ale li lon
ma 8 pi nasin \#7.

ijo musi ante ale li lon nasin \#1 tawa jan musi walo, li lon nasin \#8
tawa jan musi pimeja.

**jan utala lon soweli tawa** li lon ma \#2 en ma \#7.

**soweli suli utala** li lon ma \#3 en ma \#6.

**tomo kiwen tawa** li lon ma \#1 en ma \#8.

**jan lawa meli** li lon ma \#4.

**jan lawa** li lon ma \#5.

sitelen ale la, ijo musi walo li sitelen kepeken sitelen lili (abcde...). ijo
musi pimeja li sitelen kepeken sitelen suli (ABCDE...).

> %info%
> 
> 
> ma pi \#1 en \#2 en \#3 en \#4 ale li "poka meli" tan ni: open musi la, jan
> lawa meli ale tu li lon ma \#4.
> 
> ma pi \#5 en \#6 en \#7 en \#8 ale li "poka mije" tan ni: open musi la, jan
> lawa ale tu li lon la \#5.
>

## tawa ante 

jan lawa en tomo kiwen tawa wan pi kule sama li ken tawa lon tenpo sama. taso,
ni ale li wile lon tawa ni:

 * jan lawa en tomo kiwen tawa ni li tawa ala lon tenpo ale pi musi ni.

 * ijo musi ala li lon insa nasin tan jan lawa tawa tomo kiwen tawa ni.

 * ijo musi ante li ken ala anpa e jan lawa.

 * nasin pi jan lawa la, ijo musi ante li ken ala anpa e ma ni.

ni ale li lon la, ken tu li lon:
 
 * jan lawa li tawa ma \#3 pi nasin sama, tomo kiwen tawa pi ma \#1
   li tawa ma \#4.
 
 * jan lawa li tawa ma \#7 pi nasin sama, tomo kiwen tawa pi ma \#8
   li tawa ma \#6.

tenpo mute la, jan utala ("\\#1") li ken tawa ma tu. taso, jan utala pi kule ante
("jan utala \\#2") li ken anpa e ma lon insa nasin pi jan utala \\#1 la, ona li
ken anpa e jan utala \\#1 lon tenpo musi kama wan. jan utala \\#2 li pali e ni la,
ona li tawa ma lon insa nasin pi jan utala \\#1 (ma wan sinpin en ma wan poka).

```
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |JU |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   | X |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |ju | O |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
```

sitelen ni la, jan utala \#1 li lon ma pi sitelen "JU", jan utala \#2 li lon ma pi
sitelen "ju". jan utala \#1 li wile tawa ma pi sitelen "O", taso jan utala \#2 li
ken anpa e ma pi sitelen "X". jan musi \#2 li wile e ni la, ona li ken: anpa e
jan utala \#1, tawa e jan utala \#2 tawa ma pi sitelen "X".

## jan lawa li ken moli 

ijo musi pi jan musi wan li ken anpa e jan lawa pi jan musi ante lon tenpo musi
kama wan, jan lawa ona li "ken moli".

jan lawa li ken moli la, jan musi li wile pali e tawa, tawa ni: ijo musi ante li
ken ala anpa e jan lawa. jan musi li ken ala pali e tawa ante.

jan musi li ken ala pali e ni la, jan lawa ona li moli. jan musi ni li anpa.

jan musi li ken ala tawa e ijo musi ona tawa ni: ijo musi pi jan ante li
ken anpa e jan lawa ona.

```
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |TKT| JL|
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   | JU| JU|
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |TKT|   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|tkt| 2 | 1 |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
| 1 |jl | 1 |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
| 1 |   | 1 |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
tenpo musi pi jan walo (ijo musi pi sitelen lili) li lon.
```

sitelen ni la, tomo kiwen tawa pimeja li ken anpa e jan lawa walo lon tenpo musi
kama wan. jan lawa walo li "ken moli". jan musi walo li wile tawa ni: jan lawa
walo li "ken moli" ala.

ona li ken tawa e jan lawa tawa ma pi sitelen "1". ona li pali e ni la, ijo musi
pimeja li ken ala anpa e jan lawa lon ma ni lon tenpo kama wan.

anu la, ona li ken tawa e tomo kiwen tawa ona tawa ma pi sitelen "2". ona li
pali e ni la, tomo kiwen tawa pimeja li ken ala anpa e jan moli walo tan ni: ijo
musi ante li lon insa nasin ona.

```
+---+---+---+---+---+---+---+---+
| 1 |   |   |   |   |   |   | JL|
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   | JU| JU|
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|tkt|   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |jl |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
tenpo musi pi jan walo (ijo musi pi sitelen lili) li lon.
```

sitelen ni la, jan lawa pimeja li ken ala moli. taso, tomo kiwen tawa walo li
tawa ma pi sitelen "1" la, jan lawa pimeja li ken moli. sin la, ijo musi pimeja
li ken ala tawa ni: jan lawa pimeja li ken moli ala. ni la, jan lawa pimeja li
moli. jan musi walo li anpa e jan musi pimeja.

## kama ante

kama ni li ken: jan musi li ken ala tawa e ilo musi ona, taso jan lawa ona li
ken ala moli. ni li lon la, musi li pini. taso, jan musi ala li anpa e jan musi
ante.

```
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
| 1 | 1 |jlm|   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|JL |1 2|   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
| 1 | 2 |jl |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
tenpo musi pi jan pimeja (ijo musi pi sitelen suli) li lon.
```

sitelen ni la, jan lawa pimeja li ijo musi pimeja taso. ona li ken ala tawa ma
pi sitelen "1" tan ni: jan lawa meli walo li ken anpa e ma ni. ona li ken ala
tawa ma pi sitelen "2" tan ni: jan lawa walo li ken anpa e ma ni. taso, ijo musi
ala li ken anpa e jan lawa pimeja.

tan ni, musi li pini. jan musi walo li anpa ala e jan musi pimeja. jan musi
pimeja li anpa ala e jan musi walo.

---

tenpo musi ale la, jan musi wan li ken toki e ni: "mi anpa." ona li toki e ni
la, musi li pini. jan musi ante li anpa e ona.

tenpo musi ale la, jan musi wan li ken toki e ni: "mi wile e ni: jan ala li
anpa. ni li pona ala pona?" jan musi ante li ken toki tawa ni. ona li toki e
"pona" la, musi li pini. jan musi ala li anpa e jan musi ante.

musi suli la, nasin ni li lon: ijo musi ale li lon ma sama, li ken tawa lon
nasin sama, lon tenpo tawa tu wan pi jan musi sama, jan musi ni li ken toki e
ni: "musi ni li pini. jan ala li anpa."

## suli kiwen pi tenpo tawa 

musi mute la, jan musi, anu jan pi lawa musi, li wile e ni: tenpo musi li suli
ala.  ni li lon la, nasin pi suli kiwen pi tenpo tawa li ken lon.

nasin ni la, jan musi li nanpa e suli tenpo pi tenpo tawa ona kepeken ilo tenpo.
mute tenpo lawa li lon. tenpo pi tenpo tawa ale pi jan wan li suli tawa ona la,
jan musi ni li anpa.

anu la, mute tenpo lawa pi tenpo tawa wan li lon. jan musi ale li wile pali e
tenpo tawa wan ona lon tenpo ni. ona li ken ala pali e ni la, ona li anpa.

# musi pi ilo sona

lipu kon [Lichess](https://lichess.org/) li ilo pona. jan li ken musi kepeken
ona, li ken kama sona e nasin musi kepeken ona. lipu ni li ken toki kepeken toki
pona. taso, ante toki ona li pini ala. ona li toki e ijo kepeken nimi ante.
