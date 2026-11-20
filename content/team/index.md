---
title: The people behind Organic Maps
description: Meet the small team and the big community that build Organic Maps, a free offline maps app with no ads and no tracking.
template: team.html
weight: 40
extra:
  # menu_title is what puts the page in the footer: bottom_menu.html links
  # every page that has one, on the whole site.
  menu_title: Team
  # Without this the link preview takes the first image next to this file,
  # which is somebody's avatar. The site-wide default until a team image exists.
  preview_image: images/screenshots/prague.jpg
  founders_title: Founders
  core_title: Core team
  contributors_title: Contributors
  contributors_text: People who regularly help with code, translations, maps, testing and support.
  join_title: This could be you
  join_text: Code, translations, map edits or helping other users — every contribution counts.
  # Labels of each person's spec sheet. The page prints them in lowercase, like
  # the group titles above. "github" and the label of each link are not here:
  # they are names. The open place says join_role under role_label and links
  # how_label to the contribute page, under that page's own menu title.
  role_label: Role
  team_label: Team
  join_role: Open
  how_label: How
  community_label: Community
  # Every person keeps all seven keys. location is where they are, a city and
  # country or just a country, shown with a pin under the bio; "" leaves it
  # out. It is its own key so that the bio stays about their work. github is
  # the login, shown as @login and linked to the profile. photo is a square
  # image, 640 px, saved next to this file and named after the login: a photo
  # the person sent or their GitHub avatar, with its metadata stripped, or ""
  # for the silhouette. Keep only photos in use here, since Zola publishes
  # every file next to this page. links holds anything beyond GitHub, and may
  # be []; the page shows each url without its scheme. Keep bio and
  # location in double quotes: a colon followed by a space breaks an unquoted
  # YAML value.
  founders:
    - name: Alexander Borsuk
      role: Co-founder
      location: "Zürich, Switzerland"
      github: biodranik
      bio: "Co-founder of Organic Maps and creator of MAPS.ME."
      photo: biodranik.jpg
      links:
        - { label: Website, url: "https://alex.bio/" }
    - name: Viktor Havaka
      role: Co-founder
      location: "Buenos Aires, Argentina"
      github: vng
      bio: "Former MAPS.ME co-founder, former Mapboxer."
      photo: vng.jpg
      links:
        - { label: LinkedIn, url: "https://www.linkedin.com/in/vng/" }
  members:
    - name: Kiryl Kaveryn
      role: iOS
      location: "Poland"
      github: kirylkaveryn
      bio: "The team's iOS expert, working across the whole iOS app."
      photo: kirylkaveryn.jpg
      links:
        - { label: LinkedIn, url: "https://www.linkedin.com/in/kiryl-kaveryn/" }
    - name: Mikhail Listratsenka
      role: Android & Wear OS
      location: "Warsaw, Poland"
      github: strider-dunadan
      bio: "Works across the whole Android app and the Wear OS watch app."
      photo: strider-dunadan.jpg
      links:
        - { label: LinkedIn, url: "https://www.linkedin.com/in/mikelijordan/" }
    - name: Dina Barysevich
      role: User support
      location: "Lithuania"
      github: dinabarysevich
      bio: "Helps Organic Maps users with their questions and problems, and passes their reports on to the developers."
      photo: dinabarysevich.jpg
      links: []
    - name: Natalia Yakavenka
      role: App stores & social media
      location: "Tbilisi, Georgia"
      github: yanatalia
      bio: "Optimises the app's App Store and Google Play listings, helping Organic Maps get more users."
      photo: yanatalia.jpg
      links:
        - { label: LinkedIn, url: "https://www.linkedin.com/in/yakavenkan/" }
  # Contributors, one line each: name, role (what they help with) and github,
  # or the first of their links when they have no github. The section is
  # hidden while the list is empty.
  contributors: []
---

We are a small team of enthusiasts building a free, open-source maps app that works offline, shows no ads and does not track you.

<!-- team -->

## Built together with the community

Organic Maps would not exist without volunteers from all over the world: developers who send fixes, translators, testers, and OpenStreetMap mappers who keep the map up to date.

[See everyone who contributed](https://github.com/organicmaps/organicmaps/graphs/contributors) [Find out how you can help](@/contribute/index.md)
