# This script allows for extra scripts assigned to buttons for custom per skin creator functions to share ideas
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from collections import namedtuple
import xbmc, xbmcaddon, xbmcgui, xbmcplugin
import sys
import os
import xbmcvfs
import shutil
import re
import glob
import string
from rpc import RPC

# THIS ADDON
#try: from skin_ini import ADDONID
#except ImportError: ADDONID = 'script.tvguide.fullscreen.skin.cake'   # set this to your skin addonid
ADDONID       = 'script.tvguide.fullscreen.skin.cake'
ADDON         = xbmcaddon.Addon(id=ADDONID)
addonPath     = xbmc.translatePath(os.path.join('special://home', 'addons', ADDONID))
basePath      = xbmc.translatePath(os.path.join('special://profile', 'addon_data', ADDONID))
#
# MAIN ADDON such as script.tvguide.fullscreen
#try: from skin_ini import ADDONID_CORE
#except ImportError: ADDONID_CORE  = 'script.tvguide.fullscreen'      # set this to your dest addonid
ADDONID_CORE   = 'script.tvguide.fullscreen'
ADDON_CORE     = xbmcaddon.Addon(id=ADDONID_CORE)
addonPath_core = xbmc.translatePath(os.path.join('special://home', 'addons', ADDONID_CORE))
basePath_core  = xbmc.translatePath(os.path.join('special://profile', 'addon_data', ADDONID_CORE))
#
extrapath      = xbmc.translatePath(os.path.join(addonPath, 'resources'))
ICON           = xbmc.translatePath(os.path.join('special://home', 'addons', ADDONID, 'icon.png'))
tmp_path       = xbmc.translatePath(os.path.join('special://home', 'addons', 'packages'))
tmp_File       = xbmc.translatePath(os.path.join(basePath, 'tmp'))
dialog         = xbmcgui.Dialog()
dp             = xbmcgui.DialogProgress()




# FOR RECORDING grab or set executable and save paths
ffmpeg                 = ADDON_CORE.getSetting('autoplaywiths.ffmpeg')
autoplaywiths_folder   = ADDON_CORE.getSetting('autoplaywiths.folder')
udp                    = "udp://localhost:1234"
#udp                   = "udp://localhost:1234?buffer_size=10000000"
import json
# get name from playing or lastchannel in settings
import traceback
from subprocess import call
from subprocess import Popen
import time
timestr = time.strftime("%Y_%m%d__%H-%M")
start = timestr
streamUrl = 'none'
url = 'none'
channel = 'Channel'
player = xbmc.Player()
if player.isPlaying():
    url = player.getPlayingFile()
s = ADDON_CORE.getSetting('last.channel')
if s:
    (id, title, lineup, logo, streamUrl, visible, weight) = json.loads(s)
    channel = id
name = "PVR_%s_%s" % (channel,start)
name = name.encode("cp1252")
#url = "%s" % (url)
try: url = url.encode("cp1252")
except: pass






#################################################
# (Hopefully) Detect Skin
#################################################
skinPath = ''
# Ours - user set custom skin like script.tvguide.fullscreen.skin.cake to script.tvguide.fullscreen
if ADDON_CORE.getSetting('skin.source') == '2':
    skin_folder = ADDON_CORE.getSetting('skin.folder')
    skin_user   = ADDON_CORE.getSetting('skin.user')
    skinPath    = xbmc.translatePath(os.path.join(skin_folder, 'resources' , 'skins', skin_user))
#
# Yours - inside user_data  resources\skins\yourskinname
if ADDON_CORE.getSetting('skin.source') == '1':
    skin_user   = ADDON_CORE.getSetting('skin.user')
    skinPath    = xbmc.translatePath(os.path.join(basePath, 'resources' , 'skins', skin_user))
#
# Folder -  A Built in skin
if ADDON_CORE.getSetting('skin.source') == '0':
    skin_user   = ADDON_CORE.getSetting('skin')
    skinPath    = xbmc.translatePath(os.path.join(addonPath, 'resources' , 'skins', skin_user))
#


flipmenu = 'script-tvguide-menu.xml'
flipmain = 'script-tvguide-main.xml'
flipvod  = 'script-tvguide-vod-tv.xml'
flipstreamaddon = 'script-tvguide-streamaddon.xml'
flipstreamsetup = 'script-tvguide-streamsetup.xml'
#dialog.ok(ADDONID_CORE, ADDONID, skinPath, skin_user)  # For testing
#
deletedatabasedb = ADDON.getSetting('deletedatabasedb')
deletedatabase0 = ADDON.getSetting('deletedatabase0')
deletedatabase1 = ADDON.getSetting('deletedatabase1')
deletedatabase2 = ADDON.getSetting('deletedatabase2')
deletedatabase3 = ADDON.getSetting('deletedatabase3')
deletedatabase4 = ADDON.getSetting('deletedatabase4')
deletedatabase5 = ADDON.getSetting('deletedatabase5')
deletedatabase6 = ADDON.getSetting('deletedatabase6')
deletedatabase7 = ADDON.getSetting('deletedatabase7')
deletedatabase8 = ADDON.getSetting('deletedatabase8')
deletedatabase9 = ADDON.getSetting('deletedatabase9')
deletedatabase10 = ADDON.getSetting('deletedatabase10')
deletedatabase11 = ADDON.getSetting('deletedatabase11')
deletedatabase12 = ADDON.getSetting('deletedatabase12')
deletedatabase13 = ADDON.getSetting('deletedatabase13')
deletedatabase14 = ADDON.getSetting('deletedatabase14')
deletedatabase15 = ADDON.getSetting('deletedatabase15')
deletedatabase16 = ADDON.getSetting('deletedatabase16')
deletedatabase17 = ADDON.getSetting('deletedatabase17')
deletedatabase18 = ADDON.getSetting('deletedatabase18')
deletedatabase19 = ADDON.getSetting('deletedatabase19')
#
help1 = ADDON.getSetting('help1')
help2 = ADDON.getSetting('help2')
help3 = ADDON.getSetting('help3')
help4 = ADDON.getSetting('help4')
help5 = ADDON.getSetting('help5')
help6 = ADDON.getSetting('help6')
help7 = ADDON.getSetting('help7')
help8 = ADDON.getSetting('help8')
help9 = ADDON.getSetting('help9')
help10 = ADDON.getSetting('help10')
help11 = ADDON.getSetting('help11')
help12 = ADDON.getSetting('help12')
help13 = ADDON.getSetting('help13')
help14 = ADDON.getSetting('help14')
help15 = ADDON.getSetting('help15')
help16 = ADDON.getSetting('help16')
help17 = ADDON.getSetting('help17')
help18 = ADDON.getSetting('help18')
help19 = ADDON.getSetting('help19')
help20 = ADDON.getSetting('help20')
help21 = ADDON.getSetting('help21')
help22 = ADDON.getSetting('help22')
    
    
    
    
################################################################################
#   Skin Settings minimal
################################################################################
def skin_settings_minimal():
    import xbmc,xbmcgui,xbmcaddon
    dialog = xbmcgui.Dialog()
    #
    #ADDON_CORE = xbmcaddon.Addon("script.tvguide.fullscreen")
    #this = xbmcaddon.Addon(ADDONID)
    #
    # set skin dir name and title
    SKINS = [["Cake", "Cake"],
             ["-", "-"]]
    #
    d = xbmcgui.Dialog()
    names = [s[0] for s in SKINS]
    skin = d.select("TV Guide Fullscreen - Set Default Skin", names)
    if skin > -1:
        if ADDON_CORE:
            # Main Needed to run
            ADDON_CORE.setSetting('skin.source', '2')
            ADDON_CORE.setSetting('skin.folder', 'special://home/addons/'+ADDONID+'/')
            ADDON_CORE.setSetting('skin.user', SKINS[skin][1])
            dialog.ok('Done', 'Using "' + SKINS[skin][1] + '"')
        if not ADDON_CORE: dialog.ok('Error', 'Cannot set "' + SKINS[skin][1] + '"')
        
        
        
################################################################################
#   Skin Settings
################################################################################
def skin_settings():
    import xbmc,xbmcgui,xbmcaddon
    dialog = xbmcgui.Dialog()
    #
    #ADDON_CORE = xbmcaddon.Addon("script.tvguide.fullscreen")
    #this = xbmcaddon.Addon(ADDONID)
    #
    # set skin dir name and title
    SKINS = [["Cake", "Cake"],
             ["-", "-"]]
    #
    d = xbmcgui.Dialog()
    names = [s[0] for s in SKINS]
    skin = d.select("TV Guide Fullscreen - Set Default Skin", names)
    if skin > -1:
        if ADDON_CORE:
            # Main Needed to run
            ADDON_CORE.setSetting('skin.source', '2')
            ADDON_CORE.setSetting('skin.folder', 'special://home/addons/'+ADDONID+'/')
            ADDON_CORE.setSetting('skin.user', SKINS[skin][1])
            #
            # set epg path 30101
            ADDON_CORE.setSetting('xmltv.type', '1')
            ADDON_CORE.setSetting('xmltv.file', 'special://profile/addon_data/'+ADDONID+'/xmltv.xml')
            ADDON_CORE.setSetting('xmltv.url', ADDON.getSetting('xmltv.url'))
            ADDON_CORE.setSetting('gz', ADDON.getSetting('gz'))
            ADDON_CORE.setSetting('md5', ADDON.getSetting('md5'))
            ADDON_CORE.setSetting('xmltv.interval', ADDON.getSetting('xmltv.interval'))
            
            # NEW Lab3 Secondary XMLTV File
            ADDON_CORE.setSetting('xmltv2.enabled', ADDON.getSetting('xmltv2.enabled'))
            ADDON_CORE.setSetting('xmltv2.type', ADDON.getSetting('xmltv2.type'))
            ADDON_CORE.setSetting('xmltv2.file', ADDON.getSetting('xmltv2.file'))
            ADDON_CORE.setSetting('xmltv2.url', ADDON.getSetting('xmltv2.url'))
            # NEW Lab3 third XMLTV File
            ADDON_CORE.setSetting('xmltv3.enabled', ADDON.getSetting('xmltv3.enabled'))
            ADDON_CORE.setSetting('xmltv3.type', ADDON.getSetting('xmltv3.type'))
            ADDON_CORE.setSetting('xmltv3.file', ADDON.getSetting('xmltv3.file'))
            ADDON_CORE.setSetting('xmltv3.url', ADDON.getSetting('xmltv3.url'))
            
            # optional
            ADDON_CORE.setSetting('addons.ini.enabled', ADDON.getSetting('addons.ini.enabled'))
            ADDON_CORE.setSetting('addons.ini.file', ADDON.getSetting('addons.ini.file'))
            
            # set logos
            ADDON_CORE.setSetting('logos.source', ADDON.getSetting('logos.source'))
            ADDON_CORE.setSetting('logos.folder', ADDON.getSetting('logos.folder'))
            # Playback
            ADDON_CORE.setSetting('m3u.read', ADDON.getSetting('m3u.read'))
            ADDON_CORE.setSetting('catchup.text', ADDON.getSetting('catchup.text'))
            ADDON_CORE.setSetting('channel.shortcut', ADDON.getSetting('channel.shortcut'))
            ADDON_CORE.setSetting('play.alt.choose', ADDON.getSetting('play.alt.choose'))
            ADDON_CORE.setSetting('play.alt.continue', ADDON.getSetting('play.alt.continue'))
            ADDON_CORE.setSetting('stop.on.exit', ADDON.getSetting('stop.on.exit'))
            ADDON_CORE.setSetting('exit.on.back', ADDON.getSetting('exit.on.back'))
            # set Appearance
            ADDON_CORE.setSetting('epg.video.pip', ADDON.getSetting('epg.video.pip'))
            ADDON_CORE.setSetting('program.image.scale', ADDON.getSetting('program.image.scale'))
            ADDON_CORE.setSetting('stream.addon.list', ADDON.getSetting('stream.addon.list'))
            ADDON_CORE.setSetting('up.cat.mode', ADDON.getSetting('up.cat.mode'))
            ADDON_CORE.setSetting('action.bar', ADDON.getSetting('action.bar'))
            ADDON_CORE.setSetting('down.action', ADDON.getSetting('down.action'))
            ADDON_CORE.setSetting('program.search.plot', ADDON.getSetting('program.search.plot'))
            ADDON_CORE.setSetting('channel.logo', ADDON.getSetting('channel.logo'))
            ADDON_CORE.setSetting('addon.logo', ADDON.getSetting('addon.logo'))
            ADDON_CORE.setSetting('channels.per.page', ADDON.getSetting('channels.per.page'))
            ADDON_CORE.setSetting('channel.filter.sort', ADDON.getSetting('channel.filter.sort'))
            ADDON_CORE.setSetting('menu.addon', ADDON.getSetting('menu.addon'))
            # Background
            ADDON_CORE.setSetting('program.background.enabled', ADDON.getSetting('program.background.enabled'))
            ADDON_CORE.setSetting('program.background.image.source', ADDON.getSetting('program.background.image.source'))
            ADDON_CORE.setSetting('program.background.color', ADDON.getSetting('program.background.color'))
            ADDON_CORE.setSetting('program.background.flat', ADDON.getSetting('program.background.flat'))
            ADDON_CORE.setSetting('timebar.color', ADDON.getSetting('timebar.color'))
            ADDON_CORE.setSetting('categories.background.color', ADDON.getSetting('categories.background.color'))
            # Lab1
            ADDON_CORE.setSetting('cat.order', ADDON.getSetting('cat.order'))
            # Lab2
            '''
            ADDON_CORE.setSetting('yo.countries', 'canada,uk,us')
            ADDON_CORE.setSetting('yo.canada.headend', '325363')
            ADDON_CORE.setSetting('yo.us.headend', '318990-320445')
            ADDON_CORE.setSetting('yo.uk.headend', '114')
            ADDON_CORE.setSetting('tvguide.co.uk.days', '7')
            ADDON_CORE.setSetting('tvguide.co.uk.systemid', 'Virgin XL')
            '''
            dialog.ok('Done', 'Using "' + SKINS[skin][1] + '"')
        if not ADDON_CORE: dialog.ok('Error', 'Cannot set "' + SKINS[skin][1] + '"')
        if dialog.yesno('Built-in?', 'Do you want to refresh addons.ini?', 'These are built-in common channels.'):refresh_ini()
        





#################################################
# open an xml gui
#################################################
def _openguixml(thisxml):
    class cGUI(xbmcgui.WindowXML):
        def __init__(self, *args, **kwargs):
            #xbmcgui.WindowXML.__init__(self, *args, **kwargs)
            #self.strActionInfo = xbmcgui.ControlLabel(50, 50, 200, 200, '', 'font13', '0xFFBBBBFF')
            #self.addControl(self.strActionInfo)
            #self.strActionInfo.setLabel('Push BACK to quit')
            #self.listing = kwargs.get("listing")
            #kwargs.get("id")
            self.main_id = 1100
            self.main_control_id = 90000
            
        def onClick(self, controlID):
            # Set some variables because aaaawsome
            # the settings are available in vods like script-tvguide-vod-tv.xml and script-tvguide-main.xml  script-tvguide-menu.xml  script-tvguide-streamsetup.xml
            #
            xbmcgui.Window(self.main_id).setProperty('main_addon', ADDONID_CORE)
            #xbmcgui.Window(self.main_id).setProperty('main_addon_usersettings', 'special://home/userdata/addon_data/'+ADDONID_CORE+'/')
            xbmcgui.Window(self.main_id).setProperty('main_addon_usersettings', xbmc.translatePath(os.path.join('special://home', 'userdata', 'addon_data', ADDONID_CORE)))
            xbmcgui.Window(self.main_id).setProperty('skin_addon', ADDONID)
            xbmcgui.Window(self.main_id).setProperty('run_script', xbmc.translatePath(os.path.join(addonPath_core, 'skin.py')))
            #xbmcgui.Window(self.main_id).setProperty('run_script', addonPath_core)
            #xbmcgui.Window(self.main_id).setProperty('run_script', xbmc.translatePath(os.path.join(addonPath_core, 'resources', 'lib')))
            #
            # Background color
            #<setting id="program.background.color" label="Background EPG Colour" visible="eq(-4,0)" type="select"  default="[COLOR ff4682b4]steelblue[/COLOR]" />
            background_color = ADDON_CORE.getSetting('program.background.color')
            xbmcgui.Window(self.main_id).setProperty('background_color', background_color)
            #xbmcgui.Window(self.main_id).setProperty('background_color', 'steelblue')
            #
            # Cat color
            #<setting id="categories.background.color" label="Categories Background Colour" type="select"  default="[COLOR ff4682b4]steelblue[/COLOR]" />
            cat_color = ADDON_CORE.getSetting('categories.background.color')
            xbmcgui.Window(self.main_id).setProperty('cat_color', cat_color)
            #xbmcgui.Window(self.main_id).setProperty('cat_color', 'firebrick')
            #
            # EPG Window description color same as background but will appear darker
            xbmcgui.Window(self.main_id).setProperty('description_color', background_color)
            xbmcgui.Window(self.main_id).setProperty('description_info_color', 'skyblue')
            # button colors
            xbmcgui.Window(self.main_id).setProperty('focus_color', 'firebrick')
            xbmcgui.Window(self.main_id).setProperty('focus_current_color', 'green')
            xbmcgui.Window(self.main_id).setProperty('radio_color', 'deepskyblue')
            # scrollbar colors
            xbmcgui.Window(self.main_id).setProperty('scrollbarbg_color', 'black')
            xbmcgui.Window(self.main_id).setProperty('scrollbarnf_color', 'black')
            # slider colors
            xbmcgui.Window(self.main_id).setProperty('progress_color', 'darkcyan')
            xbmcgui.Window(self.main_id).setProperty('progressbg_color', 'grey')
            xbmcgui.Window(self.main_id).setProperty('progresscache_color', 'darkgrey')
            
            '''
            # EPG Window description color same as background but will appear darker
            xbmcgui.Window(self.main_id).setProperty('description_color', background_color)
            
            xbmcgui.Window(self.main_id).setProperty('description_info_color', ADDON_CORE.getSetting('description_info_color'))
            # button colors
            xbmcgui.Window(self.main_id).setProperty('focus_color', ADDON_CORE.getSetting('focus_color'))
            xbmcgui.Window(self.main_id).setProperty('focus_current_color', ADDON_CORE.getSetting('focus_current_color'))
            xbmcgui.Window(self.main_id).setProperty('radio_color', ADDON_CORE.getSetting('radio_color'))
            # scrollbar colors
            xbmcgui.Window(self.main_id).setProperty('scrollbarbg_color', ADDON_CORE.getSetting('scrollbarbg_color'))
            xbmcgui.Window(self.main_id).setProperty('scrollbarnf_color', ADDON_CORE.getSetting('scrollbarnf_color'))
            # slider colors
            xbmcgui.Window(self.main_id).setProperty('progress_color', ADDON_CORE.getSetting('progress_color'))
            xbmcgui.Window(self.main_id).setProperty('progressbg_color', ADDON_CORE.getSetting('progressbg_color'))
            xbmcgui.Window(self.main_id).setProperty('progresscache_color', ADDON_CORE.getSetting('progresscache_color'))
            '''

            if controlID == self.main_control_id:
                self.gui_button_SelectedPosition = self.gui_button.getSelectedPosition()
                self.setFocus(controlID)
        
        def setFocusId(self, id=90000):  pass
        
    ui = cGUI(thisxml, addonPath, skin_user)
    ui.doModal()
    del ui
#



def refresh_ini():
    xbmcgui.Dialog().notification('Creating ini files', 'Just a moment...', ICON, 5000, False)
    _WriteText(xbmc.translatePath(os.path.join(extrapath, 'playlists', 'Radio.m3u')), xbmc.translatePath(os.path.join('special://home','userdata','playlists','music', 'Radio.m3u')))
    #_failsafes_copy(xbmc.translatePath(os.path.join(addonPath,'resources','data', 'catchup.ini')), xbmc.translatePath(os.path.join(basePath,'catchup.ini')))
    _failsafes_copy(xbmc.translatePath(os.path.join(extrapath, 'addons.ini')), xbmc.translatePath(os.path.join(basePath,'addons.ini')))
    _failsafes_copy(xbmc.translatePath(os.path.join(extrapath, 'categories.ini')), xbmc.translatePath(os.path.join(basePath,'categories.ini')))
    _failsafes_copy(xbmc.translatePath(os.path.join(extrapath, 'mapping.ini')), xbmc.translatePath(os.path.join(basePath,'mapping.ini')))
    _failsafes_copy(xbmc.translatePath(os.path.join(extrapath, 'subscriptions.ini')), xbmc.translatePath(os.path.join(basePath,'subscriptions.ini')))
    _failsafes_copy(xbmc.translatePath(os.path.join(extrapath, 'folders.list')), xbmc.translatePath(os.path.join(basePath,'folders.list')))
    _sub_pass('plugin.video.iptvsubs')
    try: import sub
    except ImportError: pass
    else: sub.sub_run()
    '''
    try: import sub2;sub2.sub_run()
    except ImportError: pass
    try: import sub3;sub3.sub_run()
    except ImportError: pass
    try: import sub4;sub4.sub_run()
    except ImportError: pass
    try: import sub5;sub5.sub_run()
    except ImportError: pass
    try: import sub6;sub6.sub_run()
    except ImportError: pass
    '''
    _WriteText(xbmc.translatePath(os.path.join(basePath, 'addons.ini')), xbmc.translatePath(os.path.join(basePath_core,'addons2.ini')))
    _WriteText(xbmc.translatePath(os.path.join(basePath, 'categories.ini')), xbmc.translatePath(os.path.join(basePath_core,'categories.ini')))
    _WriteText(xbmc.translatePath(os.path.join(basePath, 'mapping.ini')), xbmc.translatePath(os.path.join(basePath_core,'mapping.ini')))
    _WriteText(xbmc.translatePath(os.path.join(basePath, 'subscriptions.ini')), xbmc.translatePath(os.path.join(basePath_core,'subscriptions.ini')))
    _failsafes_copy(xbmc.translatePath(os.path.join(basePath, 'folders.list')), xbmc.translatePath(os.path.join(basePath_core,'folders.list')))
    #xbmc.executebuiltin('RunScript(special://home/addons/'+ADDONID_CORE+'/ReloadAddonFolders.py)')
    _ReloadAddonFolders()
#





# trickery if needed for ease
def _ReloadAddonFolders():
    xbmc.log(msg='##['+ADDONID+'] Recreating subs', level=xbmc.LOGNOTICE)
    file_name = 'special://profile/addon_data/'+ADDONID_CORE+'/folders.list'
    f = xbmcvfs.File(file_name)
    items = f.read().splitlines()
    f.close()
    unique = set(items)

    file_name = 'special://profile/addon_data/'+ADDONID_CORE+'/addons.ini'
    if int(ADDON_CORE.getSetting('addons.ini.type')) == 1:
        customFile = str(ADDON_CORE.getSetting('addons.ini.file'))
        if os.path.exists(customFile) and os.access(customFile,os.W_OK):
            file_name = customFile

    plugins = {}
    logos = {}
    for path in unique:
        if path.startswith('@'):
            method = 1
            path = path[1:]
        else:
            method = 0
        # this skips non present addons
        match = re.match(r"plugin://(.*?)/",path)
        if match:
            plugin = match.group(1)
            try: id = xbmcaddon.Addon(plugin).getAddonInfo('id')
            except: continue
        try:
            response = RPC.files.get_directory(media="files", directory=path, properties=["thumbnail"])
        except:
            continue
        files = response.get("files")
        if not files:
            continue
        dirs = dict([[f["label"], f["file"]] for f in files if f["filetype"] == "directory"])
        links = dict([[f["label"], f["file"]] for f in files if f["filetype"] == "file"])
        thumbnails = dict([[f["file"], f["thumbnail"]] for f in files if f["filetype"] == "file"])
        match = re.match(r"plugin://(.*?)/",path)
        if match:
            plugin = match.group(1)
            xbmcgui.Dialog().notification('Creating ini', plugin, os.path.join('special://home/addons', plugin, 'icon.png'), 9000, False)
        else:
            continue
        if plugin not in plugins:
            plugins[plugin] = {}
        if plugin not in logos:
            logos[plugin] = {}

        streams = plugins[plugin]
        for label in links:
            file = links[label]
            if method == 1:
                streams[label] = "@"+file
            else:
                streams[label] = file
        thumbs = logos[plugin]
        for file in thumbnails:
            thumb = thumbnails[file]
            thumbs[file] = thumb

    f = xbmcvfs.File(file_name,'wb')
    write_str = "# WARNING Make a copy of this file.\n# It will be overwritten on the next folder add.\n\n"
    f.write(write_str.encode("utf8"))

    for addonId in sorted(plugins):
        write_str = "[%s]\n" % (addonId)
        #f.write(write_str)
        f.write(write_str.encode("utf8"))
        addonStreams = plugins[addonId]
        for name in sorted(addonStreams):
            stream = addonStreams[name]
            if name.startswith(' '):
                continue
            name = re.sub(r'[,:=]',' ',name)
            name = re.sub(r'\[.*?\]','',name)    # removes everything in []
            
            name = name.replace(' W HD',' WEST')
            #name = name.replace(' HD','')
            #name = re.sub("ACSTREAM - .+",'ACSTREAM ',name)
            name = name.replace('ACESTREAM - ','ACESTREAM ')
            #name = re.sub(" - .+",'',name)  # if there is epg listing in title remove them
            #for rep in [r"\[/?[BI]\]", r"\[/?COLOR.*?\]",]: # removes bold and colour
            #    name = re.sub(rep, '', name)
            #name = re.sub('\(.*?\)', '', name)   # removes everything in ()
            #name = re.sub('[^A-Za-z0-9]+', ' ', name) # removes all charachters and replaces with a space
            #name = re.sub('[^A-Za-z0-9!&()@ ]+', '', name) # removes all characters not mentioned and replaces with nothing
            name = re.sub("\xa9", "", name) #copywrite
            name = re.sub("\xae", "", name) #registered
            name = re.sub("\xc2", "", name) #
            name = re.sub("\xa0", "", name) #
            name = name.encode('ascii', 'ignore')
            name = name.lstrip(' ')
            #name = name.lstrip()
            name = name.strip()
            name = name.translate(string.whitespace)
            #name = re.sub(r"\s+", "", name, flags=re.UNICODE)
            name = name.upper()

            ######## Clean Chan Name #######
            for rep in [r"\[/?[BI]\]", r"\[/?COLOR.*?\]",]: # removes bold and colour
                #name = re.sub(rep, '', name)
                name = re.sub(rep, '', name)
            # 3
            name = name.replace('UK   ','')
            name = name.replace('USA   ','')
            name = name.replace('US   ','')
            name = name.replace('CA   ','')
            name = name.replace('UK:   ','')
            name = name.replace('USA:   ','')
            name = name.replace('US:   ','')
            name = name.replace('CA:   ','')
            #2
            name = name.replace('UK  ','')
            name = name.replace('USA  ','')
            name = name.replace('US  ','')
            name = name.replace('CA  ','')
            name = name.replace('UK:  ','')
            name = name.replace('USA:  ','')
            name = name.replace('US:  ','')
            name = name.replace('CA:  ','')
            #1
            '''
            name = name.replace('UK ','')
            #name = name.replace('USA ','')
            name = name.replace('US ','')
            name = name.replace('CA ','')
            name = name.replace('UK: ','')
            name = name.replace('USA: ','')
            name = name.replace('US: ','')
            name = name.replace('CA: ','')
            '''
            #
            # try to trim Sky tags
            name = name.replace('UKSKYMOVIES','SKY ')
            name = name.replace('UKSKY','SKY ')
            name = name.replace("UUK SKY", 'SKY ')
            name = name.replace("USKY", 'SKY ')
            name = name.replace('SKYSKY','SKY')
            name = name.replace('SKYSPORT','SKY SPORTS')
            name = name.replace("SKYSPORTS", 'SKY SPORTS')
            name = name.replace('SKY SPORT ','SKY SPORTS ')
            name = name.replace("SKYMOVIES", 'SKY')
            name = name.replace('SKY MOVIES','SKY')
            name = name.replace('SKY CINEMA','SKY')
            #
            # dumb strings
            name = name.replace(' W HD',' WEST')
            name = name.replace(' East HD',' HD')
            name = name.replace(' East','')
            name = name.replace(' EAST','')
            name = name.replace('ONLINE ','')
            #name = name.replace(' HD','')
            name = name.replace(' PRO SERVER ONLINE',' PRO SERVER ONLINE')
            # this is to eliminate ctv and lfctv comparisons
            name = name.replace('LFC TV','LFC')
            name = name.replace('LFCTV','LFC')
            #
            # this is to eliminate city tv and vague comparisons
            name = name.replace('CITY TV','City')
            name = name.replace('CITYTV','City')
            #
            # north america networks
            name = name.replace(' Vancover',' VANCOUVER')
            name = name.replace(' TORONTO','')
            name = name.replace(' HAMILTON','')
            name = name.replace(' ISLAND','')
            name = name.replace('A E','A&E')
            name = name.replace('A & E','A&E')
            name = name.replace('A&amp;E','A&E')
            name = name.replace('CW11','CW')
            name = name.replace('THE CW NETWORK','CW')
            name = name.replace('NATIONAL GEOGRAPHIC CHANNEL','NATIONAL GEOGRAPHIC')
            name = name.replace('NAT GEO','NATIONAL GEOGRAPHIC')
            name = name.replace('SCI FI','SYFY')
            # uk networks
            name = name.replace('BBC1','BBC ONE')
            name = name.replace('BBC2','BBC TWO')
            name = name.replace('BBC3','BBC THREE')
            name = name.replace('BBC4','BBC FOUR')
            name = name.replace('ITV1','ITV 1')
            name = name.replace('ITV2','ITV 2')
            name = name.replace('ITV3','ITV 3')
            name = name.replace('ITV4','ITV 4')
            # movies
            name = name.replace('HBO EAST','HBO')
            # sports
            name = name.replace('SKY SPNEWSHQ','SKY SPORTS NEWS')
            name = name.replace('BOX NATION','BOXNATION')
            name = name.replace('FS 1','FOX SPORTS 1')
            name = name.replace('FS 2','FOX SPORTS 2')
            name = name.replace('ESPN 1','ESPN')
            name = name.replace('TSN SP ','TSN ')
            name = name.replace('TSN1','TSN 1')
            name = name.replace('TSN2','TSN 2')
            name = name.replace('TSN3','TSN 3')
            name = name.replace('TSN4','TSN 4')
            name = name.replace('SPORTS NET','SPORTSNET')
            name = name.replace('SPORT NET','SPORTSNET')
            name = name.replace("BT SPORTS ", 'BT SPORT ')
            name = name.replace("BTSPORT", 'BT SPORT')
            #
            name = name.replace('SKY SPORTS 1','SKY SPORTS MAIN EVENT')
            name = name.replace('SKY SPORTS 2','SKY SPORTS PREMIERE LEAGUE')
            name = name.replace('SKY SPORTS 3','SKY SPORTS FOOTBALL')
            name = name.replace('SKY SPORTS 4','SKY SPORTS CRICKET')
            name = name.replace('SKY SPORTS 5','SKY SPORTS GOLF')
            name = name.replace('SKY DRAMA & ROMANCE','SKY DRAMA')
            name = name.replace('SKY ACTION & ADVENTURE','SKY ACTION')
            name = name.replace('SKY CRIME & THRILLER','SKY THRILLER')
            #words = ['exceptions', 'are', 'useful']
            #for word in words:
                #print(word)
                
            # iptvsubs
            if 'plugin.video.iptvsubs' in stream:
                # Networks
                name = name.replace('HD WEST','WEST')
                name = name.replace('ABC WEST','ABC Seattle')
                name = name.replace('CBS WEST','CBS Seattle')
                name = name.replace('NBC WEST','NBC Seattle')
                name = name.replace('FOX WEST','FOX Seattle')
                name = name.replace('ABC HD','ABC Boston')
                name = name.replace('CBS HD','CBS Boston')
                name = name.replace('NBC HD','NBC Boston')
                name = name.replace('FOX HD','FOX Boston')
                name = name.replace('AMC HD','AMC')
                name = name.replace(' (CND)',' CA')
                #name = name.replace(' HD','')
                name = name.replace(' EAST','')
                name = name.replace('SKY MOVIES 4 MEN','MOVIES4MEN')
                name = name.replace('SKY MOVIES','SKY')
                name = name.replace('SKY ITV','ITV')
                name = name.replace("SKY BBC", 'BBC')
                # 12 4 2016
                name = name.replace('5STAR MAX','5STARMAX') 
                name = name.replace('ACTION MAX','ACTIONMAX') 
                #name = name.replace('ACTION=','SHOWCASE ACTION=')
                #name = name.replace('"ACTION"','"SHOWCASE ACTION"')
                name = name.replace('ALJAZEERA ENGLISH','AL JAZEERA') 
                #name = name.replace('CHEK VANCOUVER','CHEK VANCOUVER') 
                name = name.replace('CITY TV','City')
                name = name.replace('COMEDY NETWORK','COMEDY CENTRAL')
                #name = name.replace('CTV=','CTV TORONTO=')
                name = name.replace('CTV (MTL)','CTV MONTREAL')
                name = name.replace('CTV NEWS NETWORK','CTV NEWS')
                name = name.replace('CW11','CW')
                name = name.replace('ESPN NEWS','ESPNEWS')
                name = name.replace('ESPN U','ESPNU')
                name = name.replace('ENCORE WESTERN','ENCORE WESTERNS')
                #name = name.replace('FX (CND)','FX CANADA')
                #name = name.replace('GLOBAL=','GLOBAL TORONTO=') 
                #name = name.replace('"GLOBAL"','"GLOBAL TORONTO"')
                name = name.replace('GLOBAL (MTL)','GLOBAL MONTREAL')
                #name = name.replace('GLOBAL BC','GLOBAL VANCOUVER')
                #name = name.replace('ID=','INVESTIGATION DISCOVERY=')
                #name = name.replace('"ID"','"INVESTIGATION DISCOVERY"')
                name = name.replace('LIFE','LIFETIME')
                #name = name.replace('"LIFE"','"LIFETIME"')
                name = name.replace('LIFETIME MOVIES','LMN')
                name = name.replace('LIFETIMETIME MOVIES','LMN')
                name = name.replace('MOVIE TIME','MOVIETIME')
                #name = name.replace('NAT GEO','NATIONAL GEOGRAPHIC')
                #name = name.replace('NATIONAL GEOGRAPHIC WILD','NAT GEO WILD')
                #name = name.replace('"NAT GEO"','"NATIONAL GEOGRAPHIC"')
                name = name.replace('RT NEWS ENGLISH','RT NEWS')
                name = name.replace('SKY 3E','3E')
                name = name.replace('SKY E4','E4')
                name = name.replace('SKY FILM4','FILM4')
                name = name.replace('SKY 4SEVEN','4SEVEN')
                name = name.replace('SKY 5 STAR','5STAR')
                name = name.replace('SKY RTE','RTE')
                name = name.replace('SKY 12','SKY ONE')
                name = name.replace('SKY 1','SKY ONE')
                name = name.replace('SKY 2','SKY TWO')
                name = name.replace('SKY SYFY','SYFY UK')
                name = name.replace('SKY CHANNEL','CHANNEL')
                name = name.replace('SKY ALIBI','ALIBI')
                name = name.replace('SKY ANIMAL PLANET','ANIMAL PLANET UK')
                name = name.replace('SKY BET','BET UK')
                name = name.replace('SKY BOX OFFICE','PPV SKY BOX OFFICE')
                name = name.replace('SKY CARTOON NETWORK','CARTOON NETWORK UK')
                name = name.replace('SKY COMEDY CENTRAL 1','COMEDY CENTRAL +1 UK')
                name = name.replace('SKY COMEDY XTRA','COMEDY CENTRAL XTRA')
                name = name.replace('SKY COMEDY CENTRAL','COMEDY CENTRAL UK')
                name = name.replace('SKY CRIME & INVESTIGATION','CRIME & INVESTIGATION UK')
                name = name.replace('SKY DAVE','DAVE')
                name = name.replace('SKY DAYSTAR','DAYSTAR')
                name = name.replace('SKY DISCOVERY HISTORY','DISCOVERY HISTORY UK')
                name = name.replace('SKY DISCOVERY SCIENCE','DISCOVERY SCIENCE UK')
                name = name.replace('SKY DISCOVERY SHED','DISCOVERY SHED')
                name = name.replace('SKY DISCOVERY TURBO','DISCOVERY TURBO UK')
                name = name.replace('SKY DISCOVERY','DISCOVERY UK')
                name = name.replace('SKY DISNEY JR','DISNEY JR UK')
                name = name.replace('SKY DISNEY XD','DISNEY XD UK')
                name = name.replace('SKY DISNEY','DISNEY UK')
                name = name.replace('SKY DMAX','DMAX')
                name = name.replace('SKY EDEN','EDEN')
                name = name.replace('SKY EWTN','EWTN') 
                name = name.replace('SKY FOOD NETWORK','FOOD UK')
                name = name.replace('SKY FOX NEWS','FOX NEWS UK')
                name = name.replace('SKY FOX','FOX UK')
                name = name.replace('SKY GOOD FOOD','GOOD FOOD')
                name = name.replace('SKY HISTORY 1','HISTORY +1 UK')
                name = name.replace('SKY HISTORY 2','H2 UK')
                name = name.replace('SKY HISTORY','HISTORY UK')
                name = name.replace('SKY HOME','HOME')
                #name = name.replace('SKY HOME HEALTH','HOME HEALTH')
                name = name.replace('SKY INSPIRATION','INSPIRATION')
                name = name.replace('SKY INVESTIGATION DISCOVERY','INVESTIGATION DISCOVERY UK')
                name = name.replace('SKY MOTORS TV UK','MOTORS TV')
                #name = name.replace('SKY NAT GEO WILD','NAT GEO WILD UK')
                #name = name.replace('SKY NAT GEO','NATIONAL GEOGRAPHIC UK')
                name = name.replace('SKY NICK JR','NICK JR UK')
                name = name.replace('SKY NICK JR TOO','NICK JR TOO UK')
                name = name.replace('SKY NICKTOONS','NICKTOONS UK')
                name = name.replace('SKY NICK','NICKELODEON UK')
                name = name.replace('SKY QUEST','QUEST')
                name = name.replace('SKY REAL LIVES','REAL LIVES')
                name = name.replace('SKY RT NOW','RT NOW')
                name = name.replace('SKY SONY CHANNEL','SONY CHANNEL')
                name = name.replace('SKY SONY MOVIE','SONY MOVIE')
                name = name.replace('SKY TBN','TBN UK')
                name = name.replace('SKY TCM','TCM UK')
                name = name.replace('SKY TCM 1','TCM +1 UK')
                name = name.replace('SKY TLC','TLC UK')
                name = name.replace('SKY TLC IRELAND','TLC IRELAND')
                name = name.replace('SKY TRU TV','TRUTV UK')
                name = name.replace('TRU TV','TRUTV')
                name = name.replace('SKY UTV IRELAND','UTV IRELAND')
                name = name.replace('SKY V CHANNEL','V CHANNEL')  
                name = name.replace('SKY WATCH','WATCH')
                name = name.replace('STARZ BLACK','STARZ IN BLACK')
                name = name.replace('THRILLER MAX','THRILLERMAX')
                name = name.replace('TVO (NA)','TVO')
                name = name.replace('YTV (NA)','YTV')
                name = name.replace('BT SPORTS 1','BT SPORT 1')
                name = name.replace('BT SPORTS 2','BT SPORT 2')
                name = name.replace('EURO SPORT 1','EUROSPORT')
                name = name.replace('EURO SPORT 2','EUROSPORT 2')
                name = name.replace('FOX DEPORTES (ES)','FOOX DEPORTES (ES)')
                name = name.replace('NBC SPORTS','NBCSN')
                name = name.replace('NFL NETWORK','NFL')
                name = name.replace('NHL NETWORK','NHL')
                name = name.replace('SKY BOX NATION','BOX NATION')
                name = name.replace('SPORTSNET ONT','SPORTSNET ONTARIO')
                name = name.replace('BRAZZERS 1','BRAZZERS')
                name = name.replace('PLAYBOY TV','PLAYBOY')
                name = name.replace('VIVID TV','VIVID')
                name = name.replace('HISTORY=','HISTORY CANADA=')
                name = name.replace('NAT GEO','NATIONAL GEOGRAPHIC')
                name = name.replace('NATIONAL GEOGRAPHIC WILD','NAT GEO WILD')
                name = name.replace('SKY NAT GEO WILD','NAT GEO WILD UK')
                name = name.replace('SKY NATIONAL GEOGRAPHIC','NATIONAL GEOGRAPHIC UK')
                


            for replace in  [':','-','_',]:
                if len(name) > 3 and name.upper()[:1] is not 'BT' and name[2] == replace:
                    name = name.split(replace,1)[1]
            #name = name.strip()
            #name = re.sub('[^A-Za-z0-9!&()@ ]+', '', name) # removes all characters not mentioned and replaces with nothing
            #
            name = re.sub(" - .+",'',name) # if there is epg listing in title remove them 
            if not name: #TODO names in brackets
                continue
            if name.startswith(' '):
                continue
            if not stream:
                stream = 'nothing'
            '''
            if 'plugin.video.f4mTester' in stream: 
                stream = "@"+stream
            ''' 
            if 'turk' in stream:
                stream=urllib.unquote(stream).decode('utf8')
            #
            write_str = "%s=%s\n" % (name,stream)
            f.write(write_str.encode("utf8"))
    f.close()

    file_name = 'special://profile/addon_data/'+ADDONID_CORE+'/icons.ini'
    f = xbmcvfs.File(file_name,'wb')
    write_str = "# WARNING Make a copy of this file.\n# It will be overwritten on the next folder add.\n\n"
    f.write(write_str.encode("utf8"))
    for addonId in sorted(logos):
        write_str = "[%s]\n" % (addonId)
        #f.write(write_str)
        f.write(write_str.encode("utf8"))
        addonLogos = logos[addonId]
        for file in sorted(addonLogos):
            logo = addonLogos[file]
            if logo:
                write_str = "%s|%s\n" % (file,logo)
                f.write(write_str.encode("utf8"))
    f.close()
    dialog = xbmcgui.Dialog()
    dialog.notification("TV Guide Fullscreen","Done: Reload Subscription Folders",sound=False)
    _reopen()





# trickery if needed for ease
def _sub_pass(theaddon):
    if xbmc.getCondVisibility('System.HasAddon(%s)' % theaddon):
        try:
            theaddon_addon = xbmcaddon.Addon(theaddon)
            theaddon_username = theaddon_addon.getSetting('kasutajanimi')
            theaddon_password = theaddon_addon.getSetting('salasona')
            sublist = xbmc.translatePath(os.path.join(basePath,'folders.list'))
            _Replace_TXT('subsuser', theaddon_username, sublist,tmp_File)
            _Replace_TXT('subspass', theaddon_password, sublist,tmp_File)
        except:  pass
#
def _Replace_TXT(clean_this, with_this, Clean_Name,tmp_File):
    xbmc.log(msg='##['+ADDONID+'] Replace text '+clean_this, level=xbmc.LOGNOTICE)
    _delete_file(tmp_File)
    if os.path.exists(Clean_Name):
        try:
            os.rename(Clean_Name, tmp_File)
            s=open(tmp_File).read()
            s=s.replace(clean_this,with_this)
            f=open(Clean_Name,'w')
            f.write(s)
            f.close()
            s.close()
        except: pass
        _delete_file(tmp_File)
#
def _delete_file(filename):
    tries = 10
    while os.path.exists(filename) and tries > 0:
        try:
            os.remove(filename)
            break
        except:
            tries -= 1






################################################################################
#   MENU VOD
################################################################################
def vod_Menu():
    vod1 = ADDON.getSetting('vod1')
    vod2 = ADDON.getSetting('vod2')
    vod3 = ADDON.getSetting('vod3')
    vod4 = ADDON.getSetting('vod4')
    vod5 = ADDON.getSetting('vod5')
    vod6 = ADDON.getSetting('vod6')
    vod7 = ADDON.getSetting('vod7')
    vod8 = ADDON.getSetting('vod8')
    vod9 = ADDON.getSetting('vod9')
    choicevod = dialog.select('Choose VOD', ['[COLOR yellow]Default[/COLOR]',vod1,vod2,vod3,vod4,vod5,vod6,vod7,vod8,vod9])
    if choicevod == 0: _openguixml('script-tvguide-vod-tv.xml')
    if choicevod == 1: _openguixml('script-tvguide-vod-'+vod1+'.xml')
    if choicevod == 2: _openguixml('script-tvguide-vod-'+vod2+'.xml')
    if choicevod == 3: _openguixml('script-tvguide-vod-'+vod3+'.xml')
    if choicevod == 4: _openguixml('script-tvguide-vod-'+vod4+'.xml')
    if choicevod == 5: _openguixml('script-tvguide-vod-'+vod5+'.xml')
    if choicevod == 6: _openguixml('script-tvguide-vod-'+vod6+'.xml')
    if choicevod == 7: _openguixml('script-tvguide-vod-'+vod7+'.xml')
    if choicevod == 8: _openguixml('script-tvguide-vod-'+vod8+'.xml')
    if choicevod == 9: _openguixml('script-tvguide-vod-'+vod9+'.xml')
#

################################################################################
#  MENU Help
# help text not including built in by primevil
# by default there is changelog, commands and playwith instructions
################################################################################
def help_Menu():
    choicehelp = dialog.select('Choose help inquery', ['[COLOR yellow]Close[/COLOR]',
                               'Keyboard and Remote Commands',
                               'Changelog',
                               'Playwith (send video to another device)',
                               help1,help2,help3,help4,help5,help6,help7,help8,help9,help10,help11,help12,help13,help14,help15,help16,help17,help18,help19,help20,help21,help22])
    if choicehelp == 0: sys.exit(0)
    if choicehelp == 1: help_run_special(xbmc.translatePath('special://home/addons/'+ADDONID_CORE+'/commands.txt'))
    if choicehelp == 2: help_run_special(xbmc.translatePath('special://home/addons/'+ADDONID_CORE+'/changelog.txt'))
    if choicehelp == 3: help_run_special(xbmc.translatePath('special://home/addons/'+ADDONID_CORE+'/resources/playwith/readme.txt'))
    if choicehelp == 4: help_run(help1)
    if choicehelp == 5: help_run(help2)
    if choicehelp == 6: help_run(help3)
    if choicehelp == 7: help_run(help4)
    if choicehelp == 8: help_run(help5)
    if choicehelp == 9: help_run(help6)
    if choicehelp == 10: help_run(help7)
    if choicehelp == 11: help_run(help8)
    if choicehelp == 12: help_run(help9)
    if choicehelp == 13: help_run(help10)
    if choicehelp == 14: help_run(help11)
    if choicehelp == 15: help_run(help12)
    if choicehelp == 16: help_run(help13)
    if choicehelp == 17: help_run(help14)
    if choicehelp == 18: help_run(help15)
    if choicehelp == 19: help_run(help16)
    if choicehelp == 20: help_run(help17)
    if choicehelp == 21: help_run(help18)
    if choicehelp == 22: help_run(help19)
    if choicehelp == 23: help_run(help20)
    if choicehelp == 24: help_run(help21)
    if choicehelp == 25: help_run(help22)
#
def help_run(help_file):
    path = xbmc.translatePath('special://home/addons/'+ADDONID+'/resources/help/'+help_file+'.txt')
    if not os.path.exists(path): return
    f = xbmcvfs.File(path,'rb')
    data = f.read()
    dialog = xbmcgui.Dialog()
    dialog.textviewer('Help', data)
#
def help_run_special(path):
    if not os.path.exists(path): return
    f = xbmcvfs.File(path,'rb')
    data = f.read()
    dialog = xbmcgui.Dialog()
    dialog.textviewer('Help', data)
#


################################################################################
#   MENU Delete Database
################################################################################
def deletedatabase_Menu():
    # check source.db
    DB_SET = dbPath = xbmc.translatePath(os.path.join(basePath, deletedatabasedb))
    if os.path.isfile(DB_SET):DB_SET_EN_DIS =  " [COLOR yellowgreen]source.db[/COLOR]"
    else:DB_SET_EN_DIS = " [COLOR red]source.db[/COLOR]"
    choicedeletedatabase = dialog.select('TV Guide Database '+DB_SET_EN_DIS, ['[COLOR yellow]Close[/COLOR]',
                                                    'Delete ALL TV Guide files (Start fresh)', 
                                                    'Delete xmltv.xml (redownload guide)',
                                                    'Delete a database file'])
    if choicedeletedatabase == 0: sys.exit(0)
    if choicedeletedatabase == 1: deleteDB_all();ADDON_CORE.setSetting('run.deldb', 'true')
    if choicedeletedatabase == 2: delete_file(deletedatabase0);delete_file('xmltv.xml.tmp');_reopen()
    if choicedeletedatabase == 3: deletedatabase_file_menu()
#
def deletedatabase_file_menu():
    choicedeletedatabase_file = dialog.select('Choose TV Guide Database file to delete', ['Delete ALL TV Guide files (Start fresh)',deletedatabasedb,deletedatabase0,
                                              deletedatabase1,deletedatabase2,deletedatabase3,deletedatabase4,deletedatabase5,
                                              deletedatabase6,deletedatabase7,deletedatabase8,deletedatabase9,deletedatabase10,
                                              deletedatabase11,deletedatabase12,deletedatabase13,deletedatabase14,deletedatabase15,
                                              deletedatabase16,deletedatabase17,deletedatabase18,deletedatabase19])
    if choicedeletedatabase_file == 0: deleteDB_all()
    if choicedeletedatabase_file == 1: delete_file(deletedatabasedb)
    if choicedeletedatabase_file == 2: delete_file(deletedatabase0)
    if choicedeletedatabase_file == 3: delete_file(deletedatabase1)
    if choicedeletedatabase_file == 4: delete_file(deletedatabase2)
    if choicedeletedatabase_file == 5: delete_file(deletedatabase3)
    if choicedeletedatabase_file == 6: delete_file(deletedatabase4)
    if choicedeletedatabase_file == 7: delete_file(deletedatabase5) 
    if choicedeletedatabase_file == 8: delete_file(deletedatabase6)
    if choicedeletedatabase_file == 9: delete_file(deletedatabase7)
    if choicedeletedatabase_file == 10: delete_file(deletedatabase8)
    if choicedeletedatabase_file == 11: delete_file(deletedatabase9)
    if choicedeletedatabase_file == 12: delete_file(deletedatabase10)
    if choicedeletedatabase_file == 13: delete_file(deletedatabase11)
    if choicedeletedatabase_file == 14: delete_file(deletedatabase12)
    if choicedeletedatabase_file == 15: delete_file(deletedatabase13)
    if choicedeletedatabase_file == 16: delete_file(deletedatabase14)
    if choicedeletedatabase_file == 17: delete_file(deletedatabase15)
    if choicedeletedatabase_file == 18: delete_file(deletedatabase16)
    if choicedeletedatabase_file == 19: delete_file(deletedatabase17)
    if choicedeletedatabase_file == 20: delete_file(deletedatabase18)
    if choicedeletedatabase_file == 21: delete_file(deletedatabase19)
#
def deleteDB_all():
    path = xbmc.translatePath('special://profile/addon_data/'+ADDONID_CORE)
    if os.path.exists(path):
        for f in os.listdir(path):
            fpath = os.path.join(path, f)
            try:
                if os.path.isfile(fpath):
                    if not fpath.lower().endswith('.xml'):
                        os.unlink(fpath)
                elif os.path.isdir(fpath):
                    shutil.rmtree(fpath)
            except Exception as e:
                print e
    else:
        print path
    #
    xbmcvfs.delete(xbmc.translatePath(os.path.join('special://profile', 'addon_data', ADDONID_CORE, deletedatabasedb)))
    xbmcvfs.delete(xbmc.translatePath(os.path.join('special://profile', 'addon_data', ADDONID_CORE, deletedatabase0)))
    xbmcvfs.delete(xbmc.translatePath(os.path.join('special://profile', 'addon_data', ADDONID_CORE, deletedatabase1)))
    xbmcvfs.delete(xbmc.translatePath(os.path.join('special://profile', 'addon_data', ADDONID_CORE, deletedatabase2)))
    xbmcvfs.delete(xbmc.translatePath(os.path.join('special://profile', 'addon_data', ADDONID_CORE, deletedatabase3)))
    
    settingsfile = xbmc.translatePath(os.path.join('special://profile', 'addon_data', ADDONID_CORE, 'settings.xml'))
    if dialog.yesno('Delete settings?', 'Do you want to delete settings.xml?', 'This will reset all settings to default'):
        xbmcvfs.delete('special://profile/addon_data/'+ADDONID_CORE+'/settings.xml')
    ADDON_CORE.setSetting('firstrun', 'true')
    #
    dbfile = xbmc.translatePath(os.path.join('special://profile', 'addon_data', ADDONID_CORE, deletedatabasedb))    
    if os.path.exists(dbfile): dialog.ok('TV Guide', 'Failed to delete source.db', 'Database may be locked,', 'Will try on next start');ADDON_CORE.setSetting('run.deldb', 'true')
    if not os.path.exists(dbfile): dialog.ok('TV Guide', 'source.db has been successfully deleted.', 'It will start fresh next time you start the guide')
    #
    xbmc.executebuiltin('XBMC.ActivateWindow(shutdownmenu)')
#
def delete_file(file):
    filepath      = xbmc.translatePath(os.path.join('special://profile', 'addon_data', ADDONID_CORE, file))
    xbmcvfs.delete(filepath)
    if os.path.exists(filepath): dialog.ok('TV Guide', 'Failed to delete '+filepath, 'File may be locked,', 'please restart and try again')
    if not os.path.exists(filepath): dialog.ok('TV Guide', filepath+' has been successfully deleted.', 'It will start fresh next time you start the guide')
#


#################################################
# Flip skin reverse description and videowindow co-ordinates
#################################################
def _skinvideowindow_toggle(Clean_File, rezsize):
     Clean_Name = xbmc.translatePath(os.path.join(skinPath, rezsize, Clean_File))
     if not os.path.exists(Clean_Name): return
     tmpFile = xbmc.translatePath(os.path.join(tmp_path,'tmp.xml'))
     if os.path.exists(tmpFile): os.remove(tmpFile)
     xbmc.log(msg='##['+ADDONID+'] '+Clean_Name, level=xbmc.LOGNOTICE)
     try:    os.rename(Clean_Name, tmpFile)
     except: pass
     s=open(tmpFile).read()
     if rezsize == '720p':
         ## Description Flip
         # flip3 720p main
         if '<posx>20.5</posx>' in s:  s=s.replace('<posx>20.5</posx>','<posx>360.5</posx>')
         else:  s=s.replace('<posx>360.5</posx>','<posx>20.5</posx>')# extra 30 for timebar at top
         # flip4 720p menu
         if '<posx>920.5</posx>' in s:  s=s.replace('<posx>920.5</posx>','<posx>-360.5</posx>')
         else:  s=s.replace('<posx>-360.5</posx>','<posx>920.5</posx>')# extra 30 for timebar at top
     #
     if rezsize == '1080i':
         ## Description Flip
         # flip3 1080p main
         if '<posx>31</posx>' in s:  s=s.replace('<posx>31</posx>','<posx>541</posx>')
         else:  s=s.replace('<posx>541</posx>','<posx>31</posx>')# extra 30 for timebar at top
         # flip4 1080p menu
         if '<posx>1381</posx>' in s:  s=s.replace('<posx>1381</posx>','<posx>-541</posx>')
         else:  s=s.replace('<posx>-541</posx>','<posx>1381</posx>')# extra 30 for timebar at top
     #
     f=open(Clean_Name,'a')
     f.write(s)
     f.close()
     if os.path.exists(tmpFile): os.remove(tmpFile)
#


#################################################
# Flip skin description co-ordinates
#################################################
def _skinflip_toggle(Clean_File, rezsize):
     Clean_Name = xbmc.translatePath(os.path.join(skinPath, rezsize, Clean_File))
     if not os.path.exists(Clean_Name): return
     tmpFile = xbmc.translatePath(os.path.join(tmp_path,'tmp.xml'))
     if os.path.exists(tmpFile): os.remove(tmpFile)
     xbmc.log(msg='##['+ADDONID+'] '+Clean_Name, level=xbmc.LOGNOTICE)
     try:    os.rename(Clean_Name, tmpFile)
     except: pass
     s=open(tmpFile).read()
     if rezsize == '720p':
         ## Description Flip
         # flip1 720p main
         if '<posy>240.5</posy>' in s:  s=s.replace('<posy>240.5</posy>','<posy>30.5</posy>')
         else:  s=s.replace('<posy>30.5</posy>','<posy>240.5</posy>')# extra 30 for timebar at top
         # flip2 720p menu
         if '<posy>0.5</posy>' in s:  s=s.replace('<posy>0.5</posy>','<posy>475.5</posy>')
         else:  s=s.replace('<posy>475.5</posy>','<posy>0.5</posy>')# extra 30 for timebar at top
         # flip5 720p menu
         #if '<posy>210.5</posy>' in s:  s=s.replace('<posy>210.5</posy>','<posy>1.5</posy>')
         #else:  s=s.replace('<posy>1.5</posy>','<posy>210.5</posy>')# extra 30 for timebar at top
     #
     if rezsize == '1080i':
         ## Description Flip
         # flip1 1080p main
         if '<posy>361</posy>' in s:  s=s.replace('<posy>361</posy>','<posy>46</posy>')
         else:  s=s.replace('<posy>46</posy>','<posy>361</posy>')
         # flip2 1080p menu
         if '<posy>1</posy>' in s:  s=s.replace('<posy>1</posy>','<posy>713</posy>')
         else:  s=s.replace('<posy>713</posy>','<posy>1</posy>')
         # flip5 1080p menu
         #if '<posy>361</posy>' in s:  s=s.replace('<posy>361</posy>','<posy>46</posy>')
         #else:  s=s.replace('<posy>46</posy>','<posy>361</posy>')
     #
     f=open(Clean_Name,'a')
     f.write(s)
     f.close()
     if os.path.exists(tmpFile): os.remove(tmpFile)
#


################################################# 
# Toggle 1080i #
#################################################
def _toggle_1080():
    disabled_1080 = xbmc.translatePath(os.path.join(skinPath, '1080i-'))
    enabled_1080  = xbmc.translatePath(os.path.join(skinPath, '1080i'))
    xbmc.executebuiltin('XBMC.ActivateWindow(home)')
    xbmc.sleep(350)
    if os.path.exists(xbmc.translatePath(os.path.join(enabled_1080, flipmenu))):
        xbmcgui.Dialog().notification('Toggle', 'Disable 1080', ICON, 1000, False)
        os.rename(enabled_1080, disabled_1080)
    else:
        xbmcgui.Dialog().notification('Toggle', 'Enable 1080', ICON, 1000, False)
        os.rename(disabled_1080, enabled_1080)
#


#################################################
# Gif to png toggle
#################################################
def _skingif_toggle(Clean_File, rezsize):
     Clean_Name = xbmc.translatePath(os.path.join(skinPath, rezsize, Clean_File))
     if not os.path.exists(Clean_Name): return
     tmpFile = xbmc.translatePath(os.path.join(tmp_path,'tmp.xml'))
     if os.path.exists(tmpFile): os.remove(tmpFile)
     xbmc.log(msg='##['+ADDONID+'] '+Clean_Name, level=xbmc.LOGNOTICE)
     try:    os.rename(Clean_Name, tmpFile)
     except: pass
     s=open(tmpFile).read()
     if rezsize == '720p':
         if 'background.gif' in s:  s=s.replace('background.gif','background.png')
         else:  s=s.replace('background.png','background.gif')# extra 30 for timebar at top
     #
     if rezsize == '1080i':
         if 'background.gif' in s:  s=s.replace('background.gif','background.png')
         else:  s=s.replace('background.png','background.gif')
     f=open(Clean_Name,'a')
     f.write(s)
     f.close()
     if os.path.exists(tmpFile): os.remove(tmpFile)
#
################################################# 
# Re-open guide
#################################################
def _reopen():
    #'''
    xbmc.executebuiltin('XBMC.ActivateWindow(home)')
    xbmc.sleep(500)
    #RUN = 'RunAddon('+ADDONID+')'
    #RUN = 'RunScript('+ADDONID_CORE+')'
    #xbmc.executebuiltin(RUN)
    xbmc.executebuiltin('XBMC.RunScript('+ addonPath_core + '/addon.py)')
    #sys.exit()
    '''
    import gui
    xbmc.executebuiltin('XBMC.ActivateWindow(home)')
    xbmc.sleep(350)
    w = gui.TVGuide()
    w.doModal()
    xbmc.sleep(350)
    del w
    '''
#
#################################################
# logos toggle
#################################################
def _logos_toggle():
    if ADDON_CORE.getSetting('logos.enabled') == 'false':
        ADDON_CORE.setSetting('logos.enabled', 'true')
    elif ADDON_CORE.getSetting('logos.enabled') == 'true':
        ADDON_CORE.setSetting('logos.enabled', 'false')
    _reopen()
    #xbmc.executebuiltin('XBMC.ReloadSkin()')
    #xbmc.executebuiltin('XBMC.Action(reloadkeymaps)')
#
#################################################
# pip toggle
#################################################
def _pip_toggle():
    if ADDON_CORE.getSetting('epg.video.pip') == 'false':
        ADDON_CORE.setSetting('epg.video.pip', 'true')
    elif ADDON_CORE.getSetting('epg.video.pip') == 'true':
        ADDON_CORE.setSetting('epg.video.pip', 'false')
    _reopen()
#
#################################################
# toggle List View for Choose Stream
#################################################
def _ChooseStream_toggle():
    if ADDON_CORE.getSetting('stream.addon.list') == 'false':
        ADDON_CORE.setSetting('stream.addon.list', 'true')
    elif ADDON_CORE.getSetting('stream.addon.list') == 'true':
        ADDON_CORE.setSetting('stream.addon.list', 'false')
    _reopen()
#
#################################################
# colums toggle
#################################################
def _colums_toggle_run(colums):
    ADDON_CORE.setSetting('channels.per.page', colums)
    _reopen()
#
def _colums_toggle():
    choicecolum = dialog.select('Choose number of PG rows', ['[COLOR yellow]Close[/COLOR]','12','16','15','14','13','11','10','9','8'])
    if choicecolum == 0: sys.exit(0)
    if choicecolum == 1: _colums_toggle_run('12')
    if choicecolum == 2: _colums_toggle_run('16')
    if choicecolum == 3: _colums_toggle_run('15')
    if choicecolum == 4: _colums_toggle_run('14')
    if choicecolum == 5: _colums_toggle_run('13')
    if choicecolum == 6: _colums_toggle_run('11')
    if choicecolum == 7: _colums_toggle_run('10')
    if choicecolum == 8: _colums_toggle_run('9')
    if choicecolum == 9: _colums_toggle_run('8')
#
#################################################
# Flip 16 to kodi 17 plus strings
#################################################
def _skinversion_toggle(Clean_File, rezsize):
     Clean_Name = xbmc.translatePath(os.path.join(skinPath, rezsize, Clean_File))
     if not os.path.exists(Clean_Name): return
     tmpFile = xbmc.translatePath(os.path.join(tmp_path,'tmp.xml'))
     if os.path.exists(tmpFile): os.remove(tmpFile)
     xbmc.log(msg='##['+ADDONID+'] '+Clean_Name, level=xbmc.LOGNOTICE)
     try:    os.rename(Clean_Name, tmpFile)
     except: pass
     s=open(tmpFile).read()
     # 16 StringCompare  to  17 String.IsEqual
     if 'String.IsEqual' in s:  s=s.replace('String.IsEqual','StringCompare')
     else:  s=s.replace('StringCompare','String.IsEqual')
     # 16 IntegerGreaterThan  to  17 Integer.IsGreater
     if 'Integer.IsGreater' in s:  s=s.replace('Integer.IsGreater','IntegerGreaterThan')
     else:  s=s.replace('IntegerGreaterThan','Integer.IsGreater')
     # 16 SubString  to  17  String.Contains
     if 'String.Contains' in s:  s=s.replace('String.Contains','SubString')
     else:  s=s.replace('SubString','String.Contains')
     #
     # special
     # 16 IsEmpty  to  17  String.IsEmpty
     if '!String.IsEmpty' in s:  s=s.replace('!String.IsEmpty','!IsEmpty')
     else:  s=s.replace('!IsEmpty','!String.IsEmpty')
     #
     # special
     # 16 IsEmpty  to  17  String.IsEmpty
     if '>String.IsEmpty' in s:  s=s.replace('>String.IsEmpty','>IsEmpty')
     else:  s=s.replace('>IsEmpty','>String.IsEmpty')
     #
     f=open(Clean_Name,'a')
     f.write(s)
     f.close()
     if os.path.exists(tmpFile): os.remove(tmpFile)
#
'''
     change these -
    IsEmpty()  to   String.IsEmpty()
    StringCompare() to  String.IsEqual()
    IntegerGreaterThan()  to  Integer.IsGreater()
    SubString()  to  String.Contains()
    
    
16 and less but work in 17
these infobools are now deprecated, though still functional, but will likely be removed in kodi v18:
    IsEmpty()
    StringCompare()
    SubString()
    IntegerGreaterThan()
    
    
17 +
new string / integer compare methods:
    Integer.IsEqual()
    Integer.IsGreater()
    Integer.IsGreaterOrEqual()
    Integer.IsLess()
    Integer.IsLessOrEqual()

    String.IsEmpty()
    String.IsEqual()
    String.StartsWith()
    String.EndsWith()
    String.Contains()
'''
     




#
################################################################################
#   toggle  color
################################################################################
def toggle_color(color__file, thesetting):
    #ADDON_CORE.setSetting('program.background.color', color__file)
    ADDON_CORE.setSetting(thesetting, color__file)
    _reopen()
#
################################################################################
#   toggle specific color
################################################################################
def menucolor__file_toggle(thissetting,menucolor_0,menucolor_1,menucolor_2,menucolor_3,menucolor_4,menucolor_5,menucolor_6,menucolor_7,menucolor_8,menucolor_9, menucolor_10,menucolor_11,menucolor_12,menucolor_13,menucolor_14,menucolor_15,menucolor_16,menucolor_17,menucolor_18,menucolor_19,menucolor_20,menucolor_21,menucolor_22,menucolor_23,menucolor_24,menucolor_25,menucolor_26,menucolor_27,menucolor_28,menucolor_29,menucolor_30):
    choicemenucolor__specfile = dialog.select('Choose Color for  '+thissetting, [menucolor_0,
                                     menucolor_1,menucolor_2,menucolor_3,menucolor_4,menucolor_5,menucolor_6,menucolor_7,menucolor_8,menucolor_9, menucolor_10,
                                     menucolor_11,menucolor_12,menucolor_13,menucolor_14,menucolor_15,menucolor_16,menucolor_17,menucolor_18,menucolor_19,menucolor_20,
                                     menucolor_21,menucolor_22,menucolor_23,menucolor_24,menucolor_25,menucolor_26,menucolor_27,menucolor_28,menucolor_29,menucolor_30])
    if choicemenucolor__specfile == 0: toggle_color(menucolor_0, thissetting)
    if choicemenucolor__specfile == 1: toggle_color(menucolor_1, thissetting)
    if choicemenucolor__specfile == 2: toggle_color(menucolor_2, thissetting)
    if choicemenucolor__specfile == 3: toggle_color(menucolor_3, thissetting)
    if choicemenucolor__specfile == 4: toggle_color(menucolor_4, thissetting)
    if choicemenucolor__specfile == 5: toggle_color(menucolor_5, thissetting)
    if choicemenucolor__specfile == 6: toggle_color(menucolor_6, thissetting)
    if choicemenucolor__specfile == 7: toggle_color(menucolor_7, thissetting)
    if choicemenucolor__specfile == 8: toggle_color(menucolor_8, thissetting)
    if choicemenucolor__specfile == 9: toggle_color(menucolor_9, thissetting)
    if choicemenucolor__specfile == 10: toggle_color(menucolor_10, thissetting)
    if choicemenucolor__specfile == 11: toggle_color(menucolor_11, thissetting)
    if choicemenucolor__specfile == 12: toggle_color(menucolor_12, thissetting)
    if choicemenucolor__specfile == 13: toggle_color(menucolor_13, thissetting)
    if choicemenucolor__specfile == 14: toggle_color(menucolor_14, thissetting)
    if choicemenucolor__specfile == 15: toggle_color(menucolor_15, thissetting)
    if choicemenucolor__specfile == 16: toggle_color(menucolor_16, thissetting)
    if choicemenucolor__specfile == 17: toggle_color(menucolor_17, thissetting)
    if choicemenucolor__specfile == 18: toggle_color(menucolor_18, thissetting)
    if choicemenucolor__specfile == 19: toggle_color(menucolor_19, thissetting)
    if choicemenucolor__specfile == 20: toggle_color(menucolor_20, thissetting)
    if choicemenucolor__specfile == 21: toggle_color(menucolor_21, thissetting)
    if choicemenucolor__specfile == 22: toggle_color(menucolor_22, thissetting)
    if choicemenucolor__specfile == 23: toggle_color(menucolor_23, thissetting)
    if choicemenucolor__specfile == 24: toggle_color(menucolor_24, thissetting)
    if choicemenucolor__specfile == 25: toggle_color(menucolor_25, thissetting)
    if choicemenucolor__specfile == 26: toggle_color(menucolor_26, thissetting)
    if choicemenucolor__specfile == 27: toggle_color(menucolor_27, thissetting)
    if choicemenucolor__specfile == 28: toggle_color(menucolor_28, thissetting)
    if choicemenucolor__specfile == 29: toggle_color(menucolor_29, thissetting)
    if choicemenucolor__specfile == 30: toggle_color(menucolor_30, thissetting)
# 
def color__file_toggle(thissetting):

    choicecolor__file = dialog.select('Choose Color for  '+thissetting, [color_0,color_1,color_2,
                                     color_21,
                                     color_61,
                                     color_15,
                                     color_94,
                                     color_22,
                                     color_25,
                                     'Blue',
                                     'Grey',
                                     'Green',
                                     'Red',
                                     'White',
                                     'Brown',
                                     'Purple',
                                     'Yellow',])
                                     
    if choicecolor__file == 0: toggle_color(color_0, thissetting)# transparent
    if choicecolor__file == 1: toggle_color(color_1, thissetting)# black
    if choicecolor__file == 2: toggle_color(color_2, thissetting)# white
    # favs
    if choicecolor__file == 3: toggle_color(color_21, thissetting)#   steelblue
    if choicecolor__file == 4: toggle_color(color_61, thissetting)#   firebrick
    if choicecolor__file == 5: toggle_color(color_15, thissetting)#   slategrey
    if choicecolor__file == 6: toggle_color(color_94, thissetting)#   olivedrab
    if choicecolor__file == 7: toggle_color(color_22, thissetting)#   skyblue
    if choicecolor__file == 8: toggle_color(color_25, thissetting)#   cadetblue
    #blue
    if choicecolor__file == 9: menucolor__file_toggle(thissetting,color_21,color_20,color_22,color_23,color_24,color_25,color_26,color_27,color_28,color_29,color_30,color_31,color_32,color_33,color_34,color_35,color_36,color_37,color_38,color_39,color_40,color_41,color_42,color_43,color_44,color_45,color_46,color_47,color_48,color_49,color_50)
    #Grey
    if choicecolor__file == 10: menucolor__file_toggle(thissetting,color_15,color_11,color_12,color_13,color_14,color_15,color_16,color_17,color_18,color_19,color_51,color_52,color_53,color_54,color_55,color_56,color_57,color_58,color_59,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0)
    #green
    if choicecolor__file == 11: menucolor__file_toggle(thissetting,color_0,color_80,color_81,color_82,color_8,color_84,color_85,color_86,color_87,color_88,color_89,color_90,color_91,color_92,color_93,color_94,color_95,color_96,color_97,color_98,color_99,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0)
    #red
    if choicecolor__file == 12: menucolor__file_toggle(thissetting,color_0,color_60,color_61,color_62,color_63,color_64,color_65,color_66,color_67,color_68,color_69,color_70,color_71,color_72,color_73,color_74,color_75,color_76,color_77,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0)
    #white
    if choicecolor__file == 13: menucolor__file_toggle(thissetting,color_0,color_1,color_2,color_3,color_4,color_5,color_6,color_7,color_8,color_9,color_10,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0)
    #brown
    if choicecolor__file == 14: menucolor__file_toggle(thissetting,color_0,color_100,color_101,color_102,color_103,color_104,color_105,color_106,color_107,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0)
    #purple
    if choicecolor__file == 15: menucolor__file_toggle(thissetting,color_0,color_108,color_109,color_110,color_111,color_112,color_113,color_114,color_115,color_116,color_117,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0)
    #yellow
    if choicecolor__file == 16: menucolor__file_toggle(thissetting,color_0,color_120,color_121,color_122,color_123,color_124,color_125,color_126,color_127,color_128,color_129,color_130,color_131,color_132,color_133,color_134,color_135,color_136,color_137,color_138,color_139,color_140,color_141,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0)
#


def _failsafes_copy(source,dest):
    if os.path.exists(dest):
        return
    if not os.path.exists(source):
        return
    _WriteText(source, dest) 
    #return True
    
#################################################
# Write source text to file
#################################################   
def _WriteText(SourceFile, DestFile):
    #xbmc.log(msg='##['+ADDONID+'] Write text', level=xbmc.LOGNOTICE)
    if os.path.exists(SourceFile):
        try:
            s=open(SourceFile).read()
            f=open(DestFile,'w')
            f.write(s)
            f.close()
            s.close()
        except: pass
#
#################################################
# Append source text to file
#################################################   
def _AppendText(SourceFile, DestFile):
    #xbmc.log(msg='##['+ADDONID+'] Append text', level=xbmc.LOGNOTICE)
    if os.path.exists(SourceFile):
        try:
            s=open(SourceFile).read()
            f=open(DestFile,'a')
            f.write(s)
            f.close()
            s.close()
        except: pass
#










################################################################################
#   ffmpeg Menu
#https://trac.ffmpeg.org/wiki/Creating%20multiple%20outputs
#https://trac.ffmpeg.org/wiki/StreamingGuide
#https://github.com/WritingMinds/ffmpeg-android   # pre built binaries
################################################################################
def record_Menu():
    ffmpeg   = ADDON_CORE.getSetting('autoplaywiths.ffmpeg')
    if url == 'none': dialog.ok('No URL', 'Please start a channel first')
    choiceffmpeg = dialog.select('Record [COLOR yellow]'+channel+ '[/COLOR]  to '+autoplaywiths_folder+ ' url:'+url,
                                                    ['[COLOR red]Stop[/COLOR]  Recording [COLOR yellow]'+channel+'[/COLOR]', 
                                                    '[COLOR green]Start[/COLOR]  Recording  (Indefinite)',
                                                    '[COLOR green]Start[/COLOR]  Recording  (Indefinite with udp)',
                                                    'Open PVR Folder '+autoplaywiths_folder,
                                                    'Play with VLC',
                                                    'Start and play on '+udp,
                                                    'Play '+udp,
                                                    'Start Recording  (30  mins)',
                                                    'Start Recording  (60  mins)',
                                                    'Start Recording  (90  mins)',
                                                    'Start Recording  (120 mins)',
                                                    'Start Recording  (1 min)'])
    if choiceffmpeg == 0: stop_ffmpeg()                # Exit ffmpeg via taskkill
    if choiceffmpeg == 1: record_ffmpeg('10000',udp,1) # Indefinite  you stop it manually
    if choiceffmpeg == 2: record_ffmpeg_udp('10000',udp,1) # Indefinite  you stop it manually with udp for 2 accounts on a pay server
    if choiceffmpeg == 3: pvr_folder()                  # Open Recording Folder
    if choiceffmpeg == 4: start_udp_ffmpeg(udp)         # Start UDP STream
    if choiceffmpeg == 5: play_udp_ffmpeg(udp)          # Play UDP Stream
    if choiceffmpeg == 6: record_ffmpeg('1800',udp,1)   # 30 min 1800
    if choiceffmpeg == 7: record_ffmpeg('3600',udp,1)   # 60 min 3600 
    if choiceffmpeg == 8: record_ffmpeg('5400',udp,1)   # 90 min 5400
    if choiceffmpeg == 9: record_ffmpeg('7200',udp,1)   # 2 hours 7200
    if choiceffmpeg == 10: record_ffmpeg('60',udp,1)    # 1 minute
    if choiceffmpeg == 11: play_vlc()                   # Record screen with ffmpeg
    
################################################################################
#   Stop Recording
################################################################################
def stop_ffmpeg():
    #if not xbmc.getCondVisibility('system.platform.windows'): dialog.ok('Wrong OS', 'Currently only works on Windows',  'WIP');sys.exit(0)
    xbmc.log(msg='##['+ADDONID+'] Stopping 3rd Party Player Playback or recording', level=xbmc.LOGNOTICE)
    if xbmc.getCondVisibility('system.platform.windows'):
        try: os.system('@ECHO off');os.system('TASKKILL /im ffmpeg.exe /f');os.system('TASKKILL /im ffplay.exe /f');os.system('TASKKILL /im rtmpdump.exe /f')
        except: pass
#

################################################################################
#   Record with ffmpeg
################################################################################
def record_ffmpeg(seconds, the_udp, ffmpeg_string):
    #if not xbmc.getCondVisibility('system.platform.windows'): dialog.ok('Wrong OS', 'Currently only works on Windows',  'WIP');sys.exit(0)
    autoplaywiths_folder   = ADDON_CORE.getSetting('autoplaywiths.folder')
    if not autoplaywiths_folder :
        dialog.ok('Save Path', 'Enter where to save your recordings in settings.',  'Please enter one under Program Schedule tab')
        xbmcaddon.Addon(id=ADDONID_CORE).openSettings()
        sys.exit(0)
    if url: 
        ffmpeg = ADDON_CORE.getSetting('autoplaywiths.ffmpeg')
        filename = xbmc.translatePath(os.path.join(autoplaywiths_folder, "%s.ts" % name)) 
        xbmc.log(msg='##['+ADDONID+'] Start 3rd Party Player recording '+autoplaywiths_folder, level=xbmc.LOGNOTICE)
        #
        #cmd = [ffmpeg, "-y", "-i", url, "-c:v", "copy", "-c:a", "copy", "-t", str(seconds), "-f", "mpegts", "-map", "0:v", "-map", "0:a", filename]
        cmd = [ffmpeg, "-y", "-i", url, "-c:v", "copy", "-c:a", "copy", "-t", str(seconds), filename]
        #p = Popen(cmd,shell=True) # has NO cmd window info prompt
        p = Popen(cmd,shell=False) # has cmd window info prompt
        #xbmc.log(msg='##['+ADDONID+'] Start Record and Playback', level=xbmc.LOGNOTICE)
        #player.stop()
        xbmcgui.Dialog().notification('RECORD', 'Recording to '+autoplaywiths_folder, ICON, 2000, False)
        #time.sleep(5)
        #try: xbmc.executebuiltin('PlayMedia(%s)' % filename)
        #except: pass
        
        
#
################################################################################
#   Record with ffmpeg and udp for 2 account
################################################################################
def record_ffmpeg_udp(seconds, the_udp, ffmpeg_string):
    #if not xbmc.getCondVisibility('system.platform.windows'): dialog.ok('Wrong OS', 'Currently only works on Windows',  'WIP');sys.exit(0)
    autoplaywiths_folder   = ADDON_CORE.getSetting('autoplaywiths.folder')
    if not autoplaywiths_folder :
        dialog.ok('Save Path', 'Enter where to save your recordings in settings.',  'Please enter one under Program Schedule tab')
        xbmcaddon.Addon(id=ADDONID_CORE).openSettings()
        sys.exit(0)
    if url: 
        ffmpeg = ADDON_CORE.getSetting('autoplaywiths.ffmpeg')
        filename = xbmc.translatePath(os.path.join(autoplaywiths_folder, "%s.ts" % name)) 
        xbmc.log(msg='##['+ADDONID+'] Start 3rd Party Player recording '+autoplaywiths_folder, level=xbmc.LOGNOTICE)
        #
        cmd = [ffmpeg, "-y", "-i", url, "-c:v", "copy", "-c:a", "copy", "-t", str(seconds), "-f", "mpegts", "-map", "0:v", "-map", "0:a", filename]
        #p = Popen(cmd,shell=True) # has NO cmd window info prompt
        p = Popen(cmd,shell=False) # has cmd window info prompt
        xbmc.log(msg='##['+ADDONID+'] Start Record and Playback', level=xbmc.LOGNOTICE)
        player.stop()
        xbmcgui.Dialog().notification('RECORD', 'Recording to '+autoplaywiths_folder, ICON, 2000, False)
        time.sleep(5)
        try: xbmc.executebuiltin('PlayMedia(%s)' % filename)
        except: pass
        
        
################################################################################
#   Open PVR save folder
################################################################################
def pvr_folder():
    autoplaywiths_folder   = ADDON_CORE.getSetting('autoplaywiths.folder')
    if not autoplaywiths_folder :
        dialog.ok('Save Path', 'Enter where to save your recordings in settings.',  'Please enter one under Program Schedule tab')
        xbmcaddon.Addon(id=ADDONID_CORE).openSettings()
        sys.exit(0)
    xbmc.executebuiltin('ActivateWindow(10025,%s,return)' % autoplaywiths_folder)
#


#wip
################################################################################
#   Play with VLC
################################################################################
def play_vlc():
    #if not xbmc.getCondVisibility('system.platform.windows'): dialog.ok('Wrong OS', 'Currently only works on Windows',  'WIP');sys.exit(0)
    if url:
        if xbmc.getCondVisibility('system.platform.windows'):
            if os.path.exists('C:\Program Files\Videolan\VLC\VLC.exe'): vlc = 'C:\Program Files\Videolan\VLC\VLC.exe'
            if os.path.exists('C:\Program Files (x86)\Videolan\VLC\VLC.exe'): vlc = "C:\Program Files (x86)\Videolan\VLC\VLC.exe"
            cmd = [vlc, "--play-and-exit", "--video-on-top", "--fullscreen", url]
            if player.isPlaying():  player.stop()
            #p = Popen(cmd,shell=True) # has NO cmd window info prompt
            p = Popen(cmd,shell=False) # has cmd window info prompt
        
        if xbmc.getCondVisibility('system.platform.android'):
            #if os.path.exists('C:\Program Files\Videolan\VLC\VLC.exe'): vlc = 'C:\Program Files\Videolan\VLC\VLC.exe'
            if player.isPlaying():  player.stop()
            #xbmc.executebuiltin('XBMC.StartAndroidActivity("org.acestream","android.intent.action.VIEW","","'+chid+'")')
            #xbmc.executebuiltin('XBMC.StartAndroidActivity("ru.vidsoftware.acestreamcontroller.free","android.intent.action.VIEW","","'+chid+'")')
#


################################################################################
#   Start a udp of current channel and play
################################################################################
# Works but crashes sometimes
def start_udp_ffmpeg(the_udp):
    ffmpeg = ADDON_CORE.getSetting('autoplaywiths.ffmpeg')
    if url:   
        xbmc.log(msg='##['+ADDONID+'] Start ffmpeg UDP '+the_udp, level=xbmc.LOGNOTICE)
        xbmcgui.Dialog().notification('UDP', 'Start UDP to '+the_udp, ICON, 2000, False)
        cmd = [ffmpeg, "-y", "-re", "-i", url, "-c:v", "copy", "-c:a", "copy", "-f", "mpegts", "-map", "0:v", "-map", "0:a", the_udp]
        #p = Popen(cmd,shell=True) # has NO cmd window info prompt
        p = Popen(cmd,shell=False) # has cmd window info prompt
        player.stop()
        time.sleep(5)
        xbmc.executebuiltin('PlayMedia(%s)' % the_udp)



################################################################################
#   Play UDP with ffmpeg
################################################################################
def play_udp_ffmpeg(the_udp):
    #if not xbmc.getCondVisibility('system.platform.windows'): dialog.ok('Wrong OS', 'Currently only works on Windows',  'WIP');sys.exit(0)
    xbmcgui.Dialog().notification('UDP', 'Play '+the_udp, ICON, 2000, False)
    xbmc.log(msg='##['+ADDONID+'] Play '+the_udp, level=xbmc.LOGNOTICE)
    if xbmc.getCondVisibility('system.platform.windows'): xbmc.executebuiltin('PlayMedia(%s)' % the_udp)















###########################################
###########################################
# ARGUMENT MENU
# run in :
# script-tvguide-main.xml 102 103 104 108 420
# script-tvguide-streamaddon.xml 102 103
# script-tvguide-streamsetup.xml 101
# script-tvguide-vod-tv.xml  102 103 420
# script-tvguide-menu.xml    101 102 103 105 106 107 110 111 112 113 114 115 116 117  290 291 420 666 200 210 211 212 213 214 215 216 217 218 219 220 221 222 # 200 - 209 are custom help 
###########################################
###########################################
if __name__ == '__main__':
    #if not len(sys.argv) > 1: xbmcgui.Dialog().notification('Skin', 'skin.py with no args', ICON, 1000, False)
    if len(sys.argv) > 1:
        mode = int(sys.argv[1])
        
        # Self masturbation for log   http://www.kammerl.de/ascii/AsciiSignature.php    fire_font-s
        xbmc.log(msg='|_   _\ \ / /     / __| | | |_ _||   \| __|', level=xbmc.LOGNOTICE)
        xbmc.log(msg='  | |  \ V /     | (_ | |_| || | | |) | _|' , level=xbmc.LOGNOTICE)
        xbmc.log(msg='  |_|   \_/       \___|\___/|___||___/|___|', level=xbmc.LOGNOTICE)
        xbmc.log(msg='##['+ADDONID+'] *TV Guide is not in anyway associated with kodi.tv or TV Guide Magazine and is a third party Kodi Addon.  Please dont post any question related to this Addon on official Kodi forum(forum.kodi.tv).  This opens as a TV Guide under programs, and an addon tool under video addons. I dont advertise this plugin publicly.  Please respect that.', level=xbmc.LOGNOTICE)
        
        # x Reopen Guide failsafe button if crash
        if mode == 100: _reopen()
        
        # refresh inis
        if mode == 101:
           refresh_ini()
               
        
        # search channel in ini
        if mode == 102:
            xbmcgui.Dialog().notification('Run', 'plugin.video.addons.ini.search', ICON, 1000, False)
            if xbmc.getCondVisibility('System.HasAddon(plugin.video.addons.ini.search)'): xbmc.executebuiltin("RunAddon(plugin.video.addons.ini.search)")
            if not xbmc.getCondVisibility('System.HasAddon(plugin.video.addons.ini.search)'):
                try:  xbmc.executebuiltin("ActivateWindow(10025,plugin://"+ADDONID+"/search_dialog,return)")
                except: pass
                
        # play url directly from ini
        if mode == 103:
            xbmcgui.Dialog().notification('Run', 'plugin.video.addons.ini.player', ICON, 1000, False)
            if xbmc.getCondVisibility('System.HasAddon(plugin.video.addons.ini.player)'): xbmc.executebuiltin("RunAddon(plugin.video.addons.ini.player)")
            if not xbmc.getCondVisibility('System.HasAddon(plugin.video.addons.ini.player)'):
                try:  xbmc.executebuiltin("ActivateWindow(10025,plugin://"+ADDONID+"/skin_iniplayer,return)")
                except: pass
                
        # Extra custom Title search
        # 80000 this is entirely done inside the gui.py
        if mode == 104:
            try:  import menu_lookups
            except ImportError:  dialog.ok('Search Title', 'Not available in this skin "' + skin_user + '"')
            else:
                program = '(No Title)';season = '';episode = '';language = 'en';description = ''
                menu_lookups.lookups_menu(program,season,episode,language,description) # Lookups Menus
                
        # Run core addon
        if mode == 105:
            xbmc.executebuiltin('XBMC.ActivateWindow(home)')
            xbmc.sleep(350)
            try:  xbmc.executebuiltin("RunAddon("+ADDONID_CORE+")")
            except: pass
            
        # Open core settings
        if mode == 106:
            xbmc.executebuiltin('XBMC.ActivateWindow(home)')
            try:  xbmcaddon.Addon(id=ADDONID_CORE).openSettings();sys.exit(0)
            except: pass
        
        # Toggle the picture in picture videowindow as a background
        if mode == 107: xbmcgui.Dialog().notification('Toggle', 'PIP Video Background', ICON, 1000, False); _pip_toggle()
        
        # Toggle the channel logo icons
        if mode == 108: xbmcgui.Dialog().notification('Toggle', 'Logos', ICON, 1000, False); _logos_toggle()
        
            
        # Horizontal Reverse the description area with the epg columns
        if mode == 110:
            xbmcgui.Dialog().notification('Toggle', 'Flip Description', ICON, 1000, False)
            xbmc.executebuiltin('XBMC.ActivateWindow(home)')
            xbmc.sleep(350)
            _skinflip_toggle(flipmenu, '720p')
            _skinflip_toggle(flipmain, '720p')
            _skinflip_toggle(flipvod, '720p')
            _skinflip_toggle(flipstreamaddon, '720p')

            _skinflip_toggle(flipmenu, '1080i')
            _skinflip_toggle(flipmain, '1080i')
            _skinflip_toggle(flipvod, '1080i')
            _skinflip_toggle(flipstreamaddon, '1080i')
            _reopen()
            

        # Vertical Reverse the description area with videowindow
        if mode == 111: 
            xbmcgui.Dialog().notification('Toggle', 'Flip Videowindow', ICON, 1000, False)
            xbmc.executebuiltin('XBMC.ActivateWindow(home)')
            xbmc.sleep(350)
            _skinvideowindow_toggle(flipmenu, '720p')
            _skinvideowindow_toggle(flipmain, '720p')
            _skinvideowindow_toggle(flipvod, '720p')

            _skinvideowindow_toggle(flipmenu, '1080i')
            _skinvideowindow_toggle(flipmain, '1080i')
            _skinvideowindow_toggle(flipvod, '1080i')
            _reopen()
            
            
        # Toggle Colums
        if mode == 112:  xbmcgui.Dialog().notification('Toggle', 'Colums', ICON, 1000, False); _colums_toggle()
        
        
        # toggle List View for Choose Stream
        if mode == 113: xbmcgui.Dialog().notification('Toggle', 'List View for Choose Stream', ICON, 1000, False); _ChooseStream_toggle()
        
        
        # toggle 1080p
        if mode == 114:
            xbmc.executebuiltin('XBMC.ActivateWindow(home)')
            xbmc.sleep(350)
            _toggle_1080()
            _reopen()
        
        # toggle gif
        if mode == 115:
            #_skingif_toggle(('program.background.color')
            xbmcgui.Dialog().notification('Toggle', 'Toggle Gif', ICON, 1000, False)
            xbmc.executebuiltin('XBMC.ActivateWindow(home)')
            xbmc.sleep(350)
            _skingif_toggle(flipmain, '720p')
            _skingif_toggle(flipmain, '1080i')
            _reopen()
        
        
        # 16 to 17 toggle
        if mode == 116: 
            xbmcgui.Dialog().notification('Toggle', '16 to 17 toggle', ICON, 1000, False)
            xbmc.executebuiltin('XBMC.ActivateWindow(home)')
            xbmc.sleep(350)
            _skinversion_toggle(flipmenu, '720p')
            _skinversion_toggle(flipmain, '720p')
            _skinversion_toggle(flipvod, '720p')
            _skinversion_toggle(flipstreamsetup, '720p')
            _skinversion_toggle(flipmenu, '1080i')
            _skinversion_toggle(flipmain, '1080i')
            _skinversion_toggle(flipvod, '1080i')
            _skinversion_toggle(flipstreamsetup, '1080i')
            _reopen()
            
        # xxxxxxxxxxxxxx play url directly from playlist.m3u             wip
        if mode == 117:
            playlistFile = xbmc.translatePath(os.path.join(basePath, 'playlist.m3u'))
            playlistFile2 = xbmc.translatePath(os.path.join(basePath, 'resources', 'playlist.m3u'))
            xbmcgui.Dialog().notification('playlist.m3u', 'Browse playlist.m3u', ICON, 1000, False)
            if os.path.exists(playlistFile):
                xbmc.executebuiltin('ActivateWindow(10025,'+playlistFile+',return)')
            if not os.path.exists(playlistFile):
                if os.path.exists(playlistFile2):
                    xbmc.executebuiltin('ActivateWindow(10025,'+playlistFile2+',return)')
                    if not os.path.exists(playlistFile2):
                        xbmcgui.Dialog().notification('Missing', 'No playlist.m3u found.', ICON, 1000, False)
                        
        if mode == 150: vod_Menu()
        if mode == 151: _openguixml('script-tvguide-vod-tv.xml')
        
        # Custom Help Menu
        if mode == 200: help_Menu()
        if mode == 201: help_run(help1)
        if mode == 202: help_run(help2)
        if mode == 203: help_run(help3)
        if mode == 204: help_run(help4)
        if mode == 205: help_run(help5)
        if mode == 206: help_run(help6)
        if mode == 207: help_run(help7)
        if mode == 208: help_run(help8)
        if mode == 209: help_run(help9)
        if mode == 210: help_run(help10)
        if mode == 211: help_run(help11)
        if mode == 212: help_run(help12)
        if mode == 213: help_run(help13)
        if mode == 214: help_run(help14)
        if mode == 215: help_run(help15)
        if mode == 216: help_run(help16)
        if mode == 217: help_run(help17)
        if mode == 218: help_run(help18)
        if mode == 219: help_run(help19)
        if mode == 220: help_run(help20)
        if mode == 221: help_run(help21)
        if mode == 222: help_run(help22)
        
        # Kodi colors
        #color_0 = '[COLOR 00000000]none[/COLOR]'
        color_0 = '[COLOR 00000000]transparent[/COLOR]'
        color_1 = '[COLOR ff606060]black[/COLOR]'
        #white
        color_2 = '[COLOR ffffffff]white[/COLOR]'
        color_3 = '[COLOR fff5f5f5]whitesmoke[/COLOR]'
        color_4 = '[COLOR fffaebd7]antiquewhite[/COLOR]'
        color_5 = '[COLOR fffffff0]ivory[/COLOR]'
        color_6 = '[COLOR fffffafa]snow[/COLOR]'
        color_7 = '[COLOR fff5f5dc]beige[/COLOR]'
        color_8 = '[COLOR fffffaf0]floralwhite[/COLOR]'
        color_9 = '[COLOR fff8f8ff]ghostwhite[/COLOR]'
        color_10 = '[COLOR ffffdead]navajowhite[/COLOR]'
        #Grey
        color_11 = '[COLOR ff808080]grey[/COLOR]'
        color_12 = '[COLOR ffc0c0c0]silver[/COLOR]'
        color_13 = '[COLOR ffa9a9a9]darkgrey[/COLOR]'
        color_14 = '[COLOR ff2f4f4f]darkslategrey[/COLOR]'
        color_15 = '[COLOR ff708090]slategrey[/COLOR]'
        color_16 = '[COLOR ff696969]dimgrey[/COLOR]'
        color_17 = '[COLOR ffd3d3d3]lightgrey[/COLOR]'
        color_18 = '[COLOR ff778899]lightslategrey[/COLOR]'
        color_19= '[COLOR ffdcdcdc]gainsboro[/COLOR]'
        #blue
        color_20 = '[COLOR ff0000ff]blue[/COLOR]'
        color_21 = '[COLOR ff4682b4]steelblue[/COLOR]'
        color_22 = '[COLOR ff87ceeb]skyblue[/COLOR]'
        color_23 = '[COLOR ff6a5acd]slateblue[/COLOR]'
        color_24 = '[COLOR ff00ffff]cyan[/COLOR]'
        color_25 = '[COLOR ff5f9ea0]cadetblue[/COLOR]'
        color_26 = '[COLOR ff00008b]darkblue[/COLOR]'
        color_27 = '[COLOR ff008b8b]darkcyan[/COLOR]'
        color_28 = '[COLOR ff483d8b]darkslateblue[/COLOR]'
        color_29 = '[COLOR ff9932cc]darkorchid[/COLOR]'
        color_30 = '[COLOR ff483d8b]darkslateblue[/COLOR]'
        color_31 = '[COLOR ff00ced1]darkturquoise[/COLOR]'
        color_32 = '[COLOR ff00bfff]deepskyblue[/COLOR]'
        color_33 = '[COLOR ff1e90ff]dodgerblue[/COLOR]'
        color_34 = '[COLOR ff4169e1]royalblue[/COLOR]'
        color_35 = '[COLOR ff000080]navy[/COLOR]'
        color_36 = '[COLOR ffe0ffff]lightcyan[/COLOR]'
        color_37 = '[COLOR ff8a2be2]blueviolet[/COLOR]'
        color_38 = '[COLOR fff0f8ff]aliceblue[/COLOR]'
        color_39 = '[COLOR ff7fffd4]aquamarine[/COLOR]'
        color_40 = '[COLOR fff0ffff]azure[/COLOR]'
        color_41 = '[COLOR ff6495ed]cornflowerblue[/COLOR]'
        color_42 = '[COLOR ff191970]midnightblue[/COLOR]'
        color_43 = '[COLOR ff66cdaa]mediumaquamarine[/COLOR]'
        color_44 = '[COLOR ff0000cd]mediumblue[/COLOR]'
        color_45 = '[COLOR ffba55d3]mediumorchid[/COLOR]'
        color_46 = '[COLOR ff7b68ee]mediumslateblue[/COLOR]'
        color_47 = '[COLOR ffb0c4de]lightsteelblue[/COLOR]'
        color_48 = '[COLOR ffb0e0e6]powderblue[/COLOR]'
        color_49 = '[COLOR ffadd8e6]lightblue[/COLOR]'
        color_50 = '[COLOR ff87cefa]lightskyblue[/COLOR]'
        color_51 = '[COLOR ff48d1cc]mediumturquoise[/COLOR]'
        color_52 = '[COLOR ff40e0d0]turquoise[/COLOR]'
        color_53 = '[COLOR ffe6e6fa]lavender[/COLOR]'
        color_54 = '[COLOR fffff0f5]lavenderblush[/COLOR]'
        color_55 = '[COLOR fffff5ee]seashell[/COLOR]'
        color_56 = '[COLOR ff008080]teal[/COLOR]'
        color_57 = '[COLOR ffff7f50]coral[/COLOR]'
        color_58 = '[COLOR fff08080]lightcoral[/COLOR]'
        color_59 = '[COLOR ffafeeee]paleturquoise[/COLOR]'
        #red
        color_60 = '[COLOR ffff0000]red[/COLOR]'
        color_61 = '[COLOR ffb22222]firebrick[/COLOR]'
        color_62 = '[COLOR ff8b0000]darkred[/COLOR]'
        color_63 = '[COLOR ffff6347]tomato[/COLOR]'
        color_64 = '[COLOR ffe9967a]darksalmon[/COLOR]'
        color_65 = '[COLOR ffffa07a]lightsalmon[/COLOR]'
        color_66 = '[COLOR ffdc143c]crimson[/COLOR]'
        color_67 = '[COLOR ff800000]maroon[/COLOR]'
        color_68 = '[COLOR ffcd5c5c]indianred[/COLOR]'
        color_69 = '[COLOR ffc71585]mediumvioletred[/COLOR]'
        color_70 = '[COLOR ffdb7093]palevioletred[/COLOR]'
        color_71 = '[COLOR fffa8072]salmon[/COLOR]'
        color_72 = '[COLOR ffffc0cb]pink[/COLOR]'
        color_73 = '[COLOR ffffb6c1]lightpink[/COLOR]'
        color_74 = '[COLOR ffff69b4]hotpink[/COLOR]'
        color_75 = '[COLOR ffff1493]deeppink[/COLOR]'
        color_76 = '[COLOR ffffdab9]peachpuff[/COLOR]'
        color_77 = '[COLOR ffffe4e1]mistyrose[/COLOR]'
        color_78 = ''
        color_79 = ''
        #green
        color_80 = '[COLOR ff008000]green[/COLOR]'
        color_81 = '[COLOR ff006400]darkgreen[/COLOR]'
        color_82 = '[COLOR ffbdb76b]darkkhaki[/COLOR]'
        color_83 = '[COLOR ff556b2f]darkolivegreen[/COLOR]'
        color_84 = '[COLOR ff228b22]forestgreen[/COLOR]'
        color_85 = '[COLOR ff8fbc8f]darkseagreen[/COLOR]'
        color_86 = '[COLOR ff7cfc00]lawngreen[/COLOR]'
        color_87 = '[COLOR ff3cb371]mediumseagreen[/COLOR]'
        color_88 = '[COLOR ff00fa9a]mediumspringgreen[/COLOR]'
        color_89 = '[COLOR ff98fb98]palegreen[/COLOR]'
        color_90 = '[COLOR ff2e8b57]seagreen[/COLOR]'
        color_91 = '[COLOR ffadff2f]greenyellow[/COLOR]'
        color_92 = '[COLOR ff00ff7f]springgreen[/COLOR]'
        color_93 = '[COLOR ff808000]olive[/COLOR]'
        color_94 = '[COLOR ff6b8e23]olivedrab[/COLOR]'
        color_95 = '[COLOR ffbdb76b]darkkhaki[/COLOR]'
        color_96 = '[COLOR fff0e68c]khaki[/COLOR]'
        color_97 = '[COLOR ff00ff00]lime[/COLOR]'
        color_98 = '[COLOR ff90ee90]lightgreen[/COLOR]'
        color_99 = '[COLOR ff20b2aa]lightseagreen[/COLOR]'
        #color_0 = '[COLOR ff32cd32]limegreen[/COLOR]'
        #color_0 = '[COLOR ff7fff00]chartreuse[/COLOR]'
        #color_0 = '[COLOR fff5fffa]mintcream[/COLOR]'
        #brown
        color_100 = '[COLOR ffa52a2a]brown[/COLOR]'
        color_101 = '[COLOR ffd2b48c]tan[/COLOR]'
        color_102 = '[COLOR ffd2691e]chocolate[/COLOR]'
        color_103 = '[COLOR ff8b4513]saddlebrown[/COLOR]'
        color_104 = '[COLOR fff4a460]sandybrown[/COLOR]'
        color_105 = '[COLOR ffbc8f8f]rosybrown[/COLOR]'
        color_106 = '[COLOR ffdeb887]burlywood[/COLOR]'
        color_107 = '[COLOR ffffebcd]blanchedalmond[/COLOR]'
        #purple
        color_108 = '[COLOR ff800080]purple[/COLOR]'
        color_109 = '[COLOR ff9400d3]darkviolet[/COLOR]'
        color_110 = '[COLOR ff8b008b]darkmagenta[/COLOR]'
        color_111 = '[COLOR ff9370db]mediumpurple[/COLOR]'
        color_112 = '[COLOR ffdda0dd]plum[/COLOR]'
        color_113 = '[COLOR ffff00ff]magenta[/COLOR]'
        color_114 = '[COLOR ffee82ee]violet[/COLOR]'
        color_115 = '[COLOR ffda70d6]orchid[/COLOR]'
        color_116 = '[COLOR ff4b0082]indigo[/COLOR]'
        color_117 = '[COLOR ffd8bfd8]thistle[/COLOR]'
        color_118 = ''
        color_119 = ''
        #yellow
        color_120 = '[COLOR ffffff00]yellow[/COLOR]'
        color_121 = '[COLOR ffffffe0]lightyellow[/COLOR]'
        color_122 = '[COLOR fffffacd]lemonchiffon[/COLOR]'
        color_123 = '[COLOR ff9acd32]yellowgreen[/COLOR]'
        color_124 = '[COLOR ffffd700]gold[/COLOR]'
        color_125 = '[COLOR ffdaa520]goldenrod[/COLOR]'
        color_126 = '[COLOR ffb8860b]darkgoldenrod[/COLOR]'
        color_127 = '[COLOR fffafad2]lightgoldenrodyellow[/COLOR]'
        color_128 = '[COLOR ffeee8aa]palegoldenrod[/COLOR]'
        color_129 = '[COLOR fff5deb3]wheat[/COLOR]'
        color_130 = '[COLOR ffffa500]orange[/COLOR]'
        color_131 = '[COLOR ffff4500]orangered[/COLOR]'
        color_132 = '[COLOR ffff8c00]darkorange[/COLOR]'
        color_133 = '[COLOR ffffe4c4]bisque[/COLOR]'
        color_134 = '[COLOR fffaf0e6]linen[/COLOR]'
        color_135 = '[COLOR ffffe4b5]moccasin[/COLOR]'
        color_136 = '[COLOR fffdf5e6]oldlace[/COLOR]'
        color_137 = '[COLOR ffffefd5]papayawhip[/COLOR]'
        color_138 = '[COLOR ffcd853f]peru[/COLOR]'
        color_139 = '[COLOR ffa0522d]sienna[/COLOR]'
        color_140 = '[COLOR fffff8dc]cornsilk[/COLOR]'
        color_141 = '[COLOR fff0fff0]honeydew[/COLOR]'
        
        # toggle Background color
        if mode == 290: color__file_toggle('program.background.color')
        
        # toggle Catbar color
        if mode == 291: color__file_toggle('categories.background.color')
           
        # x ffmpeg record
        if mode == 420:
            record_Menu()
            '''
            try:  import skin_record
            except ImportError:  dialog.ok('Record', 'Not available in this skin "' + skin_user + '"')
            else:  skin_record.record_Menu()
            '''
        # Reset Database
        if mode == 666: xbmc.executebuiltin('XBMC.ActivateWindow(home)'); deletedatabase_Menu()
           
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
    
