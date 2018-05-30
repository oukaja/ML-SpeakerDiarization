# Speaker Diarization
speaker  diarization system

## Content
Features are extracted from wav files, then unsupervised learning certain speaker's voice starting points, ending points

## Data preprocessing
###unsupervised learning
<pre>
	wavs --> features --> kmeans(silhouette) --> num of speaker and time point
</pre>

## Requirements
<pre>
scipy==1.0.0
librosa==0.5.1
sklearn==0.18.1
numpy==1.14.0
</pre>

