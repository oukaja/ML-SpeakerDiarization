# Speaker Diarization
speaker diarization system

## Content
Features are extracted from wav files, then unsupervised learning or supervised learning derived speaker recognition and a certain speaker's voice starting points, ending points

## Data preprocessing
###unsupervised learning
<pre>
	wavs --> features --> kmeans(silhouette) --> num of speaker and time point
</pre>

## Requirements
<pre>
scipy
librosa
sklearn
numpy
</pre>
