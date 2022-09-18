tv_shows = {
    "The X-Files": {
        "Season 1": {
            "Episodes": ["Scary Monster", "Scary Alien"],
            "Year": 1993,
            "Genre": "Science Fiction"
        },
        "Season 2": {
            "Episodes": ["Scary Conspiracy"],
            "Year": 1994,
            "Genre": "Horror"
        }
    },
    "Lost": {
        "Season 1": {
            "Episodes": ["What the heck is happening on this island?"],
            "Year": 2004,
            "Genre": "Science Fiction"
        }
    }
}

print(tv_shows["The X-Files"]["Season 1"]["Episodes"][1])
print(tv_shows["The X-Files"]["Season 2"]["Genre"])
print(tv_shows["Lost"]["Season 1"]["Year"])

nba_finals = {

  "Game 1": {

    "date": "05/05/2019",

    "location": "San Francisco",

    "statistics": {

      "points": 200,

      "rebounds": 20,

      "assists": 25
    }
  }
}

print(nba_finals["Game 1"]["statistics"]["rebounds"])

my_dict = {

  "a": {

    1: 2,

    3: 4,

    5: {

      6: 7,

      8: 9
    }
  }
}