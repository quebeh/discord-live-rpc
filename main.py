from pypresence import Presence
from time import sleep, time
from psutil import cpu_percent, virtual_memory
import win32gui


def GetDetails(fgw):
    _details = "Doin' Nothin"
    if fgw.lower().endswith('discord'):
        _details = 'Chatting on Discord'
    elif fgw.lower().endswith('.py') or fgw.lower().endswith('.json'):
        _details = 'Coding python'
        if 'spacebot' in fgw.lower():
            _details = 'Developing Space bot'
    elif fgw.lower().startswith('telegram'):
        _details = 'Chatting on Telegram'
    elif fgw.lower().endswith('google chrome'):
        _details = 'Searching things on Google'
        if fgw.lower().endswith('youtube - google chrome'):
            _details = 'Watching YouTube'
        elif fgw.lower().endswith('google docs - google chrome'):
            _details = 'Working on a Google Docs project'
        elif fgw.lower().startswith('whatsapp'):
            _details = 'Chatting on WhatsApp'
        elif 'documentation' in fgw.lower():
            _details = 'Reading some docs on Chrome'
        elif fgw.lower().endswith('wikipedia - google chrome'):
            _details = f'Reading Wikipedia: {fgw.lower().split(" - ")[0].title()}'
        elif fgw.lower().endswith('medium - google chrome'):
            _details = 'Reading Medium Article on Chrome'
        elif fgw.lower().endswith('iq.com - google chrome'):
            _details = 'Watching Anime'
        elif fgw.lower().endswith('gmail - google chrome'):
            _details = 'Reading emails'
    elif fgw.lower()[:-4].endswith('paint.net'):
        _details = 'Editing an Image with paint.net'
    elif fgw.lower() == 'task switching':
        _details = 'On the alt+tab screen'
    return _details


client_id = '918485200781053962'  # Put your application ID here
im_asset = 'space'  # Put your image asset's name

RPC = Presence(client_id, pipe=0)

RPC.connect()
time = int(time())
tslept = 0
cpu = True
state = f'Using {round(cpu_percent(), 1)}% of CPU'
while True:
    FGWText = win32gui.GetWindowText(win32gui.GetForegroundWindow())
    print(f'\r{FGWText}', end='')
    details = GetDetails(FGWText)
    if tslept == 5:
        tslept = 0
        cpu = not cpu
        if cpu:
            state = f'Using {round(cpu_percent(), 1)}% of CPU'
        else:
            state = f'Using {round(virtual_memory().percent, 1)}% of RAM'
    RPC.update(
        large_image=im_asset,
        large_text='Photo of Space',
        details=details,
        state=state,
        start=time,
    )
    sleep(1)
    tslept += 1
