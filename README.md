<img src="images/logo.svg" alt="Logo of poki Lapo" width="225" style="display: block; margin: 0 auto"/>

# poki-lapo


Poki Lapo is a library and monolingual corpus for Toki Pona. Our vision is to expand to include all types of media in Toki Pona, including books, poetry, music, comics, posts and more. Files are transcribed by volunteers into Markdown format with metadata as shown below.

## Schemas

### File metadata

See also the [schema validation code](utils/validate/validate-schemas.ts).

```yaml
---
# If one of these fields is missing from your text, set its value to `null`
title:
description:
authors:
  - 
proofreaders:
  - 
date: # yyyy-mm-dd
date-precision: # day, month, year, none
original:
  title:
  authors:
    -
tags:
  -
license:
sources:
  - 
archives:
  - 
preprocessing:
accessibility-notes:
notes:
---
```

### Collection metadata
```yaml
name:
sources:
  -
items:
  -
```

## Sources

| Name                                                  | Made / maintained by | Issue                                         | Claimed by            |
|-------------------------------------------------------|----------------------|-----------------------------------------------|-----------------------|
| lipu kule ([site][lk site] / [repo][lk repo])         | akesi Jan            | https://github.com/kulupu-lapo/poki/issues/9  | kala Asi              |
| Writing contests ([site][um site] / [repo][um repo])  | jan Lakuse           | https://github.com/kulupu-lapo/poki/issues/11 | kala Asi              |
| kalama sin ([site][ks site] / [ws][ks ws])            | various              | https://github.com/kulupu-lapo/poki/issues/12 | kala Asi              |
| lipu tenpo ([site][lt site] / [repo][lt repo])        | jan Alonola          | https://github.com/kulupu-lapo/poki/issues/10 | ijo vivi              |
| [TP Library][tonyu lib]                               | kala pona Tonyu      | https://github.com/kulupu-lapo/poki/issues/22 | jan Juwan             |
| Personal websites                                     | various              | https://github.com/kulupu-lapo/poki/issues/17 | ijo vivi              |
| Song collection ([yt][songs yt] / [docs][songs doc])  | jan Ke Tami          | No                                            | jan Juwan             |
| [Wikisource]                                          | various              | No                                            |                       |
| [Corpora]                                             | (sona pona)          | No                                            |                       |
| [nltk-tp]                                             | davidar              | No                                            |                       |
| [kijetesantakalu o!][kije o]                          | jan Ke Tami          | No                                            | ijo vivi              |
| [Archive Of Our Own][AO3]                             | various              | No                                            | ijo vivi              |
| [jan Lentan's blog posts][Lentan]                     | jan Lentan           | No                                            | jan Kita              |
| [lipu monsuta]                                        | soweli kina          | No                                            | jan Kita              |
| [jan Telakoman's blog posts][Telakoman]               | jan Telakoman        | No                                            | jan Kita              |
| [Storyweaver]                                         | various              | No                                            | jan Kita              |

[lk site]:https://lipukule.org/
[lk repo]:https://github.com/lipukule/lipu-kule
[um site]:https://utala.pona.la
[um repo]:https://github.com/raacz/utala
[ks site]:https://redcircle.com/shows/kalama-sin
[ks ws]:https://wikisource.org/wiki/Kalama_sin
[lt site]:https://liputenpo.org/
[lt repo]:https://github.com/lipu-tenpo/liputenpo.org
[songs yt]:https://www.youtube.com/playlist?list=PLc7R2x5fn6AqRFUR9JzGIqh0FMdtsXRnH
[songs doc]:https://docs.google.com/spreadsheets/d/1qXextl70wJUo9xJ0VzECLXb3smiroQDT8U2_aAb_ycM/edit
[tonyu lib]:https://docs.google.com/document/d/1IdMucmhPCzvoUF94Gp25XCwocWOl4PfQ_wfOkiU8cu8/edit?usp=sharing
[Wikisource]:https://wikisource.org/wiki/Category:Toki_pona
[Corpora]:https://sona.pona.la/wiki/Corpora
[nltk-tp]:https://github.com/davidar/nltk-tp/tree/master/Corpus
[kije o]:https://kijetesantakalu-o.tumblr.com/tagged/comic
[AO3]:https://archiveofourown.org/works/search?work_search%5Blanguage_id%5D=tok
[Lentan]:https://lipu-sona.pona.la/lentan/
[lipu monsuta]:https://lipumonsuta.neocities.org/
[Telakoman]:https://joelthomastr.github.io/tokipona/README_si
[Storyweaver]:https://storyweaver.org.in/en/stories?language=Toki+Pona

## Contributing

<div align="center">
  <a href="https://github.com/kulupu-lapo/poki/graphs/contributors">
    <img src="https://contrib.rocks/image?repo=kulupu-lapo/poki" />
  </a>
</div>

Feel free to post issues, fork the repo, and open pull requests with your changes.  \
You can also join the "ma pona pi toki pona" discord to talk to the maintainers.

Thank you to [ilo Nija](https://nia.dog/) for the creating the logo.

# License

The creative works listed in `plaintext` all belong to their respective copyright holders.  \
The logo is licensed under [CC0 1.0 Universal](https://creativecommons.org/public-domain/cc0/).
