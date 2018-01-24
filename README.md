# Music Advice System Using Acoustic Features
Within the scope of the project, it was aimed to present suggestions to user by
extracting similarity between datasets containing many music. It is aimed to find the
connection of the proposals made with the given music or similarity from the obvious
features. The project does not work on a profile basis like the other applications in the
literature. For this reason, we have various advantages. In the profile-based system, it
is necessary to keep the past transaction details of the users. In the scope of the project,
only specific features of music are extracted and similarities are measured by using the
k nearest neighborhood algorithm among these properties. The application keeps the
musics as a working structure under a folder and the properties of these music are
kept in the database. Once processed, the music does not need to be processed again.
Features extracted for the suggestion can taken from the database. The project has
been developed as a desktop application. The modules included in the interface are
the property table, the extracted property data, the music-based waveform drawing
screen and a simple music player. It has been developed with a dock widget to make
it more flexible. Many of the techniques in the literature have been applied for music
feature extraction. Zero crossing, spectral centroid and spectral constrast methods
did not yield very successful results when applied at first, but the success rate of
the system increased when it was supported with techniques such as mel-frequency
cepstral coefficients, chroma, tonnetz.

### Prerequisites
Project developed on Anaconda Spyder. For music manipulation librosa library used.

### Mainframe
![Mainframe](GUI/Mainframe2.JPG?raw=true "Mainframe")
