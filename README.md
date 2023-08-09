### AI-ChatBot That speaks to you!
#### To Download
<p>In your CLI navigate to a parent folder to download the Repo into</p>
type: 
```git clone https://github.com/Sarah-Stodder/AI-Chatbot```

#### To Install
In your CLI (in the parent folder where you did the clone) cd into the directory you cloned `cd AI-Chatbot`

# Create a virtual environment 


### Windows/Linux:
 ```
 python -m venv\venv
 ```
### Mac
```
python3 -m venv venv
```

## Activate Venv 
### Windows
```
venv\Scripts\activate
```

### Mac/Linux:
```
source venv/bin/activate
```
### Install dependencies:
on MacOSx: `brew install portaudio`
then all systems type:
` pip install -r requirements.txt`
### To Run
in the CLI while in the AI-Chatbot folder
type on windows: `venv\Scripts\activate` (If not already active)
type on Mac/Linux:`. venv/bin/activate` (If not already active)
type:`python chat.py`