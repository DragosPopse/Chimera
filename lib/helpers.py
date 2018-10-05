import sys
from lib.input_commands import InputCommands

def get_operating():
    platforms = {
        'linux': 'Linux',
        'linux1': 'Linux',
        'linux2': 'Linux',
        'darwin': 'OS X',
        'win32': 'Windows'
    }
    if sys.platform not in platforms:
        return sys.platform

    return platforms[sys.platform]

class MediaControlAdapter():
    VK_VOLUME_DOWN = 0
    VK_VOLUME_UP = 1
    VK_VOLUME_MUTE = 2
    VK_MEDIA_NEXT_TRACK = 3
    VK_MEDIA_PREV_TRACK = 4
    VK_MEDIA_STOP = 5
    VK_MEDIA_PLAY_PAUSE = 6
    
    _command_list = {
        'Linux':{
            VK_VOLUME_MUTE:269025042,
            VK_VOLUME_DOWN:269025041,
            VK_VOLUME_UP:269025043,
            VK_MEDIA_NEXT_TRACK:269025047,
            VK_MEDIA_PREV_TRACK:269025046,
            VK_MEDIA_STOP:269025045,
            VK_MEDIA_PLAY_PAUSE:269025044
        },
        'Windows':{
            VK_VOLUME_MUTE:173,
            VK_VOLUME_DOWN:174,
            VK_VOLUME_UP:175,
            VK_MEDIA_NEXT_TRACK:176,
            VK_MEDIA_PREV_TRACK:177,
            VK_MEDIA_STOP:178,
            VK_MEDIA_PLAY_PAUSE:179
        }
    }
    
    def __init__(self,os_name):
        self.os_name = os_name
        self.input_commands = InputCommands()
        
    def up_volume(self):
        virtual_key_id = self._command_list[self.os_name][self.VK_VOLUME_UP]
        self.input_commands.press_release(virtual_key_id)
    def down_volume(self):
        virtual_key_id = self._command_list[self.os_name][self.VK_VOLUME_DOWN]
        self.input_commands.press_release(virtual_key_id)
    def mute_volume(self):
        virtual_key_id = self._command_list[self.os_name][self.VK_VOLUME_MUTE]
        self.input_commands.press_release(virtual_key_id)
    def media_next(self):
        virtual_key_id = self._command_list[self.os_name][self.VK_MEDIA_NEXT_TRACK]
        self.input_commands.press_release(virtual_key_id)
    def media_previous(self):
        virtual_key_id = self._command_list[self.os_name][self.VK_MEDIA_PREV_TRACK]
        self.input_commands.press_release(virtual_key_id)
    def media_stop(self):
        virtual_key_id = self._command_list[self.os_name][self.VK_MEDIA_STOP]
        self.input_commands.press_release(virtual_key_id)
    def media_play_pause(self):
        virtual_key_id = self._command_list[self.os_name][self.VK_MEDIA_PLAY_PAUSE]
        self.input_commands.press_release(virtual_key_id)
    
