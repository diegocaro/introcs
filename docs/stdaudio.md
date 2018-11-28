# stdaudio

stdaudio.py

The stdaudio module defines functions related to audio.

## wait
```python
wait()
```

Wait for the sound queue to become empty.  Informally, wait for the
currently playing sound to finish.

## playSample
```python
playSample(s)
```

Play sound sample s.

## playSamples
```python
playSamples(a)
```

Play all sound samples in array a.

## playArray
```python
playArray(a)
```

This function is deprecated. It has the same behavior as
stdaudio.playSamples(). Please call stdaudio.playSamples() instead.

## playFile
```python
playFile(f)
```

Play all sound samples in the file whose name is f.wav.

## save
```python
save(f, a)
```

Save all samples in array a to the WAVE file whose name is f.wav.

## read
```python
read(f)
```

Read all samples from the WAVE file whose names is f.wav.
Store the samples in an array, and return the array.

