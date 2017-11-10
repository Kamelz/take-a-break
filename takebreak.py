import webbrowser
import time

#  ------------------------- App functions --------------------------------

# opens the requested url in the browser


def open_in_browser(url):
    webbrowser.open(url)


# evaluating the requested job and runs the targeted function.


def run(job):
    eval(job)


# run a job with a timeout by seconds


def operation(job, timer):
    time.sleep(timer)
    run(job)


# schedule repeatativ or nonrepetativ job with a timeout by seconds


def schedule_job(job, timer, repeat=False):
    if (repeat):
        while True:
            print(time.ctime())
            operation(job, timer)
    else:
        print(time.ctime())
        operation(job, timer)


# -------------------------Main app body--------------------------------

url = 'https://www.youtube.com/watch?v=JGwWNGJdvx8'

# 2h
# timer = 7200
timer = 6

job = "open_in_browser('" + url + "')"

schedule_job(job, timer, True)
