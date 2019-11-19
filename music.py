
from pybricks import ev3brick as brick
from pybricks.tools import print, wait, StopWatch
from threading import Thread

class Note:

    C0 = 16.35
    C0S = 17.32
    D0 = 18.35
    D0S = 19.45
    E0 = 20.60
    F0 = 21.83
    F0S = 23.12
    G0 = 24.50
    G0S = 25.96
    A0 = 27.50
    A0S = 29.14
    B0 = 30.87

    def __init__(self, freq, duration):
        self.freq = freq
        self.duration = duration

class NoteFactory:

    def createNote(noteCode, octave, length):
       return Note(NoteFactory.findFrequency(noteCode) * pow(2, octave), length)

    def findFrequency(noteCode):
        if(noteCode == "C"):
            return Note.C0
        if(noteCode == "CS"):
		    return Note.C0S
        if(noteCode == "D"):
            return Note.D0
        if(noteCode == "DS" or noteCode == "EB"):
            return Note.D0S
        if(noteCode == "E"):
            return Note.E0    
        if(noteCode == "F"):
            return Note.F0    
        if(noteCode == "FS" or noteCode == "GB"):
            return Note.F0S
        if(noteCode == "G"):
            return Note.G0   
        if(noteCode == "GS" or noteCode == "AB"):
            return Note.G0S
        if(noteCode == "A"):
            return Note.A0   
        if(noteCode == "AS" or noteCode == "BB"):
            return Note.A0S
        if(noteCode == "B"):
            return Note.B0
        return 0
					
class Track:
    def __init__(self, notes):
        self.notes = notes

class TrackPlayer(Thread):

    def __init__(self, track, bmp, m_time_sync):
        Thread.__init__(self)
        self.time = 0
        self.noteDelay = 100
        self.lastStartTime = 0
        self.position = 0
        self.track = track
        self.bmp = bmp
        self.m_time_sync = m_time_sync

    def run(self):
        start_time = self.m_time_sync.getTimeSync()
        while(1):
            self.play(3,(self.m_time_sync.getTimeSync() - start_time)*1000)


    def play(self, volume, masterTime):
        if(not self.isOver() and masterTime >= self.time):
            note = self.track.notes[self.position]
            duration = TimeUtils.computeDuration(note.duration, self.bmp)
            if(note.freq == 0):
                wait(duration)
            else:
                duration = duration - self.noteDelay
                brick.sound.beep(note.freq, duration, volume)
                wait(self.noteDelay)
            self.time += duration
            self.position += 1
    
    def setTime(self, newTime):
        self.reset()
        
        ok = False
        while(not ok and self.position < len(self.track.notes)):
            note = self.track.notes[self.position]
            duration = TimeUtils.computeDuration(note.duration, self.bmp)
            if(self.time + duration < newTime):
                self.time += duration
                self.position += 1
            else:
                ok = True

    def getTime(self):
        return self.time

    def isOver(self):
        return self.position >= len(self.track.notes)

    def reset(self):
        self.position = 0
        self.time = 0

class TimeUtils:
    def computeDuration(noteDuration, bmp):
        return noteDuration * 1000 * 60 / float(bmp) * 4

class TrackReader:
    def read(self, file):
        f = open(file, "r")
        values = f.readlines()
        f.close()
        notes = []
        for x in values:
            if len(x) > 2:
                notes.append(self.readNote(x))

        return Track(notes)

    def readNote(self, strNote):
        parts = strNote.split(' ')
        noteCode = parts[0]
        octave = parts[1]
        length = parts[2]
        return NoteFactory.createNote(noteCode, int(octave), float(length))