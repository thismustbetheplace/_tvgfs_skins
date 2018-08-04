# This script allows for extra scripts assigned to buttons for custom per skin creator functions to share ideas
# This uses the same as Reloadaddonfolders.py from main tv guide addon but cleans the channel names better
# If this file is missing it will fallback to the default Reloadaddonfolders.py
# -*- coding: utf-8 -*-
import xbmc, xbmcaddon, xbmcgui, xbmcplugin
import sys
import os
import xbmcvfs
import shutil
import re
import glob
import string
import json

ADDONID_TVGFS   = 'script.tvguide.fullscreen'
ADDON_TVGFS     = xbmcaddon.Addon(id=ADDONID_TVGFS)

ADDONID   = 'script.tvguide.fullscreen.skin.cake'
ADDON     = xbmcaddon.Addon(id=ADDONID)

file_name      = xbmc.translatePath(os.path.join('special://profile/','addon_data',ADDONID_TVGFS,'folders.list'))
addonsini_name = xbmc.translatePath(os.path.join('special://profile/','addon_data',ADDONID_TVGFS,'addons.ini'))
iconsini_name  = xbmc.translatePath(os.path.join('special://profile/','addon_data',ADDONID_TVGFS,'icons.ini'))
#m3u_name = xbmc.translatePath(os.path.join('special://profile/','addon_data',ADDONID_TVGFS,'playlist.m3u'))


# RPC
class RPCType(type):
    def __getattr__(cls, category):
        return Category(category)
class RPC(object):
    __metaclass__ = RPCType
class Category(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name.title().replace("_", "")
    def __getattr__(self, method):
        return Method(self, method)
class Method(object):
    def __init__(self, category, name):
        self.category = category
        self.name = name
    def __str__(self):
        return self.name.title().replace("_", "")
    def __call__(self, **kwargs):
        method = "%s.%s" % (str(self.category), str(self))
        query = {"method": method, "params": kwargs}
        return json_query(query)
class RPCError(Exception):
    pass
def json_query(query):
    if not "jsonrpc" in query:
        query["jsonrpc"] = "2.0"
    if not "id" in query:
        query["id"] = 1
    xbmc_request = json.dumps(query)
    raw = xbmc.executeJSONRPC(xbmc_request)
    clean = unicode(raw, 'utf-8', errors='ignore')
    response = json.loads(clean)
    if "error" in response:
        raise RPCError(response["error"])
    return response.get('result', response)
# RPC end





################################################################################
# ADD PASSWORD CREDENTIALS TO folders.list
################################################################################
theaddon = ADDON.getSetting('var.subpass') if not ADDON.getSetting('var.subpass') == '' else 'plugin.video.iptvsubs'
tmp_File = xbmc.translatePath(os.path.join('special://home', 'addons', 'packages','tmp'))
if os.path.exists(tmp_File): os.remove(tmp_File)
if xbmc.getCondVisibility('System.HasAddon(%s)' % theaddon):
    theaddon_addon = xbmcaddon.Addon(theaddon)
    theaddon_username = theaddon_addon.getSetting('kasutajanimi') if not theaddon_addon.getSetting('kasutajanimi') == '' else theaddon_addon.getSetting('username')
    theaddon_password = theaddon_addon.getSetting('salasona') if not theaddon_addon.getSetting('salasona') == '' else theaddon_addon.getSetting('password')
    if os.path.exists(file_name):
        try:
            os.rename(file_name, tmp_File)
            s=open(tmp_File).read()
            s=s.replace('subsuser',theaddon_username)
            s=s.replace('subspass',theaddon_password)
            f=open(file_name,'w')
            f.write(s)
            f.close()
            s.close()
        except: pass
if os.path.exists(tmp_File): os.remove(tmp_File)
######################################################


################################################################################
# folders.list
################################################################################
xbmc.log(msg='##['+ADDONID_TVGFS+'] Recreating subs', level=xbmc.LOGNOTICE)
f = xbmcvfs.File(file_name)
items = f.read().splitlines()
f.close()
unique = set(items)
if int(ADDON_TVGFS.getSetting('addons.ini.type')) == 1:
    customFile = str(ADDON_TVGFS.getSetting('addons.ini.file'))
    if os.path.exists(customFile) and os.access(customFile,os.W_OK):
        addonsini_name = customFile
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

f = xbmcvfs.File(addonsini_name,'wb')
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
        #name = name.replace(' HD','')
        #name = re.sub("ACSTREAM - .+",'ACSTREAM ',name)
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
        #name = name.translate(string.whitespace)
        #name = re.sub(r"\s+", "", name, flags=re.UNICODE)
        name = name.upper()

        ######## Clean Chan Name #######
        for rep in [r"\[/?[BI]\]", r"\[/?COLOR.*?\]",]: # removes bold and colour
            name = re.sub(rep, '', name)
            
        if 'play/movie' in stream:
            name = 'VOD  '+name
            
        if 'catchup' in stream:
            name = name+'  Catchup'
        
        #import scrub
        #chan_ids = scrub.chan_ids['','']
        #color = colors.color_name[ADDON.getSetting('timebar.color')]
        #name = name.replace(chan_ids)
        #'''
        # dumb strings
        name = name.replace(' (NEW)','')
        name = name.replace('*','')
        #name = name.replace('ACESTREAM - ','ACESTREAM ')
        name = name.replace(' W HD',' WEST')
        name = name.replace(' East HD',' HD')
        name = name.replace(' East','')
        name = name.replace(' EAST','')
        name = name.replace('HD (MTL)','MONTREAL')
        
        #
        # north america networks
        name = name.replace(' Vancover',' VANCOUVER')
        name = name.replace(' TORONTO','')
        name = name.replace(' HAMILTON','')
        # this is to eliminate city tv and vague comparisons
        name = name.replace('CITY TV','City')
        name = name.replace('CITYTV','City')
        name = name.replace('GLOBAL TV','GLOBAL')
        # uk networks
        name = name.replace('BBC1','BBC ONE')
        name = name.replace('BBC2','BBC TWO')
        name = name.replace('BBC3','BBC THREE')
        name = name.replace('BBC4','BBC FOUR')
        name = name.replace('ITV1','ITV 1')
        name = name.replace('ITV2','ITV 2')
        name = name.replace('ITV3','ITV 3')
        name = name.replace('ITV4','ITV 4')
        
        if 'ok2' in stream:
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
        #'''
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
        #
        write_str = "%s=%s\n" % (name,stream)
        f.write(write_str.encode("utf8"))
f.close()

#M3U WIP

'''
################################################################################
# PVR
################################################################################
#PVRACTIVE   = (xbmc.getCondVisibility('Pvr.HasTVChannels')) or (xbmc.getCondVisibility('Pvr.HasRadioChannels')) == True    
#if PVRACTIVE:
#if xbmc.getCondVisibility("Pvr.HasTVChannels"):
PVRACTIVE   = (xbmc.getCondVisibility('Pvr.HasTVChannels')) or (xbmc.getCondVisibility('Pvr.HasRadioChannels')) == True
if PVRACTIVE:
    index = 0
    urls = []
    channels = {}
    for group in ["radio","tv"]:
        urls = urls + xbmcvfs.listdir("pvr://channels/%s/All channels/" % group)[1]
    for group in ["radio","tv"]:
        groupid = "all%s" % group
        #json_query = RPC.get_channels(channelgroupid=groupid, properties=[ "thumbnail", "channeltype", "hidden", "locked", "channel", "lastplayed", "broadcastnow" ] )
        #json_query = RPC.PVR.get_channels(channelgroupid=groupid, properties=[ "thumbnail", "channeltype", "hidden", "locked", "channel", "lastplayed", "broadcastnow" ] )
        json_query = RPC.PVR.get_channels(channelgroupid=groupid, properties=["thumbnail", "channeltype", "hidden", "locked", "channel", "lastplayed", "broadcastnow"])
        if "channels" in json_query:
            for channel in json_query["channels"]:
                channelname = channel["label"]
                streamUrl = urls[index]
                index = index + 1
                url = "pvr://channels/%s/All channels/%s" % (group,streamUrl)
                channels[url] = channelname
    #TODO make this a function
    f = xbmcvfs.File(addonsini_name)
    items = f.read().splitlines()
    f.close()
    streams = {}
    addonId = 'nothing'
    for item in items:
        if item.startswith('['):
            addonId = item.strip('[] \t')
            streams[addonId] = {}
        elif item.startswith('#'):
            pass
        else:
            name_url = item.split('=',1)
            if len(name_url) == 2:
                name = name_url[0]
                url = name_url[1]
                if url:
                    streams[addonId][name] = url

    addonId = "script.tvguide.fullscreen"
    if addonId not in streams:
        streams[addonId] = {}
    for url in channels:
        name = channels[url]
        streams[addonId][name] = url

    f = xbmcvfs.File(addonsini_name,'a')
    write_str = "# WARNING Make a copy of this file.\n# It will be overwritten on the next folder add.\n\n"
    f.write(write_str.encode("utf8"))
    for addonId in sorted(streams):
        write_str = "[%s]\n" % (addonId)
        f.write(write_str)
        addonStreams = streams[addonId]
        for name in sorted(addonStreams):
            stream = addonStreams[name]
            if name.startswith(' '):
                continue
            name = re.sub(r'[,:=]',' ',name)
            if not stream:
                stream = 'nothing'
            write_str = "%s=%s\n" % (name,stream)
            try:
                f.write(write_str.encode("utf8"))
            except:
                f.write(write_str)
    f.close()
'''

'''
# wip to read folders list like channels do 
def _readfolderslist():
    import urllib
    import requests
    file_name = 'special://profile/addon_data/script.tvguide.fullscreen/folders.list'
    f = xbmcvfs.File(file_name)
    items = f.read().splitlines()
    f.close()
    unique = set(items)

    logos = {}
    for path in unique:
        try:
            response = RPC.files.get_directory(media="files", directory=path, properties=["thumbnail"])
        except:
            continue
        files = response["files"]
        #dirs = dict([[f["label"], f["file"]] for f in files if f["filetype"] == "directory"])
        #links = dict([[f["label"], f["file"]] for f in files if f["filetype"] == "file"])
        thumbnails = dict([[f["label"], f["thumbnail"]] for f in files if f["filetype"] == "file"])
        match = re.match(r"plugin://(.*?)/",path)
        if match:
            plugin = match.group(1)
        else:
            match = re.match(r"plugin://(.*?)$",path)
            if match:
                plugin = match.group(1)
            else:
                continue

        if plugin not in logos:
            logos[plugin] = {}

        thumbs = logos[plugin]
        for file in thumbnails:
            thumb = thumbnails[file]
            thumbs[file] = thumb
            
    logo_folder = 'special://profile/addon_data/script.tvguide.fullscreen/addon_logos/'
    for addonId in sorted(logos):
        folder = 'special://profile/addon_data/script.tvguide.fullscreen/addon_logos/%s' % addonId
        xbmcvfs.mkdirs(folder)
        addonLogos = logos[addonId]
        for label in sorted(addonLogos):
            logo = addonLogos[label]
            if logo:
                label = re.sub(r'[:/\\]', '',label)
                label = label.strip()
                label = re.sub(r"\[/?[BI]\]",'',label)
                label = re.sub(r"\[/?COLOR.*?\]",'',label)
                logo = re.sub(r'^image://','',logo)
                logo = urllib.unquote_plus(logo)
                logo = logo.strip('/')
                file_name = "%s/%s.png" % (folder,label)
                if not xbmcvfs.exists(file_name):
                    try:
                        r = requests.get(logo)
                        if r.status_code == 200:
                            f = xbmcvfs.File(file_name, 'wb')
                            chunk_size = 16 * 1024
                            for chunk in r.iter_content(chunk_size):
                                f.write(chunk)
                            f.close()
                    except Exception as detail:
                        xbmcvfs.copy(logo,file_name)
    dialog = xbmcgui.Dialog()
    dialog.notification("TV Guide Fullscreen","Done: Download Logos")
'''

################################################################################
# icons
################################################################################
f = xbmcvfs.File(iconsini_name,'wb')
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

# reopen
xbmc.executebuiltin('Dialog.Close(all,true)')
xbmc.executebuiltin('ActivateWindow(home)')
xbmc.sleep(500)
addonPath_tvgfs = xbmc.translatePath(os.path.join('special://home', 'addons', ADDONID_TVGFS))
xbmc.executebuiltin('RunScript('+ addonPath_tvgfs + '/addon.py)')


