import progressbar
from time import sleep
from progressbar import AnimatedMarker, Bar, BouncingBar, Counter, ETA, \
    FileTransferSpeed, FormatLabel, Percentage, \
    ProgressBar, ReverseBar, RotatingMarker, \
    SimpleProgress, Timer

widgets1 = [progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()]
widgets5 = ['test', progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()]

widgets2 = ['Test: ', Percentage(), ' ', Bar(marker=RotatingMarker()), ' ', ETA(), ' ', FileTransferSpeed()]
widgets3 = ['WIDGETS3: ', Percentage(), ' ', Bar(marker=RotatingMarker()), ' ', ETA(), ' ']
widgets4 = ['WIDGETS4: ', Percentage(), ' ', Bar(marker='='), ' ', ETA(), ' ']
bar = progressbar.ProgressBar(maxval=20, widgets=widgets5)
bar.start()
for i in range(20):
    bar.update(i+1)
    sleep(0.1)
bar.finish()