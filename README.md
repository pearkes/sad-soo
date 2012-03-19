A sad-soo is a sad [Yong-Soo Chung](https://twitter.com/#!/yongsoochung).

## Usage

Fetch a random sad-soo:

    $ curl http://sad-soo.herokuapp.com/random
    {
      "sad_soo": "http://sad-soo.s3.amazonaws.com/hot-startup.jpg"
    }

Bomb sad-soo's (the `count` argument is optional, by default 3 sad-soo's are bombed):

    $ curl http://sad-soo.herokuapp.com/bomb?count=3
    {
      "sad_soos": [
        "http://sad-soo.s3.amazonaws.com/hot-startup.jpg",
        "http://distilleryimage2.s3.amazonaws.com/0f1acefe696711e1989612313815112c_7.jpg",
        "http://sad-soo.s3.amazonaws.com/emails.jpg
      ]
    }

Count how many sad-soo's we have:

    $ curl http://sad-soo.herokuapp.com/count
    {
      "count": 3
    }

## Need More Sad-soo's

Pull request your sad-soo's.

## Special Thanks

Many thanks for the flask bombing template, forked from [Bryan Veloso](https://github.com/bryanveloso/aidoru)