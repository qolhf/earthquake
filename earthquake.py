from quakefeeds import QuakeFeed
import requests
print("The script is running and webhook notifications will send!")

#I KNOW THIS CODE IS NOT EFFICIENT I CODED IT FAST AND REALLY LATE..OK?..OK GOOD! 
while True:
    try:
        feed = QuakeFeed("4.5", "day")
        title = feed.event_title(0)
        time = feed.time
        depth = feed.depth(0)
        magnitude = feed.magnitude(0)

        webhook = "" #YOUR WEBHOOK HERE <<<

        message = """
        ```yaml
        A NEW EARTHQUAKE HAS HIT!

        HEADLINE: {}

        TIME: {}

        DEPTH: {}

        MAGNITUDE: {}

        COORDINATES: {}
        ```
        """.format(title, time, depth, magnitude, feed.location(0))

        with open("/tmp/earthquaketitle.txt", "r") as f:
            content = f.read()

        if content != title:
            send = requests.post('{}'.format(webhook), {
            'username': 'Qolhfs Earthquake Bot',
            'content': message,
            })

        with open("/tmp/earthquaketitle.txt", "w+") as f:
            f.write(title)
    except Exception as e:
        with open("/root/error.txt", "w") as ffff:
            ffff.write(e)

