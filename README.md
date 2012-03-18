A sad-soo is a sad [Yong-Soo Chung](https://twitter.com/#!/yongsoochung).

## Usage

Fetch a random sad-soo:

    $ curl http://sad-soo.herokuapp.com/random
    {
      "idol": "http://26.media.tumblr.com/tumblr_luz0q1X7AQ1r6j9k4o1_400.gif"
    }

Bomb sad-soo's (the `count` argument is optional, by default 5 idols are bombed):

    $ curl http://sad-soo.herokuapp.com/bomb?count=5
    {
      "sad-soo": [
        "http://24.media.tumblr.com/tumblr_lv4p1smS6I1r6j9k4o1_250.gif",
        "http://30.media.tumblr.com/tumblr_lxpdfl8cvS1r6j9k4o1_400.gif",
        "http://27.media.tumblr.com/tumblr_luz4a5t80W1r6j9k4o1_400.gif",
        "http://28.media.tumblr.com/tumblr_lxpdglIuBY1r6j9k4o2_400.gif",
        "http://24.media.tumblr.com/tumblr_ly37wbKxSD1r6j9k4o2_400.gif"
      ]
    }

Count how many sad-soo's we have:

    $ curl http://sad-soo.herokuapp.com/count
    {
      "count": 382
    }


## Special Thanks

Many thanks for the flask bombing template, forked from [Bryan Veloso](https://github.com/bryanveloso/aidoru)