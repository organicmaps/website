---
title: "Organic Maps Turns 4: The Privacy-Focused Alternative to Google Maps"
date: 2024-12-20T09:00:00+00:00
slug: "organicmaps-turns-four"
---

**Organic Maps**, the privacy-focused, open-source alternative to Google Maps, celebrates its 4th anniversary. The project came to life during Christmas week of 2020, between December 20 and December 28, as a response to the [temporary clinical death of MAPS.ME 2.0 on December 20, 2020](https://telegra.ph/What-happened-to-the-old-MAPSME-12-20). Cheers to the journey! Long live, Organic Maps! Long live, MAPS.ME too! Let a hundred flowers blossom! Merry Christmas.

## Organic Maps Today

What have we achieved so far as we approach Christmas 2024:

- ~3M¹ users from all countries of the world
- ~15k ratings and reviews on AppStore and Google Play
- 4.8/4.6 average rating on AppStore/Google Play
- 10k+ stars on [GitHub](https://github.com/organicmaps/organicmaps)
- 10k (almost) issues + PRs on [GitHub](https://github.com/organicmaps/organicmaps)
- 1k (almost) forks on [GitHub](https://github.com/organicmaps/organicmaps)
- 7k+ git commits made by 100+ contributors
- $0 spend on marketing - pure Organic growth

¹ Approximated number based on data from the App Store, Google Play, as the app has no analytics and does not collect any user data.

## The Origins

It is a good moment to reflect on how it all started.

### MapsWithYou

Once upon a time, there was a great travel maps app called **MapsWithMe** (renamed to MAPS.ME in 2014). The app was powered by [OpenStreetMap](https://wiki.openstreetmap.org/wiki/About_OpenStreetMap) map data, kind of like Wikipedia, but for maps. Unlike OpenStreetMap, which has always been an [open community effort](https://wiki.openstreetmap.org/wiki/About_OpenStreetMap), MapsWithMe [originated](https://wiki.openstreetmap.org/wiki/MAPS.ME/History) as a **proprietary**, **closed-source** app developed by [MapsWithMe GmbH](https://zh.chregister.ch/cr-portal/auszug/auszug.xhtml?uid=CHE-208.496.491). The app had two variants - a free limited version and a **paid** "Pro" version with extra features. [Over 7M users have downloaded](https://vk.company/en/press/releases/9209/) the app since its release in 2011 until Nov 2014.

### MapsWithCode

As happens time and again, in Nov 2014 the original owners [sold the company](https://www-rbc-ru.translate.goog/rbcfreenews/5464b2eacbb20ff538342f8f?_x_tr_sl=ru&_x_tr_tl=en&_x_tr_hl=en-US) to a Russian Big Tech conglomerate, for around [$18M +/-](https://vk.company/en/investors/info/10761/). As is common in such deals, the buyer likely required the original team to stay on for about a year, after which they probably moved on to their new endeavours.

The Big Tech conglomerate invested millions and millions more, hired more and more engineers, and delivered [tons of cool features](https://vk.company/en/press/releases/10100/) we all love in the Organic Maps today. In 2015, one year after the purchase, they made a bold decision to [open-source the app under the Apache 2.0 license](https://www.businesswire.com/news/home/20150930005526/en/MAPS.ME-Goes-Open-Source). The [official statement](https://www.businesswire.com/news/home/20150930005526/en/MAPS.ME-Goes-Open-Source) was:

> “We are happy to share our vision of open and free software available for communities around the globe. The whole team at MAPS.ME appreciates the opportunity to contribute in HOT’s humanitarian missions and help to serve in areas of disasters and political crises,” … “Opening MAPS.ME is an important step not just for us, but for the whole free mapping community, as OSM will become even more accessible for a wider audience, which, I hope, will attract new editors to join this outstanding movement.”

### CryptoWithoutMaps

Years after making no profit, in the November 2020 Big Tech made another [bold decision to sell its "non-core" Maps asset](https://vk.company/en/investors/info/10761/) for about $20M to [CryptoFinTech bros reportedly connected](https://www.theguardian.com/technology/2023/mar/26/caught-in-the-ftx-storm-how-a-crypto-high-flyer-fell-to-earth) to the famous, now-jailed, [Sam Bankman-Fried](https://www.justice.gov/opa/pr/samuel-bankman-fried-sentenced-25-years-his-orchestration-multiple-fraudulent-schemes) of [FTX](https://en.wikipedia.org/wiki/Bankruptcy_of_FTX), a Bahamas-based cryptocurrency exchange.

The new FinTech owners, as [reported by Guardian](https://www.theguardian.com/technology/2023/mar/26/caught-in-the-ftx-storm-how-a-crypto-high-flyer-fell-to-earth), had a brilliant idea how to monetize the wide user base by adding digital payments. At one point, they had up to 1 million people on the waiting list for Maps digital wallet. While the idea was smart, [things didn't follow the plan](https://www.theguardian.com/technology/2023/mar/26/caught-in-the-ftx-storm-how-a-crypto-high-flyer-fell-to-earth).

Back to our story. On **December 20, 2020**, version 2.0 of the MAPS.ME app was pushed to the Apple App Store. The new update de-facto was a brand-new app, completely re-done from scratch using the MapBox SDK (which itself was pretty great). Unsurprisingly, [some if not all old users were a bit disappointed](https://www.reddit.com/r/openstreetmap/comments/khsjqx/mapsme_seems_have_reached_its_end/).

[Alexander Borsuk](https://github.com/biodranik) and [Viktor Govako](https://github.com/vng), co-founders of the original MapsWithMe, also were disappointed. On the next day, on **December 21, 2020**, they registered [organicmaps.app](https://organicmaps.app) domain and [organicmaps github org](https://github.com/organicmaps/), and started to work on the last open-source version of MAPS.ME under a new name.

### OriginalMapsMe

Independently, one of the frustrated users drafted a post named ["MAPS.ME is gone. We must bring it back"](https://telegra.ph/What-happened-to-the-old-MAPSME-12-20) which shared a link to a Telegram group. Open-source ethusiasts started to gather together in the group to brainstorm how to bring MAPS.ME back. Dozens of open-source forks popped up during the first week by different people. Let a thousand flowers bloom!

Just to recall, the original MapsWithMe was **100% proprietary**. Although Big Tech later licensed the source code under Apache 2.0 and moved developemnt to the GitHub, the development process still followed the enterprise-style approaches, relying on an internal decision-making process, internal trackers, and infrastructure. The project had never gained self-governance and was always managed by full-time employees of the corporation.

Endless brainstorming on this and other topics in the Telegram group eventually led to a lengthy voice call between [Roman Tsisyk and Alexey Naumenko](https://github.com/organicmaps/community/wiki/Members), that resulted in the parallel kick-start of **this project**. The intention was to create a proper, community-driven open-source project, open to any parties willing to participate.

### OMaps

The initial name was "OMaps", obviously elaborating on Open and Original Maps. Rebranding to the current brand happened months, months later, but it is a story for another time.

Effectively, the foundation of the current open-source project was bootstrapped during ~20 hours hackathon betweem December 27-28, 2020. What had been done by the end of the day on December 28, 2020 with further follow-ups in the next few days:

- The founding GitHub [issue #1](https://github.com/organicmaps/organicmaps/issues/1), finished.
- The comprehensive project plan, initially consisting of about 30 GitHub issues, lately extended to 100+ tickets: [#1](https://github.com/organicmaps/organicmaps/issues/1), [#2](https://github.com/organicmaps/organicmaps/issues/2), [#3](https://github.com/organicmaps/organicmaps/issues/3), [#4](https://github.com/organicmaps/organicmaps/issues/4), [#5](https://github.com/organicmaps/organicmaps/issues/5), [#6](https://github.com/organicmaps/organicmaps/issues/6), [#7](https://github.com/organicmaps/organicmaps/issues/7), [#8](https://github.com/organicmaps/organicmaps/issues/8), [#9](https://github.com/organicmaps/organicmaps/issues/9), [#10](https://github.com/organicmaps/organicmaps/issues/10), [#11](https://github.com/organicmaps/organicmaps/issues/11), [#12](https://github.com/organicmaps/organicmaps/issues/12), [#13](https://github.com/organicmaps/organicmaps/issues/13), [#14](https://github.com/organicmaps/organicmaps/issues/14), [#15](https://github.com/organicmaps/organicmaps/issues/15), [#16](https://github.com/organicmaps/organicmaps/issues/16), [#17](https://github.com/organicmaps/organicmaps/issues/17), [#18](https://github.com/organicmaps/organicmaps/issues/18), [#19](https://github.com/organicmaps/organicmaps/issues/19), [#20](https://github.com/organicmaps/organicmaps/issues/20), [#21](https://github.com/organicmaps/organicmaps/issues/21), [#22](https://github.com/organicmaps/organicmaps/issues/22), [#23](https://github.com/organicmaps/organicmaps/issues/23), [#24](https://github.com/organicmaps/organicmaps/issues/24), [#25](https://github.com/organicmaps/organicmaps/issues/25), [#26](https://github.com/organicmaps/organicmaps/issues/26), [#27](https://github.com/organicmaps/organicmaps/issues/27), [#28](https://github.com/organicmaps/organicmaps/issues/28), [#29](https://github.com/organicmaps/organicmaps/issues/29), [#30](https://github.com/organicmaps/organicmaps/issues/30), [#31](https://github.com/organicmaps/organicmaps/issues/31), [#32](https://github.com/organicmaps/organicmaps/issues/32), [#33](https://github.com/organicmaps/organicmaps/issues/33), [#34](https://github.com/organicmaps/organicmaps/issues/34), [#35](https://github.com/organicmaps/organicmaps/issues/35).
- The initial project [governance document](https://github.com/organicmaps/community/wiki/Governance), pointing [Roman Tsisyk](https://github.com/organicmaps/community/wiki/Member:Roman-Tsisyk) as an "interim project manager" and a commitment to establish the governing board before the end of 2021 (done).
- Initial [team structure](https://github.com/organicmaps/community/wiki/Members) with [Alexey Naumenko](https://github.com/ooprizrakoo) in charge of the community relations and recruting enthusiasts (hats off for the excellent work!).
- Initial [set of guidelines](https://github.com/organicmaps/community/wiki/Commit-Messages) and policies, including the Code of Conduct.
- Notable [shift from using the CLA](https://github.com/organicmaps/organicmaps/issues/5) (Contributor License Agreement), which required contributors to license their changes to some owners, to using the DCO (Developer Certificate of Origin), which keeps the copyrights assigned to the contributors. It was done intentionally to prevent any possibility of closing the sources or changing the licenses in the future.
- Initial [infrastructure](https://github.com/organicmaps/community/wiki/Infrastructure), including CI/CD and hosting for maps files.
- [Initial efforts](https://github.com/organicmaps/organicmaps/commits/master/?since=2020-12-25&until=2021-01-04) focused on rebranding, removing ads, eliminating copyrighted graphics, and removing functionality dependent on proprietary backends.
- Telegram Groups, Slack Workspace, Twitter and other communication channels.
- Bonus: A prototype of bookmark management web UI based on [uMap](https://umap-project.org/) (never got integrated into the app, unfortunally).

Everyone was invited to join forces on the community-driven open-source project. The new MAPS.ME team was invited to the party too (Hey A G, up for a pint near Liverpool St?). The old team was invited as well. No background checks were performed (regretting). Everyone was welcomed to join and contribute. Of course, under the open-source license with no more proprietary backends, just to avoid entering into the MapsNotWithUs loop again. This open call is still valid.

### Further Development

The first Android release under the "app.omaps" application identifier was finally approved by Google Play on **January 3, 2021**. The data was initially sourced from the old [Axet's fork](https://gitlab.com/axet/omim/-/tree/master/tracking). The first ever bug-report from an user was received on **January 5, 2021**.

### Joined efforts

On January 7, 2021, Alexey Naumenko organized a call between Roman, Alexander and Viktor. And the three of them agreed to join forces and work together on the new project.

This is how it all got started. There was still a long road ahead, but it is a story for another time. This fork was the right one and it has survived the evolution. Now 10k+ GitHub stars and 100+ contributors. This is what the "Fork" button is all about.

Congratulations to all the users and contributors for your hard work and dedication! Thank you for being a part of this journey! Merry Christmas!
