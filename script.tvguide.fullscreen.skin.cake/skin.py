# -*- coding: utf-8 -*-
# This script allows for extra scripts assigned to buttons for custom per skin creator functions to share ideas
import sys
import xbmc,xbmcaddon,xbmcgui,xbmcvfs#,xbmcplugin
import os
import shutil
import re
import glob
#import string
ADDONID        = 'script.tvguide.fullscreen.skin.cake'
ADDON          = xbmcaddon.Addon(id=ADDONID)
addonPath      = xbmc.translatePath(os.path.join('special://home', 'addons', ADDONID))
basePath       = xbmc.translatePath(os.path.join('special://profile', 'addon_data', ADDONID))
helpdir        = xbmc.translatePath(os.path.join(addonPath, 'resources','help/'))
copysrc        = xbmc.translatePath(os.path.join(addonPath, 'resources'))
ICON           = ADDON.getAddonInfo('icon')
#FANART         = ADDON.getAddonInfo('fanart')
dialog         = xbmcgui.Dialog()
DP             = xbmcgui.DialogProgress()
# not needed
#ADDONNAME      = ADDON.getAddonInfo('name')
#ADDONVERSION   = ADDON.getAddonInfo('version')
#ADDONAUTHOR    = ADDON.getAddonInfo('author')
#ADDONCLOG      = ADDON.getAddonInfo('changelog')
#ADDONDESC      = ADDON.getAddonInfo('description')
#ADDONDISCLAIM  = ADDON.getAddonInfo('disclaimer')
#ADDONSUMMARY   = ADDON.getAddonInfo('summary')
#kodi_version   = xbmc.getInfoLabel('System.BuildVersion')  # as a number in quotes
#KODIV          = float(kodi_version[:4])                   # as a red number
#
ADDONID_TVGFS        = 'script.tvguide.fullscreen'
if not os.path.exists(xbmc.translatePath(os.path.join('special://home', 'addons', ADDONID_TVGFS))): xbmc.executebuiltin('RunPlugin(plugin://%s)' % ADDONID_TVGFS)
if not os.path.exists(xbmc.translatePath(os.path.join('special://home', 'addons', ADDONID_TVGFS))): ADDON_TVGFS = xbmcaddon.Addon(id=ADDONID)
if os.path.exists(xbmc.translatePath(os.path.join('special://home', 'addons', ADDONID_TVGFS))): ADDON_TVGFS  = xbmcaddon.Addon(id=ADDONID_TVGFS)
addonPath_tvgfs      = xbmc.translatePath(os.path.join('special://home', 'addons', ADDONID_TVGFS))
basePath_tvgfs       = xbmc.translatePath(os.path.join('special://profile', 'addon_data', ADDONID_TVGFS))
#addonPath_tvgfs     = ADDON_TVGFS.getAddonInfo('path').decode('utf-8')
#basePath_tvgfs      = ADDON_TVGFS.getAddonInfo('profile').decode('utf-8')
#
# set common files
addonini_tvgfs       = xbmc.translatePath(os.path.join(basePath_tvgfs, 'addons.ini'))
refreshdatabase      = xbmc.translatePath(os.path.join(addonPath_tvgfs, 'ResetDatabase.py'))
refreshaddon         = xbmc.translatePath(os.path.join(addonPath_tvgfs, 'ReloadAddonFolders.py'))
if os.path.exists(xbmc.translatePath(os.path.join(addonPath, 'ReloadAddonFolders.py'))): refreshaddon = xbmc.translatePath(os.path.join(addonPath, 'ReloadAddonFolders.py'))
#
# set skin user vars
skin                 = ADDON.getSetting('skin.user')   if not ADDON.getSetting('skin.user') == ''   else 'Cake'
skinfolder           = ADDON.getSetting('skin.folder') if not ADDON.getSetting('skin.folder') == '' else addonPath
skinPath             = xbmc.translatePath(os.path.join(skinfolder,'resources','skins',skin))# for skin toggle mods
fadepath             = xbmc.translatePath(os.path.join(skinPath,'media','fade/'))
fadewhitepath        = xbmc.translatePath(os.path.join(skinPath,'media','fadewhite/'))
calibrate            = xbmc.translatePath(os.path.join(skinPath,'media','calibrate/'))
rez                  = '1080i' if os.path.exists(xbmc.translatePath(os.path.join(skinfolder,'resources','skins',skin,'1080i'))) else '720p'# for skin toggle mods
installerskin        = '_gui' # Installer for tvgfs skin settings gui and logviewer with advancedsettings media in default skins dir
#
################################################################################
# THIS IS FOR RUNNING THE SKIN NOT INSTALLING #
# IMPORTANT - MAIN set window id and skin variables on load - only bool, label, image type strings
# ## This enters the setting or default value if no setting found.  As a fallback the skin will autoset defaults
# This is the function the skin first runs to set vars - must set it in the kin currently unless its a global setting
################################################################################
def set_skin_vars():
    #_set_skin_vars(sys.argv[1],sys.argv[2])
    # STEP 1 - skin xml sets the property "referencenumber" that is a value for 5100 posy that has to be manually written ahead of time
    # STEP 2 - skin xml launches this script and the path has to be set manually
    # STEP 3 - Thes values below are set if they find a setting in the settings.xml or else write default value.  Skin will wriye a default value if missing
    #
    # these are the main addons and paths
    #_set_skin_vars('rez',rez)# not used yet and 180i should be avoided imo until the logo alignment works
    _set_skin_vars('main_addon',ADDONID_TVGFS)# ie  tvgfs
    _set_skin_vars('skin_addon',ADDONID)# this addon
    _set_skin_vars('run_script','special://home/addons/'+ADDONID+'/skin.py')# to run this py for future scripts
    _set_skin_vars('xps_playlists',ADDON.getSetting('var.xps_playlists')) if not ADDON.getSetting('var.xps_playlists') == '' else 'special://profile/addon_data/'+ADDONID+'/resources/playlists/'
    _set_skin_vars('player_tags',ADDON.getSetting('var.player_tags')) if not ADDON.getSetting('var.player_tags') == '' else 'true'
    _set_skin_vars('animatedgifs',ADDON.getSetting('var.animatedgifs')) if not ADDON.getSetting('var.animatedgifs') == '' else 'true'
    _set_skin_vars('widgets',ADDON.getSetting('var.widgets')) if not ADDON.getSetting('var.widgets') == '' else 'true'
    # images
    _set_skin_vars('image_fade','fade/'+ADDON.getSetting('var.image_fade')) if not ADDON.getSetting('var.image_fade') == '' else 'fade/50.png'
    _set_skin_vars('image_fadebg','fade/'+ADDON.getSetting('var.image_fadebg')) if not ADDON.getSetting('var.image_fadebg') == '' else 'fade/50.png'
    _set_skin_vars('image_fadewhite','fadewhite/'+ADDON.getSetting('var.image_fadewhite')) if not ADDON.getSetting('var.image_fadewhite') == '' else 'fadewhite/50.png'
    _set_skin_vars('image_fadewhitebg','fadewhite/'+ADDON.getSetting('var.image_fadewhitebg')) if not ADDON.getSetting('var.image_fadewhitebg') == '' else 'fadewhite/50.png'
    _set_skin_vars('image_helpmarker',ADDON.getSetting('var.image_helpmarker')) if not ADDON.getSetting('var.image_helpmarker') == '' else 'buttons/help_marker.png'
    _set_skin_vars('image_panel',ADDON.getSetting('var.image_panel')) if not ADDON.getSetting('var.image_panel') == '' else 'backgrounds/panel.png'
    #_set_skin_vars('image_scrollbar',ADDON.getSetting('var.image_scrollbar')) if not ADDON.getSetting('var.image_scrollbar') == '' else 'scrollbar/scrollbar.png'
    '''
    _set_skin_vars('image_roundfo',ADDON.getSetting('var.image_roundfo')) if not ADDON.getSetting('var.image_roundfo') == '' else 'buttons/round-fo.png'
    _set_skin_vars('image_panelfo',ADDON.getSetting('var.image_panelfo')) if not ADDON.getSetting('var.image_panelfo') == '' else 'buttons/panel-focus.png'
    _set_skin_vars('image_popup_button',ADDON.getSetting('var.image_popup_button')) if not ADDON.getSetting('var.image_popup_button') == '' else 'buttons/popup_button.png'
    _set_skin_vars('image_popup_buttonfo',ADDON.getSetting('var.image_popup_buttonfo')) if not ADDON.getSetting('var.image_popup_buttonfo') == '' else 'buttons/popup_buttonfo.png'
    _set_skin_vars('image_button',ADDON.getSetting('var.image_button')) if not ADDON.getSetting('var.image_button') == '' else 'buttons/tvg-button-nofocus.png'
    _set_skin_vars('image_buttonfo',ADDON.getSetting('var.image_buttonfo')) if not ADDON.getSetting('var.image_buttonfo') == '' else 'buttons/tvg-button-focus.png'
    '''
    # colors
    _set_skin_vars('popup_background_color',ADDON.getSetting('var.popup_background_color')) if not ADDON.getSetting('var.popup_background_color') == '' else 'steelblue'
    _set_skin_vars('radio_color',ADDON.getSetting('var.radio_color')) if not ADDON.getSetting('var.radio_color') == '' else 'deepskyblue'
    _set_skin_vars('focus_color',ADDON.getSetting('var.focus_color')) if not ADDON.getSetting('var.focus_color') == '' else 'firebrick'
    _set_skin_vars('focus_current_color',ADDON.getSetting('var.focus_current_color')) if not ADDON.getSetting('var.focus_current_color') == '' else 'darkgreen'
    _set_skin_vars('scrollbarbg_color',ADDON.getSetting('var.scrollbarbg_color')) if not ADDON.getSetting('var.scrollbarbg_color') == '' else 'dimgrey'
    _set_skin_vars('scrollbarnf_color',ADDON.getSetting('var.scrollbarnf_color')) if not ADDON.getSetting('var.scrollbarnf_color') == '' else 'black'
    _set_skin_vars('progress_color',ADDON.getSetting('var.progress_color')) if not ADDON.getSetting('var.progress_color') == '' else 'darkcyan'
    _set_skin_vars('progressbg_color',ADDON.getSetting('var.progressbg_color')) if not ADDON.getSetting('var.progressbg_color') == '' else 'dimgrey'
    _set_skin_vars('description_bar_color',ADDON.getSetting('var.description_bar_color')) if not ADDON.getSetting('var.description_bar_color') == '' else 'green'
    _set_skin_vars('description_info_color',ADDON.getSetting('var.description_info_color')) if not ADDON.getSetting('var.description_info_color') == '' else 'skyblue'
    _set_skin_vars('bar_color',ADDON.getSetting('var.bar_color')) if not ADDON.getSetting('var.bar_color') == '' else 'lightgreen'
    _set_skin_vars('channelbg_color',ADDON.getSetting('var.channelbg_color')) if not ADDON.getSetting('var.channelbg_color') == '' else 'black'
    _set_skin_vars('epgbg_color',ADDON.getSetting('var.epgbg_color')) if not ADDON.getSetting('var.epgbg_color') == '' else 'dimgrey'

    # this is for the flip toggle and is based on a condition statement using slide animations
    #_set_skin_vars('referencenumber','240.6')# 240.6 or 30.6
    _set_skin_vars('referencenumber',ADDON.getSetting('var.referencenumber')) if not ADDON.getSetting('var.referencenumber') == '' else '240.6'
    if xbmc.getCondVisibility('String.IsEqual(Window(1100).Property(referencenumber),)'): _set_skin_vars('referencenumber','240.6')# 5001 bullshit
    #
    if not xbmc.getCondVisibility('String.IsEqual(Window(1100).Property(referencenumber),240.6)'): _set_skin_vars('flip_vertical','true');ADDON.setSetting('var.flip_vertical','true')# toggle
    else:  _set_skin_vars('flip_vertical','false');ADDON.setSetting('var.flip_vertical','false')# toggle
    #
    if ADDON.getSetting('var.flip_horizontal') == 'true': _set_skin_vars('flip_horizontal','true')# toggle
    else: _set_skin_vars('flip_horizontal','false')# toggle
    # not needed
    #_set_skin_vars('main_addon_usersettings',basePath_tvgfs)# ie  tvgfs  user_data
    #_set_skin_vars('skin_addon_usersettings',ADDONID)# this addon
    # these can be set in settings.xml
    #_set_skin_vars('popup_background_color',ADDON.getSetting('program.background.color')) if not ADDON.getSetting('program.background.color') == '' else 'steelblue'
    #_set_skin_vars('cat_color',ADDON.getSetting('categories.background.color')) if not ADDON.getSetting('categories.background.color') == '' else 'firebrick'
    #_set_skin_vars('cat_color',ADDON.getSetting('var.cat_color')) if not ADDON.getSetting('var.cat_color') == '' else 'firebrick'
    #_set_skin_vars('progresscache_color',ADDON.getSetting('var.progresscache_color')) if not ADDON.getSetting('var.progresscache_color') == '' else 'darkgrey'
    #_set_skin_vars('image_blackfade',  ADDON.getSetting('var.image_blackfade'))   if not ADDON.getSetting('var.image_blackfade') == ''   else 'backgrounds/black-clear.png'
    #_set_skin_vars('image_blackfade25',ADDON.getSetting('var.image_blackfade25')) if not ADDON.getSetting('var.image_blackfade25') == '' else 'trans/black25.png'
    #_set_skin_vars('image_blackfade75',ADDON.getSetting('var.image_blackfade75')) if not ADDON.getSetting('var.image_blackfade75') == '' else 'trans/black75.png'
    #_set_skin_vars('image_whitefade75',ADDON.getSetting('var.image_whitefade75')) if not ADDON.getSetting('var.image_whitefade75') == '' else 'trans/white75.png'
    # vod1 widgets
    if not ADDON.getSetting('vodtitle1') == '':  _set_skin_vars('vodtitle1', ADDON.getSetting('vodtitle1')); _set_skin_vars('vodpath1', ADDON.getSetting('vodpath1')); _set_skin_vars('vodthumb1', ADDON.getSetting('vodthumb1'))
    if not ADDON.getSetting('vodtitle2') == '':  _set_skin_vars('vodtitle2', ADDON.getSetting('vodtitle2')); _set_skin_vars('vodpath2', ADDON.getSetting('vodpath2')); _set_skin_vars('vodthumb2', ADDON.getSetting('vodthumb2'))
    if not ADDON.getSetting('vodtitle3') == '':  _set_skin_vars('vodtitle3', ADDON.getSetting('vodtitle3')); _set_skin_vars('vodpath3', ADDON.getSetting('vodpath3')); _set_skin_vars('vodthumb3', ADDON.getSetting('vodthumb3'))
    if not ADDON.getSetting('vodtitle4') == '':  _set_skin_vars('vodtitle4', ADDON.getSetting('vodtitle4')); _set_skin_vars('vodpath4', ADDON.getSetting('vodpath4')); _set_skin_vars('vodthumb4', ADDON.getSetting('vodthumb4'))
    if not ADDON.getSetting('vodtitle5') == '':  _set_skin_vars('vodtitle5', ADDON.getSetting('vodtitle5')); _set_skin_vars('vodpath5', ADDON.getSetting('vodpath5')); _set_skin_vars('vodthumb5', ADDON.getSetting('vodthumb5'))
    if not ADDON.getSetting('vodtitle6') == '':  _set_skin_vars('vodtitle6', ADDON.getSetting('vodtitle6')); _set_skin_vars('vodpath6', ADDON.getSetting('vodpath6')); _set_skin_vars('vodthumb6', ADDON.getSetting('vodthumb6'))
    if not ADDON.getSetting('vodtitle7') == '':  _set_skin_vars('vodtitle7', ADDON.getSetting('vodtitle7')); _set_skin_vars('vodpath7', ADDON.getSetting('vodpath7')); _set_skin_vars('vodthumb7', ADDON.getSetting('vodthumb7'))
    if not ADDON.getSetting('vodtitle8') == '':  _set_skin_vars('vodtitle8', ADDON.getSetting('vodtitle8')); _set_skin_vars('vodpath8', ADDON.getSetting('vodpath8')); _set_skin_vars('vodthumb8', ADDON.getSetting('vodthumb8'))
    if not ADDON.getSetting('vodtitle9') == '':  _set_skin_vars('vodtitle9', ADDON.getSetting('vodtitle9')); _set_skin_vars('vodpath9', ADDON.getSetting('vodpath9')); _set_skin_vars('vodthumb9', ADDON.getSetting('vodthumb9'))
    if not ADDON.getSetting('vodtitle10') == '': _set_skin_vars('vodtitle10',ADDON.getSetting('vodtitle10'));_set_skin_vars('vodpath10',ADDON.getSetting('vodpath10'));_set_skin_vars('vodthumb10',ADDON.getSetting('vodthumb10'))
    if not ADDON.getSetting('vodtitle11') == '': _set_skin_vars('vodtitle11',ADDON.getSetting('vodtitle11'));_set_skin_vars('vodpath11',ADDON.getSetting('vodpath11'));_set_skin_vars('vodthumb11',ADDON.getSetting('vodthumb11'))
    if not ADDON.getSetting('vodtitle12') == '': _set_skin_vars('vodtitle12',ADDON.getSetting('vodtitle12'));_set_skin_vars('vodpath12',ADDON.getSetting('vodpath12'));_set_skin_vars('vodthumb12',ADDON.getSetting('vodthumb12'))
    if not ADDON.getSetting('vodtitle13') == '': _set_skin_vars('vodtitle13',ADDON.getSetting('vodtitle13'));_set_skin_vars('vodpath13',ADDON.getSetting('vodpath13'));_set_skin_vars('vodthumb13',ADDON.getSetting('vodthumb13'))
    if not ADDON.getSetting('vodtitle14') == '': _set_skin_vars('vodtitle14',ADDON.getSetting('vodtitle14'));_set_skin_vars('vodpath14',ADDON.getSetting('vodpath14'));_set_skin_vars('vodthumb14',ADDON.getSetting('vodthumb14'))
    if not ADDON.getSetting('vodtitle15') == '': _set_skin_vars('vodtitle15',ADDON.getSetting('vodtitle15'));_set_skin_vars('vodpath15',ADDON.getSetting('vodpath15'));_set_skin_vars('vodthumb15',ADDON.getSetting('vodthumb15'))
    # vod2 widgets
    if not ADDON.getSetting('vod2title1') == '':  _set_skin_vars('vod2title1', ADDON.getSetting('vod2title1')); _set_skin_vars('vod2path1', ADDON.getSetting('vod2path1')); _set_skin_vars('vod2thumb1', ADDON.getSetting('vod2thumb1'))
    if not ADDON.getSetting('vod2title2') == '':  _set_skin_vars('vod2title2', ADDON.getSetting('vod2title2')); _set_skin_vars('vod2path2', ADDON.getSetting('vod2path2')); _set_skin_vars('vod2thumb2', ADDON.getSetting('vod2thumb2'))
    if not ADDON.getSetting('vod2title3') == '':  _set_skin_vars('vod2title3', ADDON.getSetting('vod2title3')); _set_skin_vars('vod2path3', ADDON.getSetting('vod2path3')); _set_skin_vars('vod2thumb3', ADDON.getSetting('vod2thumb3'))
    if not ADDON.getSetting('vod2title4') == '':  _set_skin_vars('vod2title4', ADDON.getSetting('vod2title4')); _set_skin_vars('vod2path4', ADDON.getSetting('vod2path4')); _set_skin_vars('vod2thumb4', ADDON.getSetting('vod2thumb4'))
    if not ADDON.getSetting('vod2title5') == '':  _set_skin_vars('vod2title5', ADDON.getSetting('vod2title5')); _set_skin_vars('vod2path5', ADDON.getSetting('vod2path5')); _set_skin_vars('vod2thumb5', ADDON.getSetting('vod2thumb5'))
    if not ADDON.getSetting('vod2title6') == '':  _set_skin_vars('vod2title6', ADDON.getSetting('vod2title6')); _set_skin_vars('vod2path6', ADDON.getSetting('vod2path6')); _set_skin_vars('vod2thumb6', ADDON.getSetting('vod2thumb6'))
    if not ADDON.getSetting('vod2title7') == '':  _set_skin_vars('vod2title7', ADDON.getSetting('vod2title7')); _set_skin_vars('vod2path7', ADDON.getSetting('vod2path7')); _set_skin_vars('vod2thumb7', ADDON.getSetting('vod2thumb7'))
    if not ADDON.getSetting('vod2title8') == '':  _set_skin_vars('vod2title8', ADDON.getSetting('vod2title8')); _set_skin_vars('vod2path8', ADDON.getSetting('vod2path8')); _set_skin_vars('vod2thumb8', ADDON.getSetting('vod2thumb8'))
    if not ADDON.getSetting('vod2title9') == '':  _set_skin_vars('vod2title9', ADDON.getSetting('vod2title9')); _set_skin_vars('vod2path9', ADDON.getSetting('vod2path9')); _set_skin_vars('vod2thumb9', ADDON.getSetting('vod2thumb9'))
    if not ADDON.getSetting('vod2title10') == '': _set_skin_vars('vod2title10',ADDON.getSetting('vod2title10'));_set_skin_vars('vod2path10',ADDON.getSetting('vod2path10'));_set_skin_vars('vod2thumb10',ADDON.getSetting('vod2thumb10'))
    if not ADDON.getSetting('vod2title11') == '': _set_skin_vars('vod2title11',ADDON.getSetting('vod2title11'));_set_skin_vars('vod2path11',ADDON.getSetting('vod2path11'));_set_skin_vars('vod2thumb11',ADDON.getSetting('vod2thumb11'))
    if not ADDON.getSetting('vod2title12') == '': _set_skin_vars('vod2title12',ADDON.getSetting('vod2title12'));_set_skin_vars('vod2path12',ADDON.getSetting('vod2path12'));_set_skin_vars('vod2thumb12',ADDON.getSetting('vod2thumb12'))
    if not ADDON.getSetting('vod2title13') == '': _set_skin_vars('vod2title13',ADDON.getSetting('vod2title13'));_set_skin_vars('vod2path13',ADDON.getSetting('vod2path13'));_set_skin_vars('vod2thumb13',ADDON.getSetting('vod2thumb13'))
    if not ADDON.getSetting('vod2title14') == '': _set_skin_vars('vod2title14',ADDON.getSetting('vod2title14'));_set_skin_vars('vod2path14',ADDON.getSetting('vod2path14'));_set_skin_vars('vod2thumb14',ADDON.getSetting('vod2thumb14'))
    if not ADDON.getSetting('vod2title15') == '': _set_skin_vars('vod2title15',ADDON.getSetting('vod2title15'));_set_skin_vars('vod2path15',ADDON.getSetting('vod2path15'));_set_skin_vars('vod2thumb15',ADDON.getSetting('vod2thumb15'))


def _set_skin_vars(thevar,varset):
    xbmc.executebuiltin('SetProperty('+thevar+','+varset+',1100)')# 1100 sets the kodi default custom stuff window id you can maybe change it
################################################################################
# GUI - MAIN SET TVGFS SKIN SETTINGS - grabs from this addons settings.xml (if found) and copies them over to tvgfs
# THIS IS FOR INSTALLING THE SKIN NOT RUNNING IT #  A fancy way to set the skin dir and name while retaining a backups of your settings ;)
################################################################################
def _set_tvgfs_settings():
    if ADDON_TVGFS:
        if os.path.exists(skinPath):
            if ADDON.getSetting('run.minimal') == 'true':# Main set skin and is the minimal purpose of this gui
                ADDON_TVGFS.setSetting('skin.source', '2')
                #ADDON_TVGFS.setSetting('skin.folder', 'special://home/addons/'+ADDONID+'/')
                #ADDON_TVGFS.setSetting('skin.user', ADDON.getSetting('skin.user'))
                ADDON_TVGFS.setSetting('skin.folder', ADDON.getSetting('skin.folder'))
                ADDON_TVGFS.setSetting('skin.user', skin)
                #ADDON_TVGFS.setSetting('skin.user', SKINS[skin][1])
            if ADDON.getSetting('run.epg') == 'true' and not ADDON.getSetting('xmltv.url') == '':  # set epg path 30101
                ADDON_TVGFS.setSetting('xmltv.url', ADDON.getSetting('xmltv.url'))
                ADDON_TVGFS.setSetting('xmltv.type', '1')
                ADDON_TVGFS.setSetting('xmltv.url', ADDON.getSetting('xmltv.url'))
                ADDON_TVGFS.setSetting('gz', ADDON.getSetting('gz'))
                ADDON_TVGFS.setSetting('md5', ADDON.getSetting('md5'))
                ADDON_TVGFS.setSetting('xmltv.interval', ADDON.getSetting('xmltv.interval'))
                ADDON_TVGFS.setSetting('xmltv.offset', ADDON.getSetting('xmltv.offset'))
            if ADDON.getSetting('xmltv2.enabled') == 'true' and not ADDON.getSetting('xmltv2.url') == '':  # Lab3 Secondary XMLTV File
                ADDON_TVGFS.setSetting('xmltv2.url', ADDON.getSetting('xmltv2.url'))
                ADDON_TVGFS.setSetting('xmltv2.enabled', ADDON.getSetting('xmltv2.enabled'))
                ADDON_TVGFS.setSetting('xmltv2.type', ADDON.getSetting('xmltv2.type'))
                ADDON_TVGFS.setSetting('xmltv2.file', ADDON.getSetting('xmltv2.file'))
                ADDON_TVGFS.setSetting('xmltv2.url', ADDON.getSetting('xmltv2.url'))
                ADDON_TVGFS.setSetting('xmltv2.offset', ADDON.getSetting('xmltv2.offset'))
            if ADDON.getSetting('xmltv3.enabled') == 'true' and not ADDON.getSetting('xmltv3.url') == '':  # Lab3 third XMLTV File
                ADDON_TVGFS.setSetting('xmltv3.url', ADDON.getSetting('xmltv3.url'))
                ADDON_TVGFS.setSetting('xmltv3.enabled', ADDON.getSetting('xmltv3.enabled'))
                ADDON_TVGFS.setSetting('xmltv3.type', ADDON.getSetting('xmltv3.type'))
                ADDON_TVGFS.setSetting('xmltv3.file', ADDON.getSetting('xmltv3.file'))
                ADDON_TVGFS.setSetting('xmltv3.url', ADDON.getSetting('xmltv3.url'))
                ADDON_TVGFS.setSetting('xmltv3.offset', ADDON.getSetting('xmltv3.offset'))
            if ADDON.getSetting('categories.ini.enabled') == 'true':# categories ini
                ADDON_TVGFS.setSetting('categories.ini.enabled', ADDON.getSetting('categories.ini.enabled'))
                ADDON_TVGFS.setSetting('categories.ini.type', ADDON.getSetting('categories.ini.type'))
                if os.path.exists(xbmc.translatePath(os.path.join(ADDON.getSetting('categories.ini.file')))):
                    ADDON_TVGFS.setSetting('categories.ini.file', ADDON.getSetting('categories.ini.file'))
                else:
                    ADDON_TVGFS.setSetting('categories.ini.url', ADDON.getSetting('categories.ini.url'))
                ADDON_TVGFS.setSetting('categories.remember', ADDON.getSetting('categories.remember'))
                # Lab1
                ADDON_TVGFS.setSetting('cat.order', ADDON.getSetting('cat.order'))
                ADDON_TVGFS.setSetting('epg.subtitle', ADDON.getSetting('epg.subtitle'))
            if ADDON.getSetting('logos.enabled') == 'true':# set logos
                ADDON_TVGFS.setSetting('logos.source', ADDON.getSetting('logos.source'))
                ADDON_TVGFS.setSetting('logos.folder', ADDON.getSetting('logos.folder'))
                ADDON_TVGFS.setSetting('logos.url', ADDON.getSetting('logos.url'))
            if ADDON.getSetting('addons.ini.enabled') == 'true':# addon ini
                ADDON_TVGFS.setSetting('addons.ini.enabled', ADDON.getSetting('addons.ini.enabled'))
                ADDON_TVGFS.setSetting('addons.ini.file', ADDON.getSetting('addons.ini.file'))
            if ADDON.getSetting('run.playback') == 'true':# Playback
                ADDON_TVGFS.setSetting('m3u.read', ADDON.getSetting('m3u.read'))
                ADDON_TVGFS.setSetting('catchup.text', ADDON.getSetting('catchup.text'))
                ADDON_TVGFS.setSetting('channel.shortcut', ADDON.getSetting('channel.shortcut'))
                ADDON_TVGFS.setSetting('play.always.choose', ADDON.getSetting('play.always.choose'))
                ADDON_TVGFS.setSetting('play.alt.choose', ADDON.getSetting('play.alt.choose'))
                ADDON_TVGFS.setSetting('play.alt.continue', ADDON.getSetting('play.alt.continue'))
                ADDON_TVGFS.setSetting('stop.on.exit', ADDON.getSetting('stop.on.exit'))
                ADDON_TVGFS.setSetting('exit.on.back', ADDON.getSetting('exit.on.back'))
                ADDON_TVGFS.setSetting('mine1', ADDON.getSetting('mine1'))
            if ADDON.getSetting('run.appearance') == 'true':# set Appearance
                ADDON_TVGFS.setSetting('epg.video.pip', ADDON.getSetting('epg.video.pip'))
                ADDON_TVGFS.setSetting('program.image.scale', ADDON.getSetting('program.image.scale'))
                ADDON_TVGFS.setSetting('stream.addon.list', ADDON.getSetting('stream.addon.list'))
                ADDON_TVGFS.setSetting('up.cat.mode', ADDON.getSetting('up.cat.mode'))
                ADDON_TVGFS.setSetting('action.bar', ADDON.getSetting('action.bar'))
                ADDON_TVGFS.setSetting('down.action', ADDON.getSetting('down.action'))
                ADDON_TVGFS.setSetting('program.search.plot', ADDON.getSetting('program.search.plot'))
                ADDON_TVGFS.setSetting('channel.logo', ADDON.getSetting('channel.logo'))
                ADDON_TVGFS.setSetting('addon.logo', ADDON.getSetting('addon.logo'))
                ADDON_TVGFS.setSetting('channels.per.page', ADDON.getSetting('channels.per.page'))
                ADDON_TVGFS.setSetting('channel.filter.sort', ADDON.getSetting('channel.filter.sort'))
                ADDON_TVGFS.setSetting('menu.addon', ADDON.getSetting('menu.addon'))
            if ADDON.getSetting('run.background') == 'true':# Background
                ADDON_TVGFS.setSetting('program.background.enabled', ADDON.getSetting('program.background.enabled'))
                ADDON_TVGFS.setSetting('program.background.image.source', ADDON.getSetting('program.background.image.source'))
                #ADDON_TVGFS.setSetting('program.background.image', ADDON.getSetting('program.background.image'))
                ADDON_TVGFS.setSetting('program.background.color', ADDON.getSetting('program.background.color'))
                ADDON_TVGFS.setSetting('program.background.flat', ADDON.getSetting('program.background.flat'))
                ADDON_TVGFS.setSetting('timebar.color', ADDON.getSetting('timebar.color'))
                ADDON_TVGFS.setSetting('categories.background.color', ADDON.getSetting('categories.background.color'))
            if ADDON.getSetting('run.backgroundimage') == 'true' and os.path.exists(xbmc.translatePath(os.path.join(ADDON.getSetting('program.background.image')))):# Background image
                ADDON_TVGFS.setSetting('program.background.enabled', ADDON.getSetting('program.background.enabled'))
                ADDON_TVGFS.setSetting('program.background.image.source', ADDON.getSetting('program.background.image.source'))
                ADDON_TVGFS.setSetting('program.background.image', ADDON.getSetting('program.background.image'))
                ADDON_TVGFS.setSetting('program.background.color', ADDON.getSetting('program.background.color'))
                ADDON_TVGFS.setSetting('program.background.flat', ADDON.getSetting('program.background.flat'))
                ADDON_TVGFS.setSetting('timebar.color', ADDON.getSetting('timebar.color'))
                ADDON_TVGFS.setSetting('categories.background.color', ADDON.getSetting('categories.background.color'))
            # post install
            if ADDON.getSetting('var.flip_vertical') == 'true': toggle_vertical()
            if ADDON.getSetting('var.flip_horizontal') == 'true':  toggle_horizontal()
            skinchangelog  = xbmc.translatePath(os.path.join(skinPath,'changelog.txt'))
            if os.path.exists(skinchangelog):
                gui_helpMenu(skinchangelog)
            if ADDON.getSetting('run.refresh') == 'true': refresh_ini()
            else: 
                if dialog.yesno(ADDONID_TVGFS, "Would you like to open %s?" % ADDONID_TVGFS, yeslabel="[B][COLOR green]Yes[/COLOR][/B]", nolabel="[B][COLOR red]No Skip[/COLOR][/B]"):_reopen()
        else: xbmcgui.Dialog().notification('ERROR', 'Skin Not Found', ICON, 1000, False)
def gui_set_tvgfs_settings():
    class firstRun(xbmcgui.WindowXMLDialog):
        def __init__(self,*args,**kwargs):
            print ''
        def onInit(self):
            set_skin_vars()
            try: copy_failsafes()
            except: pass
            self.title      = 101
            self.okbutton   = 201;self.ignore = 202;self.runit = 203;self.extra1 = 204;self.extra2 = 205;self.extra3 = 206
            self.first      = 301;self.two = 302;self.three = 303;self.four = 304;self.five = 305;self.six = 306;self.seven = 307;self.eight = 308;self.nine = 309;self.ten = 310;self.eleven = 311;self.twelve = 312;self.thirteen = 313;self.fourteen = 314
            self.firsthelp  = 401;self.twohelp = 402;self.threehelp = 403;self.fourhelp = 404;self.fivehelp = 405;self.sixhelp = 406;self.sevenhelp = 407;self.eighthelp = 408;self.ninehelp = 409;self.tenhelp = 410;self.elevenhelp = 411;self.twelvehelp = 412;self.thirteenhelp = 413;self.fourteenhelp = 414
            self.old1       = 501;self.old2 = 502;self.old3 = 503;self.old4 = 504;self.old5 = 505;self.old6 = 506;self.old7 = 507;self.old8 = 508
            self.showdialog()
            # dont edit these
            self.controllist = [self.first, self.two, self.three, self.four, self.five, self.six, self.seven, self.eight, self.nine, self.ten, self.eleven, self.twelve, self.thirteen, self.fourteen]
            # step 1 of 2 - enter the respective settings id order or leave blank
            self.controlsettings = ['run.minimal','run.epg','xmltv2.enabled','xmltv3.enabled',
            'addons.ini.enabled',
            'categories.ini.enabled',
            'logos.enabled',
            'run.playback',
            'run.appearance',
            'run.background',
            'run.backgroundimage',
            'var.flip_vertical',
            'var.flip_horizontal',
            'run.refresh']
            for item in self.controllist:
                if ADDON.getSetting(self.controlsettings[self.controllist.index(item)]) == 'true': self.getControl(item).setSelected(True)
        def showdialog(self):
            self.getControl(self.title).setLabel('Install [COLOR yellow]'+skin+'[/COLOR]')
            # tvgfs current settings
            self.getControl(self.old1).setLabel('[COLOR=blue]xmltv.xml  ●[/COLOR] '+ADDON_TVGFS.getSetting('xmltv.url')+'  '+ADDON_TVGFS.getSetting('xmltv.file'))
            self.getControl(self.old2).setLabel('[COLOR=blue]xmltv2.xml ●[/COLOR] '+ADDON_TVGFS.getSetting('xmltv2.enabled')+'  '+ADDON_TVGFS.getSetting('xmltv2.url')+'  '+ADDON_TVGFS.getSetting('xmltv2.file'))
            self.getControl(self.old3).setLabel('[COLOR=blue]xmltv3.xml ●[/COLOR] '+ADDON_TVGFS.getSetting('xmltv3.enabled')+'  '+ADDON_TVGFS.getSetting('xmltv3.url')+'  '+ADDON_TVGFS.getSetting('xmltv3.file'))
            self.getControl(self.old4).setLabel('[COLOR=blue]Logos ●[/COLOR] '+    ADDON_TVGFS.getSetting('logos.enabled')+' | [COLOR=blue]Folder ●[/COLOR] '+ADDON_TVGFS.getSetting('logos.folder')+' | [COLOR=blue]url ●[/COLOR] '+ADDON_TVGFS.getSetting('logos.url'))
            self.getControl(self.old5).setLabel('[COLOR=blue]User skin ●[/COLOR] '+ADDON_TVGFS.getSetting('skin.user')+' | [COLOR=blue]Skin ●[/COLOR] '+ADDON_TVGFS.getSetting('skin')+' | [COLOR=blue]Background ●[/COLOR] '+ADDON_TVGFS.getSetting('program.background.color')+' | [COLOR=blue]addons.ini ●[/COLOR] '+ADDON_TVGFS.getSetting('addons.ini.enabled')+' | [COLOR=blue]addons.ini ●[/COLOR] '+ADDON_TVGFS.getSetting('addons.ini.enabled')+' | [COLOR=blue]Categories ●[/COLOR] '+ADDON_TVGFS.getSetting('categories.ini.enabled')+' | [COLOR=blue]ini subscriptions ●[/COLOR] '+ADDON_TVGFS.getSetting('addons.ini.subscriptions')+' | [COLOR=blue]mapping.ini ●[/COLOR] '+ADDON_TVGFS.getSetting('mapping.ini.enabled')+' | '+ADDON_TVGFS.getSetting('mapping.m3u.enabled'))
            self.getControl(self.old6).setLabel('')
            self.getControl(self.old7).setLabel('')
            self.getControl(self.old8).setLabel('')
            #
            # step 2 of 2 - enter the respective help tag order or leave blank
            yup  = 'olive'
            nope  = 'red'
            color1 = yup if os.path.exists(skinPath) else nope
            self.getControl(self.first).setLabel('[COLOR=blue]Install:[/COLOR]   "[COLOR yellow]'+skin+'[/COLOR]" Skin  (Minimal)');
            self.getControl(self.firsthelp).setLabel('[COLOR=%s]%s[/COLOR]' % (color1,skinPath))
            
            self.getControl(self.two).setLabel('[COLOR=blue]Set:[/COLOR]  Use xmltv.xml (Default)')
            self.getControl(self.twohelp).setLabel('[COLOR=blue]xmltv.xml  ●[/COLOR] '+ADDON.getSetting('xmltv.url'))
            self.getControl(self.three).setLabel('[COLOR=blue]Set:[/COLOR]  Use xmltv2.xml (Multi)')
            self.getControl(self.threehelp).setLabel('[COLOR=blue]xmltv2.xml ●[/COLOR] '+ADDON.getSetting('xmltv2.url'))
            self.getControl(self.four).setLabel('[COLOR=blue]Set:[/COLOR]  Use xmltv3.xml (Multi)')
            self.getControl(self.fourhelp).setLabel('[COLOR=blue]xmltv3.xml ●[/COLOR] '+ADDON.getSetting('xmltv3.url'))
            
            #color5 = yup if os.path.exists(ADDON.getSetting('addons.ini.file')) else nope
            color5 = yup if os.path.exists(xbmc.translatePath(os.path.join(ADDON.getSetting('addons.ini.file')))) else nope
            self.getControl(self.five).setLabel('[COLOR=blue]Import:[/COLOR]  addons.ini')
            self.getControl(self.fivehelp).setLabel('[COLOR=blue]'+ADDON.getSetting('addons.ini.enabled')+'[/COLOR] ● '+ADDON.getSetting('addons.ini.url')+' | [COLOR='+color5+']'+ADDON.getSetting('addons.ini.file')+'[/COLOR]')

            #color6 = yup if os.path.exists(ADDON.getSetting('categories.ini.file')) else nope
            color6 = yup if os.path.exists(xbmc.translatePath(os.path.join(ADDON.getSetting('categories.ini.file')))) else nope
            self.getControl(self.six).setLabel('[COLOR=blue]Import:[/COLOR]  categories.ini')
            self.getControl(self.sixhelp).setLabel('[COLOR=blue]'+ADDON.getSetting('categories.ini.enabled')+'[/COLOR] ● '+ADDON.getSetting('categories.ini.url')+' | [COLOR='+color6+']'+ADDON.getSetting('categories.ini.file')+'[/COLOR]')

            #color7 = yup if os.path.exists(ADDON.getSetting('categories.ini.file')) else nope
            color7 = yup if os.path.exists(xbmc.translatePath(os.path.join(ADDON.getSetting('logos.folder')))) else nope
            self.getControl(self.seven).setLabel('[COLOR=blue]Import:[/COLOR]  Logos')
            self.getControl(self.sevenhelp).setLabel('[COLOR=blue]'+ADDON.getSetting('logos.enabled')+'[/COLOR] ● '+ADDON.getSetting('logos.url')+' | [COLOR='+color7+']'+ADDON.getSetting('logos.folder')+'[/COLOR]')

            self.getControl(self.eight).setLabel('[COLOR=blue]Set:[/COLOR]  Playback Tweaks')
            self.getControl(self.eighthelp).setLabel('[COLOR=blue]Krypton+ fix ●[/COLOR] '+ADDON.getSetting('m3u.read')+' | [COLOR=blue]Meta ●[/COLOR] '+ADDON.getSetting('catchup.text')+' | [COLOR=blue]Always choose channel ●[/COLOR] '+ADDON.getSetting('play.always.choose')+' | [COLOR=blue]Alt channels ●[/COLOR] '+ADDON.getSetting('play.alt.choose'))

            self.getControl(self.nine).setLabel('[COLOR=blue]Set:[/COLOR]  Appearance and Navigation')
            self.getControl(self.ninehelp).setLabel('[COLOR=blue]Columns ●[/COLOR] '+ADDON.getSetting('channels.per.page')+' | [COLOR=blue]Up to Categories ●[/COLOR] '+ADDON.getSetting('up.cat.mode')+' | [COLOR=blue]Show ActionBar ●[/COLOR] '+ADDON.getSetting('action.bar')+' | [COLOR=blue]Down to ActionBar ●[/COLOR] '+ADDON.getSetting('down.action')+' | [COLOR=blue]PIP ●[/COLOR] '+ADDON.getSetting('epg.video.pip'))

            self.getControl(self.ten).setLabel('[COLOR=blue]Set:[/COLOR]  Background Color (Defaults)')
            self.getControl(self.tenhelp).setLabel('[COLOR=blue]'+ADDON.getSetting('program.background.enabled')+'[/COLOR] | Background ● '+ADDON.getSetting('program.background.color')+' | Flat Background Image ● '+ADDON.getSetting('program.background.flat')+' | Categories ● '+ADDON.getSetting('categories.background.color')+' | Timebar ● '+ADDON.getSetting('timebar.color'))

            #color11 = yup if os.path.exists(ADDON.getSetting('program.background.image')) else nope
            color11 = yup if os.path.exists(xbmc.translatePath(os.path.join(ADDON.getSetting('program.background.image')))) else nope
            self.getControl(self.eleven).setLabel('[COLOR=blue]Set:[/COLOR]  Background Image')
            self.getControl(self.elevenhelp).setLabel('[COLOR=blue]Image ●[/COLOR]  [COLOR='+color11+']'+ADDON.getSetting('program.background.image')+'[/COLOR]')

            self.getControl(self.twelve).setLabel('[COLOR=dimgrey]Skin Co-ordinates:[/COLOR]  Flip Vertical')
            self.getControl(self.twelvehelp).setLabel('[COLOR=blue]'+ADDON.getSetting('var.flip_vertical')+'  ●[/COLOR]  VERTICAL | Flip the Description area with the channel columns')
            self.getControl(self.thirteen).setLabel('[COLOR=dimgrey]Skin Co-ordinates:[/COLOR]  Flip Horizontal')
            self.getControl(self.thirteenhelp).setLabel('[COLOR=blue]'+ADDON.getSetting('var.flip_horizontal')+'  ●[/COLOR]  HORIZONTAL | Flip the Description area with the videowindow and program image')
            
            is_refreshaddon = '[COLOR=lime]TVGFS folders.list Present[/COLOR] ● It is reccommended to refresh your channels periodically and on first run' if os.path.exists(xbmc.translatePath(os.path.join(basePath_tvgfs, 'folders.list'))) else 'Go into StreamSetup and slect addon subscriptions.'
            self.getControl(self.fourteen).setLabel('[COLOR=dimgrey]Optional[/COLOR]  Refresh Addon folders.list')
            self.getControl(self.fourteenhelp).setLabel(is_refreshaddon)
            self.setFocus(self.getControl(self.okbutton))
        def doAddonMenu(self):
            self.close()
            gui_run_extras()
            #url = 'plugin://%s/?mode=test' % ADDONID
            #url = 'plugin://%s/' % ADDONID_TVGFS
            #xbmc.executebuiltin('ActivateWindow(10025, "%s", return)' % url)
        def doIgnore(self):
            self.close()
        def doExtra1(self): # choose skin
            fileroot =xbmc.translatePath(os.path.join(ADDON.getSetting('skin.folder'),'resources','skins'))
            browse_dialog = xbmcgui.Dialog()
            folder = browse_dialog.browse(type=0, heading='Select Skin', shares='files', mask='/', useThumbs=False, treatAsFolder=True, defaultt=fileroot, enableMultiple=False)
            if not os.path.exists(xbmc.translatePath(os.path.join(folder,'media'))): return
            foldername = os.path.split(folder[:-1])[1]
            ADDON.setSetting('skin.user',foldername)
            ADDON_TVGFS.setSetting('skin.user',foldername)
            self.close();_open_addon(ADDONID)
        def doExtra2(self): # open skin settings
            _open_setting(ADDONID)
        def doExtra3(self):# open tvgfs settings
            _open_setting(ADDONID_TVGFS)
        def onClick(self, controlId):
            if controlId == self.okbutton:
                self.close()
                for item in self.controllist:
                    at = self.controllist.index(item)
                    if self.getControl(item).isSelected():
                         ADDON.setSetting(self.controlsettings[at], 'true')
                    else:
                        ADDON.setSetting(self.controlsettings[at], 'false')
                _set_tvgfs_settings()
            elif controlId == self.ignore: self.doIgnore()
            elif controlId == self.runit:  self.doAddonMenu()
            elif controlId == self.extra1: self.doExtra1()
            elif controlId == self.extra2: self.doExtra2()
            elif controlId == self.extra3: self.doExtra3()
    fr = firstRun('SetSettings.xml',ADDON.getAddonInfo('path'), installerskin, current='true')
    fr.doModal()
    del fr
def toggle_skin():
    fileroot =xbmc.translatePath(os.path.join(ADDON.getSetting('skin.folder'),'resources','skins'))
    browse_dialog = xbmcgui.Dialog()
    folder = browse_dialog.browse(type=0, heading='Select Skin', shares='files', mask='/', useThumbs=False, treatAsFolder=True, defaultt=fileroot, enableMultiple=False)
    #file = browse_dialog.browse(type=1, heading='Select File', shares='files', mask='.apk', useThumbs=False, treatAsFolder=False, defaultt=fileroot, enableMultiple=False)
    if not os.path.exists(xbmc.translatePath(os.path.join(folder,'media'))): return
    foldername = os.path.split(folder[:-1])[1]
    ADDON.setSetting('skin.user',foldername)
    ADDON_TVGFS.setSetting('skin.user',foldername)
    _reopen()
################################################################################
# GUI - MENU2 RUN EXTRA COMMANDS SHORTCUT - MAIN MENU2
################################################################################
def gui_run_extras():
    openset = dialog.select('Open Setting', ['Play from addons.ini File',
    'Refresh ini Files and Subscriptions',
    'Open Settings  ●  '+ADDONID,
    'Open Settings  ●  '+ADDONID_TVGFS,
    '[COLOR blue]GUI[/COLOR]  ●  Reset Database',
    '[COLOR blue]GUI[/COLOR]  ●  Help',
    '[COLOR blue]GUI[/COLOR]  ●  Toggle TVGFS Settings',
    '[COLOR blue]GUI[/COLOR]  ●  TVGFS Maintenance',
    '[COLOR blue]GUI[/COLOR]  ●  View Log ● XML',
    '[COLOR blue]GUI[/COLOR]  ●  Install Skin',
    '[COLOR blue]GUI[/COLOR]  ●  Play .M3U',
    '[COLOR blue]GUI[/COLOR]  ●  advancedsettings.xml',
    '[COLOR blue]GUI[/COLOR]  ●  playerfactorycore.xml',
    '[COLOR blue]GUI[/COLOR]  ●  Calibration Pics',
    'Open settings.xml with Notepad (Windows)',
    'Enable all Addons'])
    if openset == 0:  ini_browse()
    if openset == 1:  refresh_ini()#;_reopen()
    if openset == 2:  _open_setting(ADDONID)
    if openset == 3:  _open_setting(ADDONID_TVGFS)
    if openset == 4:  gui_resetdatabase()
    if openset == 5:  gui_helpMenu()
    if openset == 6:  gui_toggle_settings()
    if openset == 7:  gui_tvgfsmaintenence()
    if openset == 8:  gui_LogViewer()
    if openset == 9:  gui_set_tvgfs_settings()
    if openset == 10: gui_playm3u()
    if openset == 11: gui_autoConfig()
    if openset == 12: _writeplayerfactorycore()
    if openset == 13: gui_show_calibrate()
    if openset == 14: _run_exe('C:/Windows/System32/notepad.exe', xbmc.translatePath(os.path.join(addonPath, 'resources', 'settings.xml')))
    if openset == 15: _enable()
def _open_setting(thisADDONID):
    xbmc.executebuiltin('XBMC.ActivateWindow(home)')
    try:  xbmcaddon.Addon(id=thisADDONID).openSettings()
    except: pass
def _open_addon(thisADDONID):
    xbmc.executebuiltin('XBMC.ActivateWindow(home)')
    xbmc.sleep(350)
    try:  xbmc.executebuiltin("RunAddon("+thisADDONID+")")
    except: pass
def refresh_ini():
    if os.path.exists(refreshaddon): xbmc.executebuiltin('RunScript('+refreshaddon+')')
    if not os.path.exists(refreshaddon): xbmc.executebuiltin('RunScript('+refreshaddon2+')')
def gui_show_calibrate(): # test patterns
    browse_dialog = xbmcgui.Dialog()
    picturefile = browse_dialog.browse(type=1, heading='Choose Calibration Pic', shares='files', mask='.png|.jpg|.jpeg', useThumbs=False, treatAsFolder=False, defaultt=calibrate, enableMultiple=False)
    if not os.path.exists(picturefile): return
    thisfadefile = os.path.split(picturefile[:])[1]
    xbmc.executebuiltin('ShowPicture(%s)' % picturefile)
def _run_exe(name=None, url=None):# wip
    from subprocess import call
    from subprocess import Popen
    if os.path.exists(name):
        cmd = [name, url]
        #cmd = [ffmpeg, "-y", "-i", url, "-c:v", "copy", "-c:a", "copy", "-t", str(seconds), "-f", "mpegts", "-map", "0:v", "-map", "0:a", filename]
        #cmd = [ffmpeg, "-y", "-i", url, "-c:v", "copy", "-c:a", "copy", "-t", str(seconds), filename]
        #p = Popen(cmd,shell=True) # has NO cmd window info prompt
        p = Popen(cmd,shell=False) # has cmd window info prompt
def _enable(): # enable addons
    from sqlite3 import dbapi2 as db_lib
    db_path = xbmc.translatePath(os.path.join('special://home/','userdata','Database','Addons27.db'))
    conn = db_lib.connect(db_path)
    conn.text_factory = str
    KODIV  = float(xbmc.getInfoLabel("System.BuildVersion")[:4])
    if KODIV >= 17:
        dialog.notification("Enable","Enabling All Addons",sound=False)
        contents = os.listdir(xbmc.translatePath(os.path.join('special://home/','addons')))
        conn.executemany('update installed set enabled=1 WHERE addonID = (?)', ((val,) for val in contents))
        conn.commit()
    else: pass
def gui_helpMenu(url=None):
    if url == None:
        browse_dialog = xbmcgui.Dialog()
        url = browse_dialog.browse(type=1, heading='Select File', shares='files', mask='.txt', useThumbs=False, treatAsFolder=False, defaultt=helpdir, enableMultiple=False)
        if not os.path.exists(url): return
    if os.path.exists(url):
        name2 =  os.path.basename(url)
        f = xbmcvfs.File(url,'rb')
        data = f.read()
        dialog = xbmcgui.Dialog()
        dialog.textviewer(name2, data)
def gui_playm3u(playlistFile=None):
    browse_dialog = xbmcgui.Dialog()
    playlistFile = browse_dialog.browse(type=1, heading='Choose m3u', shares='files', mask='.m3u|.m3u8|.strm|.html|.xps', useThumbs=False, treatAsFolder=False, defaultt=ADDON.getSetting('var.xps_playlists'), enableMultiple=False)
    xbmc.executebuiltin('ActivateWindow(10025,'+playlistFile+',return)')
def gui_tvgfsmaintenence():
    #addonPath_tvgfs      = xbmc.translatePath(os.path.join('special://home', 'addons', ADDONID_TVGFS))
    opentvgfspy = dialog.select('WIP TVGFS Maintenance', ['Manage addons.ini m3u Playlist Subscriptions',
    'Mangage Catchup Urls',
    'Shortcut Editor (run the guide once)',
    'Action Editor',
    'Clear Channel Mappings',
    'Export Channel Mappings',
    'Import Channel Mappings',
    'Clear Alternative Channel Mappings',
    'Export Alternative Channel Mappings',
    'Import Alternative Channel Mappings',
    'Download All Addon Folder Logos',
    'Download All Channel Logos',
     ])
    if opentvgfspy == 0:  _tvgfsmaintenence('subscriptions.py', arg=None)
    if opentvgfspy == 1:  _tvgfsmaintenence('catchup.py', arg=None)
    if opentvgfspy == 2:  _tvgfsmaintenence('ShortcutEditor.py', arg=None)
    if opentvgfspy == 3:  _tvgfsmaintenence('ActionEditor.py', arg=None)
    if opentvgfspy == 4:  _tvgfsmaintenence('backup.py', '5')
    if opentvgfspy == 5:  _tvgfsmaintenence('backup.py', '1')
    if opentvgfspy == 6:  _tvgfsmaintenence('backup.py', '2')
    if opentvgfspy == 7:  _tvgfsmaintenence('backup.py', '6')
    if opentvgfspy == 8:  _tvgfsmaintenence('backup.py', '3')
    if opentvgfspy == 9:  _tvgfsmaintenence('backup.py', '4')
    if opentvgfspy == 10: _tvgfsmaintenence('logos.py', arg=None)
    if opentvgfspy == 11: _tvgfsmaintenence('channel_logos.py', arg=None)
def _tvgfsmaintenence(script, arg=None):
    scriptpath = xbmc.translatePath(os.path.join(addonPath_tvgfs, script))
    if arg == None:
        if os.path.exists(scriptpath): xbmc.executebuiltin('RunScript('+scriptpath+')')
    else:
        if os.path.exists(scriptpath): xbmc.executebuiltin('RunScript('+scriptpath+','+arg+')')
################################################################################
# GUI - MENU Toggle TVGFS Settings on the fly and custom skin mods
################################################################################
def gui_toggle_settings():
    togglechoice = dialog.select('Toggle TVGFS Settings   (These will re-open TVGFS)', ['[COLOR blue]'+ADDON_TVGFS.getSetting('epg.video.pip')+'[/COLOR]  ●  Image as a background (false is Video Background)',
    '[COLOR blue]'+ADDON_TVGFS.getSetting('play.always.choose')+'[/COLOR]  ●  Always choose channel',
    '[COLOR blue]'+ADDON_TVGFS.getSetting('stream.addon.list')+'[/COLOR]  ●  List View for Choose Stream',
    '[COLOR blue]'+ADDON_TVGFS.getSetting('logos.enabled')+'[/COLOR]  ●  Channel logo icons',
    '[COLOR blue]'+ADDON_TVGFS.getSetting('channels.per.page')+'[/COLOR]  ●  Colums (Channels per page)',
    '[COLOR blue]'+ADDON_TVGFS.getSetting('skin.user')+'[/COLOR]  ●  Change Skin',
    '[COLOR blue]'+ADDON_TVGFS.getSetting('help.invisiblebuttons')+'[/COLOR]  ●  Enable Help Overlay',
    '[COLOR blue]'+ADDON.getSetting('var.flip_vertical')+'[/COLOR]  ●  (Vertical) Flip description with epg',
    '[COLOR blue]'+ADDON.getSetting('var.flip_horizontal')+'[/COLOR]  ●  (Horizontal) Flip videowindow with description',
    '[COLOR blue]'+ADDON.getSetting('var.image_fade')+'[/COLOR]  ●  Gamma Black Level (Darkness fade)',
    '[COLOR blue]'+ADDON.getSetting('var.image_fadebg')+'[/COLOR]  ●  Gamma Black Level Backgrounds (Darkness fade)',
    '[COLOR blue]'+ADDON.getSetting('var.image_fadewhite')+'[/COLOR]  ●  Gamma White Level (Color Diffuse)',
    '[COLOR blue]'+ADDON.getSetting('var.image_fadewhitebg')+'[/COLOR]  ●  Gamma White Level Backgrounds (Color Diffuse)',
    '[COLOR blue]'+ADDON_TVGFS.getSetting('program.background.color')+'[/COLOR]  ●  Background color',
    '[COLOR blue]'+ADDON_TVGFS.getSetting('categories.background.color')+'[/COLOR]  ●  Catbar color',
    '[COLOR blue]'+rez+'[/COLOR]  ●  1080p  (Experimental)',
    '[COLOR red]CAUTION[/COLOR]  ●  16 to 17 toggle (No Guarantees)'])
    if togglechoice == 0:  xbmcgui.Dialog().notification('Toggle', 'PIP Video Background', ICON, 1000, False); _togglesetting_tvgfs('epg.video.pip')
    if togglechoice == 1:  xbmcgui.Dialog().notification('Toggle', 'Channel Choose', ICON, 1000, False); _togglesetting_tvgfs('play.always.choose')
    if togglechoice == 2:  xbmcgui.Dialog().notification('Toggle', 'List View for Choose Stream', ICON, 1000, False); _togglesetting_tvgfs('stream.addon.list')
    if togglechoice == 3:  xbmcgui.Dialog().notification('Toggle', 'Logos', ICON, 1000, False); _togglesetting_tvgfs('logos.enabled')
    if togglechoice == 4:  xbmcgui.Dialog().notification('Toggle', 'Colums', ICON, 1000, False); gui_colums_toggle()# channels.per.page
    if togglechoice == 5:  xbmcgui.Dialog().notification('Toggle', 'New Skin', ICON, 1000, False); toggle_skin()# channels.per.page
    if togglechoice == 6:  xbmcgui.Dialog().notification('Toggle', 'Help', ICON, 1000, False); _set_skin_vars('help_toggle','true')# invisible buttons
    if togglechoice == 7:  toggle_vertical();_reopen()# var.flip_vertical
    if togglechoice == 8:  toggle_horizontal()#;_reopen()# var.flip_horizontal
    if togglechoice == 9:  xbmcgui.Dialog().notification('Toggle', 'Gamma Black', ICON, 1000, False); gui_fade_toggle()# var.image_fade
    if togglechoice == 10: xbmcgui.Dialog().notification('Toggle', 'Gamma Black  Background', ICON, 1000, False); gui_fadebg_toggle()# var.image_fadebg
    if togglechoice == 11: xbmcgui.Dialog().notification('Toggle', 'Gamma White', ICON, 1000, False); gui_fadewhite_toggle()# var.image_fade
    if togglechoice == 12: xbmcgui.Dialog().notification('Toggle', 'Gamma White  Background', ICON, 1000, False); gui_fadewhitebg_toggle()# var.image_fadebg
    if togglechoice == 13: xbmcgui.Dialog().notification('Toggle', 'Background Color', ICON, 1000, False); gui_color_toggle('program.background.color')
    if togglechoice == 14: xbmcgui.Dialog().notification('Toggle', 'Cat Color', ICON, 1000, False); gui_color_toggle('categories.background.color')
    if togglechoice == 15: xbmcgui.Dialog().notification('Toggle', '1080i', ICON, 1000, False); toggle_1080();_reopen()# var.rez
    if togglechoice == 16: xbmcgui.Dialog().notification('Toggle', 'Jarvis Strings', ICON, 1000, False); toggle_jarvis_strings()
def gui_fade_toggle():
    browse_dialog = xbmcgui.Dialog()
    fadefile = browse_dialog.browse(type=1, heading='Choose the gamma level (Darkness)', shares='files', mask='.png', useThumbs=False, treatAsFolder=False, defaultt=fadepath, enableMultiple=False)
    if not os.path.exists(fadefile): return
    thisfadefile = os.path.split(fadefile[:])[1]
    ADDON.setSetting('var.image_fade', thisfadefile)
    _set_skin_vars('image_fade','fade/'+thisfadefile)
def gui_fadewhite_toggle():
    browse_dialog = xbmcgui.Dialog()
    fadewhitefile = browse_dialog.browse(type=1, heading='Choose the white gamma level (Color Diffuse)', shares='files', mask='.png', useThumbs=False, treatAsFolder=False, defaultt=fadewhitepath, enableMultiple=False)
    if not os.path.exists(fadewhitefile): return
    thisfadewhitefile = os.path.split(fadewhitefile[:])[1]
    ADDON.setSetting('var.image_fadewhite', thisfadewhitefile)
    _set_skin_vars('image_fadewhite','fadewhite/'+thisfadewhitefile)
def gui_fadebg_toggle():
    browse_dialog = xbmcgui.Dialog()
    fadebgfile = browse_dialog.browse(type=1, heading='Choose the gamma level for backgrounds (Darkness)', shares='files', mask='.png', useThumbs=False, treatAsFolder=False, defaultt=fadepath, enableMultiple=False)
    if not os.path.exists(fadebgfile): return
    thisfadebgfile = os.path.split(fadebgfile[:])[1]
    ADDON.setSetting('var.image_fadebg', thisfadebgfile)
    _set_skin_vars('image_fadebg','fade/'+thisfadebgfile)
def gui_fadewhitebg_toggle():
    browse_dialog = xbmcgui.Dialog()
    fadewhitebgfile = browse_dialog.browse(type=1, heading='Choose the white gamma level for backgrounds (Color Diffuse)', shares='files', mask='.png', useThumbs=False, treatAsFolder=False, defaultt=fadewhitepath, enableMultiple=False)
    if not os.path.exists(fadewhitebgfile): return
    thisfadewhitebgfile = os.path.split(fadewhitebgfile[:])[1]
    ADDON.setSetting('var.image_fadewhitebg', thisfadewhitebgfile)
    _set_skin_vars('image_fadewhitebg','fadewhite/'+thisfadewhitebgfile)
def _togglesetting_tvgfs(toggletvgfs):
    if ADDON_TVGFS.getSetting(toggletvgfs) == 'false': ADDON_TVGFS.setSetting(toggletvgfs, 'true')
    elif ADDON_TVGFS.getSetting(toggletvgfs) == 'true': ADDON_TVGFS.setSetting(toggletvgfs, 'false')
    _reopen()
def _togglesetting(togglethis):
    if ADDON.getSetting(togglethis) == 'false': ADDON.setSetting(togglethis, 'true')
    elif ADDON.getSetting(togglethis) == 'true': ADDON.setSetting(togglethis, 'false')
def gui_colums_toggle():
    choicecolum = dialog.select('Choose number of PG rows', ['[COLOR yellow]Close[/COLOR]','12','16','15','14','13','11','10','9','8'])
    if choicecolum == 0: sys.close(0)
    if choicecolum == 1: ADDON_TVGFS.setSetting('channels.per.page', '12');_reopen()
    if choicecolum == 2: ADDON_TVGFS.setSetting('channels.per.page', '16');_reopen()
    if choicecolum == 3: ADDON_TVGFS.setSetting('channels.per.page', '15');_reopen()
    if choicecolum == 4: ADDON_TVGFS.setSetting('channels.per.page', '14');_reopen()
    if choicecolum == 5: ADDON_TVGFS.setSetting('channels.per.page', '13');_reopen()
    if choicecolum == 6: ADDON_TVGFS.setSetting('channels.per.page', '11');_reopen()
    if choicecolum == 7: ADDON_TVGFS.setSetting('channels.per.page', '10');_reopen()
    if choicecolum == 8: ADDON_TVGFS.setSetting('channels.per.page', '9');_reopen()
    if choicecolum == 9: ADDON_TVGFS.setSetting('channels.per.page', '8');_reopen()
def gui_color_toggle(thissetting):
    color_none = '[COLOR 00000000]none[/COLOR]';color_0 =  '[COLOR 00000000]transparent[/COLOR]'; color_1 = '[COLOR ff606060]black[/COLOR]';color_2 = '[COLOR ffffffff]white[/COLOR]';color_3 = '[COLOR fff5f5f5]whitesmoke[/COLOR]';color_4 = '[COLOR fffaebd7]antiquewhite[/COLOR]';color_5 = '[COLOR fffffff0]ivory[/COLOR]';color_6 = '[COLOR fffffafa]snow[/COLOR]';color_7 = '[COLOR fff5f5dc]beige[/COLOR]';color_8 = '[COLOR fffffaf0]floralwhite[/COLOR]';color_9 = '[COLOR fff8f8ff]ghostwhite[/COLOR]';color_10 = '[COLOR ffffdead]navajowhite[/COLOR]'
    color_11 =  '[COLOR ff808080]grey[/COLOR]';color_12 = '[COLOR ffc0c0c0]silver[/COLOR]';color_13 = '[COLOR ffa9a9a9]darkgrey[/COLOR]';color_14 = '[COLOR ff2f4f4f]darkslategrey[/COLOR]';color_15 = '[COLOR ff708090]slategrey[/COLOR]';color_16 = '[COLOR ff696969]dimgrey[/COLOR]';color_17 = '[COLOR ffd3d3d3]lightgrey[/COLOR]';color_18 = '[COLOR ff778899]lightslategrey[/COLOR]';color_19= '[COLOR ffdcdcdc]gainsboro[/COLOR]'
    color_20 =  '[COLOR ff0000ff]blue[/COLOR]';color_21 = '[COLOR ff4682b4]steelblue[/COLOR]';color_22 = '[COLOR ff87ceeb]skyblue[/COLOR]';color_23 = '[COLOR ff6a5acd]slateblue[/COLOR]';color_24 = '[COLOR ff00ffff]cyan[/COLOR]';color_25 = '[COLOR ff5f9ea0]cadetblue[/COLOR]';color_26 = '[COLOR ff00008b]darkblue[/COLOR]';color_27 = '[COLOR ff008b8b]darkcyan[/COLOR]';color_28 = '[COLOR ff483d8b]darkslateblue[/COLOR]';color_29 = '[COLOR ff9932cc]darkorchid[/COLOR]';
    color_30 =  '[COLOR ff483d8b]darkslateblue[/COLOR]';color_31 = '[COLOR ff00ced1]darkturquoise[/COLOR]';color_32 = '[COLOR ff00bfff]deepskyblue[/COLOR]';color_33 = '[COLOR ff1e90ff]dodgerblue[/COLOR]';color_34 = '[COLOR ff4169e1]royalblue[/COLOR]';color_35 = '[COLOR ff000080]navy[/COLOR]';color_36 = '[COLOR ffe0ffff]lightcyan[/COLOR]';color_37 = '[COLOR ff8a2be2]blueviolet[/COLOR]';color_38 = '[COLOR fff0f8ff]aliceblue[/COLOR]';color_39 = '[COLOR ff7fffd4]aquamarine[/COLOR]';
    color_40 =  '[COLOR fff0ffff]azure[/COLOR]';color_41 = '[COLOR ff6495ed]cornflowerblue[/COLOR]';color_42 = '[COLOR ff191970]midnightblue[/COLOR]';color_43 = '[COLOR ff66cdaa]mediumaquamarine[/COLOR]';color_44 = '[COLOR ff0000cd]mediumblue[/COLOR]';color_45 = '[COLOR ffba55d3]mediumorchid[/COLOR]';color_46 = '[COLOR ff7b68ee]mediumslateblue[/COLOR]';color_47 = '[COLOR ffb0c4de]lightsteelblue[/COLOR]';color_48 = '[COLOR ffb0e0e6]powderblue[/COLOR]';color_49 = '[COLOR ffadd8e6]lightblue[/COLOR]';
    color_50 =  '[COLOR ff87cefa]lightskyblue[/COLOR]';color_51 = '[COLOR ff48d1cc]mediumturquoise[/COLOR]';color_52 = '[COLOR ff40e0d0]turquoise[/COLOR]';color_53 = '[COLOR ffe6e6fa]lavender[/COLOR]';color_54 = '[COLOR fffff0f5]lavenderblush[/COLOR]';color_55 = '[COLOR fffff5ee]seashell[/COLOR]';color_56 = '[COLOR ff008080]teal[/COLOR]';color_57 = '[COLOR ffff7f50]coral[/COLOR]';color_58 = '[COLOR fff08080]lightcoral[/COLOR]';color_59 = '[COLOR ffafeeee]paleturquoise[/COLOR]';
    color_60 =  '[COLOR ffff0000]red[/COLOR]';color_61 = '[COLOR ffb22222]firebrick[/COLOR]';color_62 = '[COLOR ff8b0000]darkred[/COLOR]';color_63 = '[COLOR ffff6347]tomato[/COLOR]';color_64 = '[COLOR ffe9967a]darksalmon[/COLOR]';color_65 = '[COLOR ffffa07a]lightsalmon[/COLOR]';color_66 = '[COLOR ffdc143c]crimson[/COLOR]';color_67 = '[COLOR ff800000]maroon[/COLOR]';color_68 = '[COLOR ffcd5c5c]indianred[/COLOR]';color_69 = '[COLOR ffc71585]mediumvioletred[/COLOR]';
    color_70 =  '[COLOR ffdb7093]palevioletred[/COLOR]';color_71 = '[COLOR fffa8072]salmon[/COLOR]';color_72 = '[COLOR ffffc0cb]pink[/COLOR]';color_73 = '[COLOR ffffb6c1]lightpink[/COLOR]';color_74 = '[COLOR ffff69b4]hotpink[/COLOR]';color_75 = '[COLOR ffff1493]deeppink[/COLOR]';color_76 = '[COLOR ffffdab9]peachpuff[/COLOR]';color_77 = '[COLOR ffffe4e1]mistyrose[/COLOR]';color_78 = '';color_79 = ''
    color_80 =  '[COLOR ff008000]green[/COLOR]';color_81 = '[COLOR ff006400]darkgreen[/COLOR]';color_82 = '[COLOR ffbdb76b]darkkhaki[/COLOR]';color_83 = '[COLOR ff556b2f]darkolivegreen[/COLOR]';color_84 = '[COLOR ff228b22]forestgreen[/COLOR]';color_85 = '[COLOR ff8fbc8f]darkseagreen[/COLOR]';color_86 = '[COLOR ff7cfc00]lawngreen[/COLOR]';color_87 = '[COLOR ff3cb371]mediumseagreen[/COLOR]';color_88 = '[COLOR ff00fa9a]mediumspringgreen[/COLOR]';color_89 = '[COLOR ff98fb98]palegreen[/COLOR]';
    color_90 =  '[COLOR ff2e8b57]seagreen[/COLOR]';color_91 = '[COLOR ffadff2f]greenyellow[/COLOR]';color_92 = '[COLOR ff00ff7f]springgreen[/COLOR]';color_93 = '[COLOR ff808000]olive[/COLOR]';color_94 = '[COLOR ff6b8e23]olivedrab[/COLOR]';color_95 = '[COLOR ffbdb76b]darkkhaki[/COLOR]';color_96 = '[COLOR fff0e68c]khaki[/COLOR]';color_97 = '[COLOR ff00ff00]lime[/COLOR]';color_98 = '[COLOR ff90ee90]lightgreen[/COLOR]';color_99 = '[COLOR ff20b2aa]lightseagreen[/COLOR]';
    color_100 = '[COLOR ffa52a2a]brown[/COLOR]';color_101 = '[COLOR ffd2b48c]tan[/COLOR]';color_102 = '[COLOR ffd2691e]chocolate[/COLOR]';color_103 = '[COLOR ff8b4513]saddlebrown[/COLOR]';color_104 = '[COLOR fff4a460]sandybrown[/COLOR]';color_105 = '[COLOR ffbc8f8f]rosybrown[/COLOR]';color_106 = '[COLOR ffdeb887]burlywood[/COLOR]';color_107 = '[COLOR ffffebcd]blanchedalmond[/COLOR]';
    color_108 = '[COLOR ff800080]purple[/COLOR]';color_109 = '[COLOR ff9400d3]darkviolet[/COLOR]';color_110 = '[COLOR ff8b008b]darkmagenta[/COLOR]';color_111 = '[COLOR ff9370db]mediumpurple[/COLOR]';color_112 = '[COLOR ffdda0dd]plum[/COLOR]';color_113 = '[COLOR ffff00ff]magenta[/COLOR]';color_114 = '[COLOR ffee82ee]violet[/COLOR]';color_115 = '[COLOR ffda70d6]orchid[/COLOR]';color_116 = '[COLOR ff4b0082]indigo[/COLOR]';color_117 = '[COLOR ffd8bfd8]thistle[/COLOR]';color_118 = '';color_119 = '';
    color_120 = '[COLOR ffffff00]yellow[/COLOR]';color_121 = '[COLOR ffffffe0]lightyellow[/COLOR]';color_122 = '[COLOR fffffacd]lemonchiffon[/COLOR]';color_123 = '[COLOR ff9acd32]yellowgreen[/COLOR]';color_124 = '[COLOR ffffd700]gold[/COLOR]';color_125 = '[COLOR ffdaa520]goldenrod[/COLOR]';color_126 = '[COLOR ffb8860b]darkgoldenrod[/COLOR]';color_127 = '[COLOR fffafad2]lightgoldenrodyellow[/COLOR]';color_128 = '[COLOR ffeee8aa]palegoldenrod[/COLOR]';color_129 = '[COLOR fff5deb3]wheat[/COLOR]';
    color_130 = '[COLOR ffffa500]orange[/COLOR]';color_131 = '[COLOR ffff4500]orangered[/COLOR]';color_132 = '[COLOR ffff8c00]darkorange[/COLOR]';color_133 = '[COLOR ffffe4c4]bisque[/COLOR]';color_134 = '[COLOR fffaf0e6]linen[/COLOR]';color_135 = '[COLOR ffffe4b5]moccasin[/COLOR]';color_136 = '[COLOR fffdf5e6]oldlace[/COLOR]';color_137 = '[COLOR ffffefd5]papayawhip[/COLOR]';color_138 = '[COLOR ffcd853f]peru[/COLOR]';color_139 = '[COLOR ffa0522d]sienna[/COLOR]';color_140 = '[COLOR fffff8dc]cornsilk[/COLOR]';color_141 = '[COLOR fff0fff0]honeydew[/COLOR]';
    choicecolor__file = dialog.select('Choose Color for  '+thissetting, [color_0,color_1,color_2,color_21,color_61,color_15,color_94,color_22,color_25,'Blue','Grey','Green','Red','White','Brown','Purple','Yellow',])
    if choicecolor__file == 0: _toggle_color(color_0, thissetting)# transparent
    if choicecolor__file == 1: _toggle_color(color_1, thissetting)# black
    if choicecolor__file == 2: _toggle_color(color_2, thissetting)# white
    # favs
    if choicecolor__file == 3: _toggle_color(color_21, thissetting)#   steelblue
    if choicecolor__file == 4: _toggle_color(color_61, thissetting)#   firebrick
    if choicecolor__file == 5: _toggle_color(color_15, thissetting)#   slategrey
    if choicecolor__file == 6: _toggle_color(color_94, thissetting)#   olivedrab
    if choicecolor__file == 7: _toggle_color(color_22, thissetting)#   skyblue
    if choicecolor__file == 8: _toggle_color(color_25, thissetting)#   cadetblue
    #blue
    if choicecolor__file == 9: _toggle_color_gui(thissetting,color_21,color_20,color_22,color_23,color_24,color_25,color_26,color_27,color_28,color_29,color_30,color_31,color_32,color_33,color_34,color_35,color_36,color_37,color_38,color_39,color_40,color_41,color_42,color_43,color_44,color_45,color_46,color_47,color_48,color_49,color_50)
    #Grey
    if choicecolor__file == 10: _toggle_color_gui(thissetting,color_15,color_11,color_12,color_13,color_14,color_15,color_16,color_17,color_18,color_19,color_51,color_52,color_53,color_54,color_55,color_56,color_57,color_58,color_59,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0)
    #green
    if choicecolor__file == 11: _toggle_color_gui(thissetting,color_0,color_80,color_81,color_82,color_8,color_84,color_85,color_86,color_87,color_88,color_89,color_90,color_91,color_92,color_93,color_94,color_95,color_96,color_97,color_98,color_99,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0)
    #red
    if choicecolor__file == 12: _toggle_color_gui(thissetting,color_0,color_60,color_61,color_62,color_63,color_64,color_65,color_66,color_67,color_68,color_69,color_70,color_71,color_72,color_73,color_74,color_75,color_76,color_77,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0)
    #white
    if choicecolor__file == 13: _toggle_color_gui(thissetting,color_0,color_1,color_2,color_3,color_4,color_5,color_6,color_7,color_8,color_9,color_10,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0)
    #brown
    if choicecolor__file == 14: _toggle_color_gui(thissetting,color_0,color_100,color_101,color_102,color_103,color_104,color_105,color_106,color_107,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0)
    #purple
    if choicecolor__file == 15: _toggle_color_gui(thissetting,color_0,color_108,color_109,color_110,color_111,color_112,color_113,color_114,color_115,color_116,color_117,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0)
    #yellow
    if choicecolor__file == 16: _toggle_color_gui(thissetting,color_0,color_120,color_121,color_122,color_123,color_124,color_125,color_126,color_127,color_128,color_129,color_130,color_131,color_132,color_133,color_134,color_135,color_136,color_137,color_138,color_139,color_140,color_141,color_0,color_0,color_0,color_0,color_0,color_0,color_0,color_0)
def _toggle_color_gui(thissetting,menucolor_0,menucolor_1,menucolor_2,menucolor_3,menucolor_4,menucolor_5,menucolor_6,menucolor_7,menucolor_8,menucolor_9, menucolor_10,menucolor_11,menucolor_12,menucolor_13,menucolor_14,menucolor_15,menucolor_16,menucolor_17,menucolor_18,menucolor_19,menucolor_20,menucolor_21,menucolor_22,menucolor_23,menucolor_24,menucolor_25,menucolor_26,menucolor_27,menucolor_28,menucolor_29,menucolor_30):
    settogglecolor = dialog.select('Choose Color for  '+thissetting, [menucolor_0,menucolor_1,menucolor_2,menucolor_3,menucolor_4,menucolor_5,menucolor_6,menucolor_7,menucolor_8,menucolor_9, menucolor_10,menucolor_11,menucolor_12,menucolor_13,menucolor_14,menucolor_15,menucolor_16,menucolor_17,menucolor_18,menucolor_19,menucolor_20,menucolor_21,menucolor_22,menucolor_23,menucolor_24,menucolor_25,menucolor_26,menucolor_27,menucolor_28,menucolor_29,menucolor_30])
    if settogglecolor == 0: _toggle_color(menucolor_0, thissetting)
    if settogglecolor == 1: _toggle_color(menucolor_1, thissetting)
    if settogglecolor == 2: _toggle_color(menucolor_2, thissetting)
    if settogglecolor == 3: _toggle_color(menucolor_3, thissetting)
    if settogglecolor == 4: _toggle_color(menucolor_4, thissetting)
    if settogglecolor == 5: _toggle_color(menucolor_5, thissetting)
    if settogglecolor == 6: _toggle_color(menucolor_6, thissetting)
    if settogglecolor == 7: _toggle_color(menucolor_7, thissetting)
    if settogglecolor == 8: _toggle_color(menucolor_8, thissetting)
    if settogglecolor == 9: _toggle_color(menucolor_9, thissetting)
    if settogglecolor == 10: _toggle_color(menucolor_10, thissetting)
    if settogglecolor == 11: _toggle_color(menucolor_11, thissetting)
    if settogglecolor == 12: _toggle_color(menucolor_12, thissetting)
    if settogglecolor == 13: _toggle_color(menucolor_13, thissetting)
    if settogglecolor == 14: _toggle_color(menucolor_14, thissetting)
    if settogglecolor == 15: _toggle_color(menucolor_15, thissetting)
    if settogglecolor == 16: _toggle_color(menucolor_16, thissetting)
    if settogglecolor == 17: _toggle_color(menucolor_17, thissetting)
    if settogglecolor == 18: _toggle_color(menucolor_18, thissetting)
    if settogglecolor == 19: _toggle_color(menucolor_19, thissetting)
    if settogglecolor == 20: _toggle_color(menucolor_20, thissetting)
    if settogglecolor == 21: _toggle_color(menucolor_21, thissetting)
    if settogglecolor == 22: _toggle_color(menucolor_22, thissetting)
    if settogglecolor == 23: _toggle_color(menucolor_23, thissetting)
    if settogglecolor == 24: _toggle_color(menucolor_24, thissetting)
    if settogglecolor == 25: _toggle_color(menucolor_25, thissetting)
    if settogglecolor == 26: _toggle_color(menucolor_26, thissetting)
    if settogglecolor == 27: _toggle_color(menucolor_27, thissetting)
    if settogglecolor == 28: _toggle_color(menucolor_28, thissetting)
    if settogglecolor == 29: _toggle_color(menucolor_29, thissetting)
    if settogglecolor == 30: _toggle_color(menucolor_30, thissetting)
def _toggle_color(color__file, thesetting):
    ADDON_TVGFS.setSetting(thesetting, color__file)
    _reopen()
def _reopen():
    xbmc.executebuiltin('ActivateWindow(home)')
    xbmc.executebuiltin('Dialog.Close(all,true)')
    xbmc.sleep(350)
    xbmc.executebuiltin('RunScript('+ addonPath_tvgfs + '/addon.py)')
def toggle_vertical(): # Horizontal Reverse the description area with the epg columns
     #xbmcgui.Dialog().notification('Toggle', 'Flip Vertical', ICON, 1000, False)
     xbmc.executebuiltin('XBMC.ActivateWindow(home)')
     #xbmc.sleep(350)
     Clean_Name = xbmc.translatePath(os.path.join(skinPath, rez, 'script-tvguide-main.xml'))
     if not os.path.exists(Clean_Name): return
     tmpFile = xbmc.translatePath(os.path.join('special://home', 'addons', 'packages','tmp.xml'))
     if os.path.exists(tmpFile): delete_file(tmpFile)
     try:    os.rename(Clean_Name, tmpFile)
     except: pass
     s=open(tmpFile).read()
     # this is because of 5001 wich is hardcodes in gui.py
     if rez == '720p':
         if '240.6' in s:
             s=s.replace('240.6','30.6')
             _set_skin_vars('referencenumber','30.6');ADDON.setSetting('var.referencenumber','30.6')# toggle
         else:
             s=s.replace('30.6','240.6')
             _set_skin_vars('referencenumber','240.6');ADDON.setSetting('var.referencenumber','240.6')# toggle
     if rez == '1080i':
         if '361' in s:
             s=s.replace('361','46')
             _set_skin_vars('referencenumber','46');ADDON.setSetting('var.referencenumber','46')# toggle
         else:
             s=s.replace('46','361')
             _set_skin_vars('referencenumber','361');ADDON.setSetting('var.referencenumber','361')# toggle
     f=open(Clean_Name,'a')
     f.write(s)
     f.close()
     if os.path.exists(tmpFile): delete_file(tmpFile)
     xbmcgui.Dialog().notification('Toggle', 'Flip EPG Vertical', ICON, 1000, False)
     _togglesetting('var.flip_vertical')
     if not xbmc.getCondVisibility('String.IsEqual(Window(1100).Property(flip_vertical),true)'): _set_skin_vars('flip_vertical','true')
     else:  _set_skin_vars('flip_vertical','false')
def toggle_horizontal(): # Vertical Reverse the description area with videowindow
    #xbmcgui.Dialog().notification('Toggle', 'Flip Horizontal', ICON, 1000, False)
    _togglesetting('var.flip_horizontal')
    if not xbmc.getCondVisibility('String.IsEqual(Window(1100).Property(flip_horizontal),true)'): _set_skin_vars('flip_horizontal','true')
    else:  _set_skin_vars('flip_horizontal','false')
def toggle_1080():
    disabled_1080 = xbmc.translatePath(os.path.join(skinPath, '1080i_'))
    enabled_1080  = xbmc.translatePath(os.path.join(skinPath, '1080i'))
    xbmc.executebuiltin('ActivateWindow(home)')
    xbmc.executebuiltin('Dialog.Close(all,true)')
    xbmc.sleep(350)
    if os.path.exists(xbmc.translatePath(os.path.join(enabled_1080, 'script-tvguide-main.xml'))):
        xbmcgui.Dialog().notification('Toggle', 'Disable 1080', ICON, 1000, False)
        os.rename(enabled_1080, disabled_1080)
    else:
        xbmcgui.Dialog().notification('Toggle', 'Enable 1080', ICON, 1000, False)
        os.rename(disabled_1080, enabled_1080)
def toggle_jarvis_strings():
    # 16 to 17 toggle
    xbmcgui.Dialog().notification('Toggle', '16 to 17 toggle', ICON, 1000, False)
    xbmc.executebuiltin('XBMC.ActivateWindow(home)')
    xbmc.sleep(350)
    _toggle_jarvis_strings('script-tvguide-main.xml', rez)
    _toggle_jarvis_strings('script-tvguide-menu.xml', rez)
    _toggle_jarvis_strings('script-tvguide-vod-tv.xml', rez)
    _toggle_jarvis_strings('script-tvguide-streamsetup.xml', rez)
    _toggle_jarvis_strings('script-tvguide-programlist.xml', rez)
    _reopen()
def _toggle_jarvis_strings(Clean_File, rezsize):
     # Flip 16 to kodi 17 plus strings
     #
     # in Kodi 17 these are depreciated
     #16 IsEmpty  to  17  String.IsEmpty                script-tvguide-main   script-tvguide-menu  script-tvguide-vod-tv
     #16 StringCompare  to  17 String.IsEqual           script-tvguide-main   script-tvguide-menu  script-tvguide-vod-tv   script-tvguide-programlist (not needed)
     #16 SubString  to  17  String.Contains             script-tvguide-main   script-tvguide-menu  script-tvguide-vod-tv   script-tvguide-streamsetup
     #16 IntegerGreaterThan  to  17 Integer.IsGreater   script-tvguide-main   script-tvguide-menu  script-tvguide-vod-tv   script-tvguide-streamsetup
     Clean_Name = xbmc.translatePath(os.path.join(skinPath, rezsize, Clean_File))
     if not os.path.exists(Clean_Name): return
     tmpFile = xbmc.translatePath(os.path.join('special://home', 'addons', 'packages','tmp.xml'))
     if os.path.exists(tmpFile): delete_file(tmpFile)
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
     # 16 IsEmpty  to  17  String.IsEmpty
     if '!String.IsEmpty' in s:  s=s.replace('!String.IsEmpty','!IsEmpty')
     else:  s=s.replace('!IsEmpty','!String.IsEmpty')
     # 16 IsEmpty  to  17  String.IsEmpty
     if '>String.IsEmpty' in s:  s=s.replace('>String.IsEmpty','>IsEmpty')
     else:  s=s.replace('>IsEmpty','>String.IsEmpty')
     f=open(Clean_Name,'a')
     f.write(s)
     f.close()
     if os.path.exists(tmpFile): delete_file(tmpFile)
################################################################################
# GUI - Reset TVGFS database
################################################################################
def gui_resetdatabase():
    choiceresetdatabase = dialog.select('Delete MAIN TV Guide Database files?', ['Reset EPG Data','Reset Everything','Reset Image cache','Delete TheLogoDB.com Cache'])
    if choiceresetdatabase == 0: xbmc.executebuiltin('RunScript('+refreshdatabase+', 1)')# Reset Database Reset EPG Data
    if choiceresetdatabase == 1: xbmc.executebuiltin('RunScript('+refreshdatabase+', 2)')# Reset Database Everything
    if choiceresetdatabase == 2: xbmc.executebuiltin('RunScript('+refreshdatabase+', 3)')# Reset Database  Image cache
    if choiceresetdatabase == 3: xbmc.executebuiltin('RunScript('+refreshdatabase+', 4)')# Delete TheLogoDB.com Cache
def delete_file_prompt(filename=None):
    if dialog.yesno('Delete File?', "[COLOR yellow]Would you like delete the current [COLOR white]%s[/COLOR] file?" % filename, yeslabel="[B][COLOR green]Yes Delete[/COLOR][/B]", nolabel="[B][COLOR red]No Skip[/COLOR][/B]"):
        tries = 10
        while os.path.exists(filename) and tries > 0:
            try:
                os.remove(filename)
                break
            except:
                tries -= 1
        dialog.notification("TV Guide Fullscreen","Done Deleting",sound=False)
def delete_file(filename=None):
    tries = 10
    while os.path.exists(filename) and tries > 0:
        try:
            os.remove(filename)
            break
        except:
            tries -= 1
def remove_dir(path=None):
    dirList, flsList = xbmcvfs.listdir(path)
    for fl in flsList:
        xbmcvfs.delete(os.path.join(path, fl))
    for dr in dirList:
        xbmcvfs.delete(xbmc.translatePath(os.path.join(path, '%s')) % dr)
    xbmcvfs.rmdir(path)
################################################################################
# GUI - skin XML - Open a custom skin xml
################################################################################
def gui_run_custom_skinxml(thisxml):
    class cGUI(xbmcgui.WindowXML):
        def __init__(self, *args, **kwargs):
            #self.main_id = 1100
            self.main_control_id = 90000
        def onClick(self, controlID):
            if controlID == self.main_control_id:
                self.gui_button_SelectedPosition = self.gui_button.getSelectedPosition()
                self.setFocus(controlID)
        def setFocusId(self, id=90000):  pass
    ui = cGUI(thisxml, ADDON.getAddonInfo('path'), ADDON.getSetting('skin.user'))
    ui.doModal()
    del ui
################################################################################
# GUI - skin XML - Viewlog 
################################################################################
def gui_LogViewer(default=None):
    class LogViewer(xbmcgui.WindowXMLDialog):
        def __init__(self,*args,**kwargs):
            self.default = kwargs['default']
        def onInit(self):
            self.title      = 101
            self.msg        = 102
            self.scrollbar  = 103
            self.settings   = 201
            self.kodi       = 202
            self.kodiold    = 203
            self.asgui      = 204
            self.okbutton   = 205
            #
            self.advanced   = 206
            self.playercore = 207
            self.sources    = 208
            self.rssfeeds   = 209
            f = open(self.default, 'r')
            self.logmsg = f.read()
            f.close()
            self.titlemsg = "%s: %s" % ('Log and XML Viewer', self.default.replace(xbmc.translatePath('special://logpath/'), '').replace(basePath, ''))
            self.showdialog()
        def showdialog(self):
            self.getControl(self.title).setLabel(self.titlemsg)
            self.getControl(self.msg).setText(_highlightText(self.logmsg))
            self.setFocusId(self.scrollbar)
        def onClick(self, controlId):
            if   controlId == self.okbutton: self.close()
            elif controlId == self.settings: self.close(); gui_set_tvgfs_settings()
            elif controlId == self.kodi:
                newmsg = Grab_Log(False)
                filename = Grab_Log(True)
                if newmsg == False:
                    self.titlemsg = "%s: View Log Error" % ADDONID
                    self.getControl(self.msg).setText("Log File Does Not Exists!")
                else:
                    self.titlemsg = "%s: %s" % ('Kodi Log', filename.replace(xbmc.translatePath('special://logpath/'), ''))
                    self.getControl(self.title).setLabel(self.titlemsg)
                    self.getControl(self.msg).setText(_highlightText(newmsg))
                    self.setFocusId(self.scrollbar)
            elif controlId == self.kodiold:  
                newmsg = Grab_Log(False, True)
                filename = Grab_Log(True, True)
                if newmsg == False:
                    self.titlemsg = "%s: View Log Error" % ADDONID
                    self.getControl(self.msg).setText("Log File Does Not Exists!")
                else:
                    self.titlemsg = "%s: %s" % ('Kodi OLD Log', filename.replace(xbmc.translatePath('special://logpath/'), ''))
                    self.getControl(self.title).setLabel(self.titlemsg)
                    self.getControl(self.msg).setText(_highlightText(newmsg))
                    self.setFocusId(self.scrollbar)
            elif controlId == self.asgui:
                self.close()
                gui_autoConfig()
            elif controlId == self.advanced:
                newmsg = Grab_xml(True, False, False, False)
                filename = Grab_xml(True, False, False, False)
                ADVANCED = xbmc.translatePath('special://home/userdata/advancedsettings.xml')
                if os.path.exists(ADVANCED):
                    self.titlemsg = "[COLOR orange]%s: advanced.xml[/COLOR]  (extra gui tweaks to override guisettings.xml)\n\n   %s" % (ADDONID,  filename.replace(ADVANCED, ''))
                    self.getControl(self.title).setLabel(self.titlemsg)
                    self.getControl(self.msg).setText(self.titlemsg)
                    self.setFocusId(self.scrollbar)
                else:
                    self.titlemsg = "%s: View advancedsettings Error" % ADDONID
                    self.getControl(self.msg).setText("advancedsettings File Does Not Exists!")
            elif controlId == self.playercore:
                newmsg = Grab_xml(False, True, False, False)
                filename = Grab_xml(False, True, False, False)
                PLAYERCORE = xbmc.translatePath('special://home/userdata/playercorefactory.xml')
                if os.path.exists(PLAYERCORE):
                    self.titlemsg = "[COLOR orange]%s: advanced.xml[/COLOR]  (3rd Party Players)\n\n   %s" % (ADDONID,  filename.replace(PLAYERCORE, ''))
                    self.getControl(self.title).setLabel(self.titlemsg)
                    self.getControl(self.msg).setText(self.titlemsg)
                    self.setFocusId(self.scrollbar)
                else:
                    self.titlemsg = "%s: View playerfactorycore.xml Error" % ADDONID
                    self.getControl(self.msg).setText("playerfactorycore.xml File Does Not Exists!")
            elif controlId == self.sources:
                newmsg = Grab_xml(False, False, True, False)
                filename = Grab_xml(False, False, True, False)
                SOURCES = xbmc.translatePath('special://home/userdata/sources.xml')
                if os.path.exists(SOURCES):
                    self.titlemsg = "[COLOR orange]%s: sources.xml[/COLOR]  (Media and repo paths)\n\n   %s" % (ADDONID,  filename.replace(SOURCES, ''))
                    self.getControl(self.title).setLabel(self.titlemsg)
                    self.getControl(self.msg).setText(self.titlemsg)
                    self.setFocusId(self.scrollbar)
                else:
                    self.titlemsg = "%s: View sources.xml Error" % ADDONID
                    self.getControl(self.msg).setText("sources.xml File Does Not Exists!")
            elif controlId == self.rssfeeds:
                newmsg = Grab_xml(False, False, False, True)
                filename = Grab_xml(False, False, False, True)
                RSSFEED  = xbmc.translatePath('special://home/userdata/RssFeeds.xml')
                if os.path.exists(RSSFEED):
                    self.titlemsg = "[COLOR orange]%s: RssFeeds.xml[/COLOR]  (Kodi Rss Feeds)\n\n   %s" % (ADDONID,  filename.replace(RSSFEED, ''))
                    self.getControl(self.title).setLabel(self.titlemsg)
                    self.getControl(self.msg).setText(self.titlemsg)
                    self.setFocusId(self.scrollbar)
                else:
                    self.titlemsg = "%s: View rssfeeds.xml Error" % ADDONID
                    self.getControl(self.msg).setText("rssfeeds.xml File Does Not Exists!")
        def onAction(self, action):
            if   action == ACTION_PREVIOUS_MENU: self.close()
            elif action == ACTION_NAV_BACK: self.close()
    if default == None: default = Grab_Log(True)
    lv = LogViewer('LogViewer.xml', ADDON.getAddonInfo('path'), installerskin, default=default)
    lv.doModal()
    del lv
def _highlightText(msg):
    msg = msg.replace('\n', '[NL]')
    matches = re.compile("-->Python callback/script returned the following error<--(.+?)-->End of Python script error report<--").findall(msg)
    for item in matches:
        string = '-->Python callback/script returned the following error<--%s-->End of Python script error report<--' % item
        msg    = msg.replace(string, '[COLOR red]%s[/COLOR]' % string)
    msg = msg.replace('WARNING', '[COLOR yellow]WARNING[/COLOR]').replace('ERROR', '[COLOR red]ERROR[/COLOR]').replace('[NL]', '\n').replace(': EXCEPTION Thrown (PythonToCppException) :', '[COLOR red]: EXCEPTION Thrown (PythonToCppException) :[/COLOR]')
    msg = msg.replace('\\\\', '\\').replace(xbmc.translatePath('special://home/'), '')
    return msg
def Grab_Log(file=False, old=False, wizard=False):
    finalfile   = 0
    logfilepath = os.listdir(xbmc.translatePath('special://logpath/'))
    logsfound   = []
    for item in logfilepath:
        if old == True and item.endswith('.old.log'): logsfound.append(os.path.join(xbmc.translatePath('special://logpath/'), item))
        elif old == False and item.endswith('.log') and not item.endswith('.old.log'): logsfound.append(os.path.join(xbmc.translatePath('special://logpath/'), item))
    if len(logsfound) > 0:
        logsfound.sort(key=lambda f: os.path.getmtime(f))
        if file == True: return logsfound[-1]
        else:
            filename    = open(logsfound[-1], 'r')
            logtext     = filename.read()
            filename.close()
            return logtext
    else:  return False
def Grab_xml(advanced=False, playercore=False, sources=False, rssfeeds=False):  # xml in log viewer
    if advanced == True:
        ADVANCED = xbmc.translatePath('special://home/userdata/advancedsettings.xml')
        if not os.path.exists(ADVANCED): return False
        else:
            if file == True:
                return ADVANCED
            else:
                filename    = open(ADVANCED, 'r')
                logtext     = filename.read()
                filename.close()
                return logtext
    if playercore == True:
        PLAYERCORE = xbmc.translatePath('special://home/userdata/playercorefactory.xml')
        if not os.path.exists(PLAYERCORE): return False
        else:
            if file == True:
                return PLAYERCORE
            else:
                filename    = open(PLAYERCORE, 'r')
                logtext     = filename.read()
                filename.close()
                return logtext
    if sources == True:
        SOURCES = xbmc.translatePath('special://home/userdata/sources.xml')
        if not os.path.exists(SOURCES): return False
        else:
            if file == True:
                return SOURCES
            else:
                filename    = open(SOURCES, 'r')
                logtext     = filename.read()
                filename.close()
                return logtext
    if rssfeeds == True:
        RSSFEED  = xbmc.translatePath('special://home/userdata/RssFeeds.xml')
        if not os.path.exists(RSSFEED): return False
        else:
            if file == True:
                return RSSFEED
            else:
                filename    = open(RSSFEED, 'r')
                logtext     = filename.read()
                filename.close()
                return logtext
    finalfile   = 0
    #logfilepath = os.listdir(xbmc.translatePath('special://logpath/'))
    logsfound   = []
    if len(logsfound) > 0:
        logsfound.sort(key=lambda f: os.path.getmtime(f))
        # WALDO  congrats you found a useless line of code easter egg.  I hope you enjoy the mods as much as i do using them.
        if file == True: return logsfound[-1]
        else:
            filename    = open(logsfound[-1], 'r')
            logtext     = filename.read()
            filename.close()
            return logtext
    else: 
        return False
################################################################################
# GUI - advancedsettings.xml gui window no skin xml
################################################################################
def gui_autoConfig(msg='', TxtColor='0xFFFFFFFF', Font='font13', BorderWidth=10):
    class MyWindow(xbmcgui.WindowDialog):
        scr={};
        def __init__(self,msg='',L=0,T=0,W=1280,H=720,TxtColor='0xFFFFFFFF',Font='font12',BorderWidth=10):
            advancedinstaller  = xbmc.translatePath(os.path.join(addonPath,'resources','skins',installerskin,'media', 'advancedgui'))# advancedsettings gui media path
            buttonfocus, buttonnofocus = os.path.join(advancedinstaller, 'button-focus_lightblue.png'), os.path.join(advancedinstaller, 'button-focus_grey.png')
            radiobgfocus, radiobgnofocus, radiofocus, radionofocus = os.path.join(advancedinstaller, 'MenuItemFO.png'), os.path.join(advancedinstaller, 'MenuItemNF.png'), os.path.join(advancedinstaller, 'radiobutton-focus.png'), os.path.join(advancedinstaller, 'radiobutton-nofocus.png')
            slidernibfocus, slidernibnofocus, sliderfocus, slidernofocus = os.path.join(advancedinstaller, 'osd_slider_nib.png'), os.path.join(advancedinstaller, 'osd_slider_nibNF.png'), os.path.join(advancedinstaller, 'slider1.png'), os.path.join(advancedinstaller, 'slider1.png')
            image_path = os.path.join(advancedinstaller, 'ContentPanel.png')
            boxbg = os.path.join(advancedinstaller, 'bgg2.png')
            self.border = xbmcgui.ControlImage(L,T,W,H, image_path)
            self.addControl(self.border); 
            self.BG=xbmcgui.ControlImage(L+BorderWidth,T+BorderWidth,W-(BorderWidth*2),H-(BorderWidth*2), os.path.join(advancedinstaller, 'black.png'), aspectRatio=0, colorDiffuse='0x5FFFFFFF')
            self.addControl(self.BG)
            top = T+BorderWidth
            leftside = L+BorderWidth
            rightside = L+(W/2)-(BorderWidth*2)
            firstrow = top+30
            secondrow = firstrow+275+(BorderWidth/2)
            currentwidth = ((W/2)-(BorderWidth*4))/2
            #
            header = '[COLOR %s]Advanced Settings Configurator[/COLOR]' % ('white')
            self.Header=xbmcgui.ControlLabel(L, top, W, 30, header, font='font13', textColor=TxtColor, alignment=0x00000002)
            self.addControl(self.Header)
            top += 30+BorderWidth
            self.bgarea = xbmcgui.ControlImage(leftside, firstrow, rightside-L, 275, boxbg, aspectRatio=0, colorDiffuse='0x5FFFFFFF')
            self.addControl(self.bgarea)
            self.bgarea2 = xbmcgui.ControlImage(rightside+BorderWidth+BorderWidth, firstrow, rightside-L, 275, boxbg, aspectRatio=0, colorDiffuse='0x5FFFFFFF')
            self.addControl(self.bgarea2)
            self.bgarea3 = xbmcgui.ControlImage(leftside, secondrow, rightside-L, 275, boxbg, aspectRatio=0, colorDiffuse='0x5FFFFFFF')
            self.addControl(self.bgarea3)
            self.bgarea4 = xbmcgui.ControlImage(rightside+BorderWidth+BorderWidth, secondrow, rightside-L, 275, boxbg, aspectRatio=0, colorDiffuse='0x5FFFFFFF')
            self.addControl(self.bgarea4)
            #
            header = '[COLOR %s]Video Cache Size[/COLOR]' % ('white')
            self.Header2=xbmcgui.ControlLabel(leftside+BorderWidth, firstrow+5, (W/2)-(BorderWidth*2), 20, header, font='font10', textColor=TxtColor, alignment=0x00000002)
            self.addControl(self.Header2)
            freeMemory = int(float(_getInfo('System.Memory(free)')[:-2])*.33)
            recMemory = int(float(_getInfo('System.Memory(free)')[:-2])*.23)
            msg3 = "[COLOR %s]Number of bytes used for buffering streams in memory.  When set to [COLOR %s]0[/COLOR] the cache will be written to disk instead of RAM.  Note: For the memory size set here, Kodi will require 3x the amount of RAM to be free. Setting this too high might cause Kodi to crash if it can't get enough RAM(1/3 of Free Memory: [COLOR %s]%s[/COLOR])[/COLOR]" % ('white', 'gold', 'gold', freeMemory)
            self.Support3=xbmcgui.ControlTextBox(leftside+int(BorderWidth*1.5), firstrow+30+BorderWidth, (W/2)-(BorderWidth*4), 150, font='font10', textColor=TxtColor)
            self.addControl(self.Support3)
            self.Support3.setText(msg3)
            try: self.videoCacheSize=xbmcgui.ControlSlider(leftside+int(BorderWidth*1.5), firstrow+210,(W/2)-(BorderWidth*5),20, textureback=sliderfocus, texture=slidernibnofocus, texturefocus=slidernibfocus, orientation=xbmcgui.HORIZONTAL)
            except: self.videoCacheSize=xbmcgui.ControlSlider(leftside+int(BorderWidth*1.5), firstrow+210,(W/2)-(BorderWidth*5),20, textureback=sliderfocus, texture=slidernibnofocus, texturefocus=slidernibfocus)
            self.addControl(self.videoCacheSize)
            self.videomin = 0; self.videomax = freeMemory if freeMemory < 2000 else 2000
            self.recommendedVideo = recMemory if recMemory < 500 else 500; self.currentVideo = self.recommendedVideo
            videopos = _percentage(self.currentVideo, self.videomax)
            self.videoCacheSize.setPercent(videopos)
            current1 = '[COLOR %s]Current:[/COLOR] [COLOR %s]%s MB[/COLOR]' % ('gold', 'white', self.currentVideo)
            recommended1 = '[COLOR %s]Recommended:[/COLOR] [COLOR %s]%s MB[/COLOR]' % ('gold', 'white', self.recommendedVideo)
            self.currentVideo1=xbmcgui.ControlTextBox(leftside+BorderWidth,firstrow+235,currentwidth,25,font=Font,textColor=TxtColor)
            self.addControl(self.currentVideo1)
            self.currentVideo1.setText(current1)
            self.recommendedVideo1=xbmcgui.ControlTextBox(leftside+BorderWidth+currentwidth,firstrow+235,currentwidth,25,font=Font,textColor=TxtColor)
            self.addControl(self.recommendedVideo1)
            self.recommendedVideo1.setText(recommended1)
            #
            header = '[COLOR %s]CURL Timeout/CURL Low Speed[/COLOR]' % ('white')
            self.Header3=xbmcgui.ControlLabel(rightside+BorderWidth, firstrow+5, (W/2)-(BorderWidth*2), 20, header, font='font13', textColor=TxtColor, alignment=0x00000002)
            self.addControl(self.Header3)
            msg3 = "[COLOR %s][B]curlclienttimeout[/B] is the time in seconds for how long it takes for libcurl connection will timeout and [B]curllowspeedtime[/B] is the time in seconds for libcurl to consider a connection lowspeed.  For slower connections set it to 20.[/COLOR]" % 'white'
            self.Support3=xbmcgui.ControlTextBox(rightside+int(BorderWidth*3.5), firstrow+30+BorderWidth, (W/2)-(BorderWidth*4), 150, font='font12', textColor=TxtColor)
            self.addControl(self.Support3)
            self.Support3.setText(msg3)
            try: self.CURLTimeout=xbmcgui.ControlSlider(rightside+int(BorderWidth*3.5),firstrow+210,(W/2)-(BorderWidth*5),20, textureback=sliderfocus, texture=slidernibnofocus, texturefocus=slidernibfocus, orientation=xbmcgui.HORIZONTAL)
            except: self.CURLTimeout=xbmcgui.ControlSlider(rightside+int(BorderWidth*3.5),firstrow+210,(W/2)-(BorderWidth*5),20, textureback=sliderfocus, texture=slidernibnofocus, texturefocus=slidernibfocus)
            self.addControl(self.CURLTimeout)
            self.curlmin = 0; self.curlmax = 20
            self.recommendedCurl = 10; self.currentCurl = self.recommendedCurl
            curlpos = _percentage(self.currentCurl, self.curlmax)
            self.CURLTimeout.setPercent(curlpos)
            current2 = '[COLOR %s]Current:[/COLOR] [COLOR %s]%ss[/COLOR]' % ('gold', 'white', self.currentCurl)
            recommended2 = '[COLOR %s]Recommended:[/COLOR] [COLOR %s]%ss[/COLOR]' % ('gold', 'white', self.recommendedCurl)
            self.currentCurl2=xbmcgui.ControlTextBox(rightside+(BorderWidth*3),firstrow+235,currentwidth,25,font=Font,textColor=TxtColor)
            self.addControl(self.currentCurl2)
            self.currentCurl2.setText(current2)
            self.recommendedCurl2=xbmcgui.ControlTextBox(rightside+(BorderWidth*3)+currentwidth,firstrow+235,currentwidth,25,font=Font,textColor=TxtColor)
            self.addControl(self.recommendedCurl2)
            self.recommendedCurl2.setText(recommended2)
            #
            header = '[COLOR %s]Read Buffer Factor[/COLOR]' % ('white')
            self.Header4=xbmcgui.ControlLabel(leftside, secondrow+5, (W/2)-(BorderWidth*2), 20, header, font='font13', textColor=TxtColor, alignment=0x00000002)
            self.addControl(self.Header4)
            msg3 = "[COLOR %s]The value of this setting is a multiplier of the default limit. If Kodi is loading a typical bluray raw file at 36 Mbit/s, then a value of 2 will need at least 72 Mbit/s of network bandwidth. However, unlike with the RAM setting, you can safely increase this value however high you want, and Kodi won't crash.[/COLOR]" % 'white'
            self.Support3=xbmcgui.ControlTextBox(leftside+int(BorderWidth*1.5), secondrow+30+BorderWidth, (W/2)-(BorderWidth*4), 150, font='font12', textColor=TxtColor)
            self.addControl(self.Support3)
            self.Support3.setText(msg3)
            try: self.readBufferFactor=xbmcgui.ControlSlider(leftside+int(BorderWidth*1.5), secondrow+210,(W/2)-(BorderWidth*5),20, textureback=sliderfocus, texture=slidernibnofocus, texturefocus=slidernibfocus, orientation=xbmcgui.HORIZONTAL)
            except: self.readBufferFactor=xbmcgui.ControlSlider(leftside+int(BorderWidth*1.5), secondrow+210,(W/2)-(BorderWidth*5),20, textureback=sliderfocus, texture=slidernibnofocus, texturefocus=slidernibfocus)
            self.addControl(self.readBufferFactor)
            self.readmin = 0; self.readmax = 10
            self.recommendedRead = 5; self.currentRead = self.recommendedRead
            readpos = _percentage(self.currentRead, self.readmax)
            self.readBufferFactor.setPercent(readpos)
            current3 = '[COLOR %s]Current:[/COLOR] [COLOR %s]%s[/COLOR]' % ('gold', 'white', self.currentRead)
            recommended3 = '[COLOR %s]Recommended:[/COLOR] [COLOR %s]%s[/COLOR]' % ('gold', 'white', self.recommendedRead)
            self.currentRead3=xbmcgui.ControlTextBox(leftside+BorderWidth,secondrow+235,currentwidth,25,font=Font,textColor=TxtColor)
            self.addControl(self.currentRead3)
            self.currentRead3.setText(current3)
            self.recommendedRead3=xbmcgui.ControlTextBox(leftside+BorderWidth+currentwidth,secondrow+235,currentwidth,25,font=Font,textColor=TxtColor)
            self.addControl(self.recommendedRead3)
            self.recommendedRead3.setText(recommended3)
            #
            header = '[COLOR %s]Buffer Mode[/COLOR]' % ('white')
            self.Header4=xbmcgui.ControlLabel(rightside+BorderWidth, secondrow+5, (W/2)-(BorderWidth*2), 20, header, font='font13', textColor=TxtColor, alignment=0x00000002)
            self.addControl(self.Header4)
            msg4 = "[COLOR %s]This setting will force Kodi to use a cache for all video files, including local network, internet, and even the local hard drive. Default value is 0 and will only cache videos that use internet file paths/sources.[/COLOR]" % 'white'
            self.Support4=xbmcgui.ControlTextBox(rightside+int(BorderWidth*3.5), secondrow+30+BorderWidth, (W/2)-(BorderWidth*4), 110, font='font12', textColor=TxtColor)
            self.addControl(self.Support4)
            self.Support4.setText(msg4)
            B1 = secondrow+130+BorderWidth; B2 = B1+30; B3 = B2+30; B4 = B3+30;
            self.Button0 = xbmcgui.ControlRadioButton(rightside+(BorderWidth*3), B1, (W/2)-(BorderWidth*4), 30, '0: Buffer all internet filesystems', font='font12', focusTexture=radiobgfocus, noFocusTexture=radiobgnofocus, focusOnTexture=radiofocus, noFocusOnTexture=radiofocus, focusOffTexture=radionofocus, noFocusOffTexture=radionofocus)
            self.Button1 = xbmcgui.ControlRadioButton(rightside+(BorderWidth*3), B2, (W/2)-(BorderWidth*4), 30, '1: Buffer all filesystems', font='font12', focusTexture=radiobgfocus, noFocusTexture=radiobgnofocus, focusOnTexture=radiofocus, noFocusOnTexture=radiofocus, focusOffTexture=radionofocus, noFocusOffTexture=radionofocus)
            self.Button2 = xbmcgui.ControlRadioButton(rightside+(BorderWidth*3), B3, (W/2)-(BorderWidth*4), 30, '2: Only buffer true internet filesystems', font='font12', focusTexture=radiobgfocus, noFocusTexture=radiobgnofocus, focusOnTexture=radiofocus, noFocusOnTexture=radiofocus, focusOffTexture=radionofocus, noFocusOffTexture=radionofocus)
            self.Button3 = xbmcgui.ControlRadioButton(rightside+(BorderWidth*3), B4, (W/2)-(BorderWidth*4), 30, '3: No Buffer', font='font12', focusTexture=radiobgfocus, noFocusTexture=radiobgnofocus, focusOnTexture=radiofocus, noFocusOnTexture=radiofocus, focusOffTexture=radionofocus, noFocusOffTexture=radionofocus)
            self.addControl(self.Button0)
            self.addControl(self.Button1)
            self.addControl(self.Button2)
            self.addControl(self.Button3)
            self.Button0.setSelected(False)
            self.Button1.setSelected(True)
            self.Button2.setSelected(False)
            self.Button3.setSelected(False)
            #
            self.buttonWrite=xbmcgui.ControlButton(leftside,T+H-40-BorderWidth,(W/2)-(BorderWidth*2),35,"Write File",textColor="0xFF000000",focusedColor="0xFF000000",alignment=2,focusTexture=buttonfocus,noFocusTexture=buttonnofocus)
            self.buttonCancel=xbmcgui.ControlButton(rightside+BorderWidth*2,T+H-40-BorderWidth,(W/2)-(BorderWidth*2),35,"Cancel",textColor="0xFF000000",focusedColor="0xFF000000",alignment=2,focusTexture=buttonfocus,noFocusTexture=buttonnofocus)
            self.addControl(self.buttonWrite); self.addControl(self.buttonCancel)
            #
            self.buttonWrite.controlLeft(self.buttonCancel); self.buttonWrite.controlRight(self.buttonCancel); self.buttonWrite.controlUp(self.Button3); self.buttonWrite.controlDown(self.videoCacheSize)
            self.buttonCancel.controlLeft(self.buttonWrite); self.buttonCancel.controlRight(self.buttonWrite); self.buttonCancel.controlUp(self.Button3); self.buttonCancel.controlDown(self.videoCacheSize)
            self.videoCacheSize.controlUp(self.buttonWrite); self.videoCacheSize.controlDown(self.CURLTimeout)
            self.CURLTimeout.controlUp(self.videoCacheSize); self.CURLTimeout.controlDown(self.readBufferFactor)
            self.readBufferFactor.controlUp(self.CURLTimeout); self.readBufferFactor.controlDown(self.Button0)
            self.Button0.controlUp(self.CURLTimeout); self.Button0.controlDown(self.Button1); self.Button0.controlLeft(self.readBufferFactor); self.Button0.controlRight(self.readBufferFactor);
            self.Button1.controlUp(self.Button0); self.Button1.controlDown(self.Button2); self.Button1.controlLeft(self.readBufferFactor); self.Button1.controlRight(self.readBufferFactor);
            self.Button2.controlUp(self.Button1); self.Button2.controlDown(self.Button3); self.Button2.controlLeft(self.readBufferFactor); self.Button2.controlRight(self.readBufferFactor);
            self.Button3.controlUp(self.Button2); self.Button3.controlDown(self.buttonWrite); self.Button3.controlLeft(self.readBufferFactor); self.Button3.controlRight(self.readBufferFactor);
            self.setFocus(self.videoCacheSize)
        def doExit(self):
            self.CloseWindow()
        def updateCurrent(self, control):
            if control == self.videoCacheSize:
                self.currentVideo = (self.videomax)*self.videoCacheSize.getPercent()/100
                current = '[COLOR %s]Current:[/COLOR] [COLOR %s]%s MB[/COLOR]' % ('gold', 'white', int(self.currentVideo))
                self.currentVideo1.setText(current)
            elif control == self.CURLTimeout:
                self.currentCurl = (self.curlmax)*self.CURLTimeout.getPercent()/100
                current = '[COLOR %s]Current:[/COLOR] [COLOR %s]%ss[/COLOR]' % ('gold', 'white', int(self.currentCurl))
                self.currentCurl2.setText(current)
            elif control == self.readBufferFactor:
                self.currentRead = (self.readmax)*self.readBufferFactor.getPercent()/100
                current = '[COLOR %s]Current:[/COLOR] [COLOR %s]%s[/COLOR]' % ('gold', 'white', int(self.currentRead))
                self.currentRead3.setText(current)
            elif control in [self.Button0, self.Button1, self.Button2, self.Button3]:
                self.Button0.setSelected(False)
                self.Button1.setSelected(False)
                self.Button2.setSelected(False)
                self.Button3.setSelected(False)
                control.setSelected(True)
        def doWrite(self):
            #self.currentVideo = int((self.videomax-20)*self.videoCacheSize.getPercent()/100+20)*1024*1024
            #self.currentCurl = int((self.curlmax)*self.CURLTimeout.getPercent()/100)
            #self.currentRead = int((self.readmax)*self.readBufferFactor.getPercent()/100)
            if   self.Button0.isSelected(): buffermode = 0
            elif self.Button1.isSelected(): buffermode = 1
            elif self.Button2.isSelected(): buffermode = 2
            elif self.Button3.isSelected(): buffermode = 3
            ADVANCED = xbmc.translatePath('special://home/userdata/advancedsettings.xml')
            if os.path.exists(ADVANCED):
                choicewritexml = dialog.yesno('Delete current?', "[COLOR %s]There is currently an active [COLOR %s]AdvancedSettings.xml[/COLOR], would you like to remove it and continue?[/COLOR]" % ('gold', 'white'), yeslabel="[B][COLOR green]Remove Settings[/COLOR][/B]", nolabel="[B][COLOR red]Cancel Write[/COLOR][/B]")
                if choicewritexml == 0: return
                try: os.remove(ADVANCED)
                except: f = open(ADVANCED, 'w'); f.close()
            with open(ADVANCED, 'w+') as f:
                f.write('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n')
                f.write('<advancedsettings>\n')
                f.write('    <splash>false</splash>\n')
                f.write('    <loglevel hide="false">0</loglevel>\n')
                f.write('    <jsonrpc>\n');f.write('        <compactoutput>true</compactoutput>\n');f.write('    </jsonrpc>\n')
                f.write('    <samba>\n');f.write('        <statfiles>false</statfiles>\n');f.write('    </samba>\n')
                f.write('    <gui>\n');f.write('        <nofliptimeout>0</nofliptimeout>\n');f.write('        <algorithmdirtyregions>3</algorithmdirtyregions>\n');f.write('    </gui>\n')
                f.write('    <filelists>\n');f.write('        <allowfiledeletion>true</allowfiledeletion>\n');f.write('    </filelists>\n')
                f.write('    <videolibrary>\n');f.write('        <cleanonupdate>true</cleanonupdate>\n');f.write('    </videolibrary>\n')
                f.write('    <videoextensions>\n');f.write('        <add>.html</add>\n');f.write('    </videoextensions>\n')
                f.write('    <videoscanner>\n');f.write('        <ignoreerrors>true</ignoreerrors>\n');f.write('    </videoscanner>\n')
                # less than 17
                KODIV  = float(xbmc.getInfoLabel("System.BuildVersion")[:4])
                if KODIV < 17: f.write('    <network>\n');f.write('        <buffermode>%s</buffermode>\n' % buffermode);f.write('        <cachemembuffersize>%s</cachemembuffersize>\n' % int(self.currentVideo*1024*1024));f.write('        <readbufferfactor>%s</readbufferfactor>\n' % self.currentRead);f.write('        <curlclienttimeout>%s</curlclienttimeout>\n' % self.currentCurl);f.write('        <curllowspeedtime>%s</curllowspeedtime>\n' % self.currentCurl);f.write('    </network>\n')
                # greater than 17
                else: f.write('    <cache>\n');f.write('        <buffermode>%s</buffermode>\n' % buffermode);f.write('        <memorysize>%s</memorysize>\n' % int(self.currentVideo*1024*1024));f.write('        <readfactor>%s</readfactor>\n' % self.currentRead);f.write('    </cache>\n');f.write('    <network>\n');f.write('        <curlclienttimeout>%s</curlclienttimeout>\n' % self.currentCurl);f.write('        <curllowspeedtime>%s</curllowspeedtime>\n' % self.currentCurl);f.write('    </network>\n')
                if KODIV < 18: f.write('    <gamesgeneral>\n');f.write('        <enable>true</enable>\n');f.write('    </gamesgeneral>\n')
                sqldo = dialog.yesno('SQL (Optional)', "[COLOR %s]Do you use an [COLOR %s]SQL Server[/COLOR]?[/COLOR]" % ('gold', 'white'),"Only answer yes if you are sure", yeslabel="[B][COLOR green]Yes[/COLOR][/B]?", nolabel="[B][COLOR red]No[/COLOR][/B] (Default)")
                if not sqldo == 0:
                    keyboard = xbmc.Keyboard('192.168.1.2', 'sql host');keyboard.doModal()
                    if keyboard.isConfirmed() and keyboard.getText():  sql_host = keyboard.getText()
                    keyboard = xbmc.Keyboard('xbox', 'sql user');keyboard.doModal()
                    if keyboard.isConfirmed() and keyboard.getText():  sql_user = keyboard.getText()
                    keyboard = xbmc.Keyboard('xbox', 'sql pass');keyboard.doModal()
                    if keyboard.isConfirmed() and keyboard.getText():  sql_pass = keyboard.getText()
                    f.write('    <musicdatabase>\n');f.write('        <type>mysql</type>\n');f.write('        <host>%s</host>\n' % sql_host);f.write('        <user>%s</user>\n' % sql_user);f.write('        <pass>%s</pass>\n' % sql_pass);f.write('    </musicdatabase>\n')
                    f.write('    <videodatabase>\n');f.write('        <type>mysql</type>\n');f.write('        <host>%s</host>\n' % sql_host);f.write('        <user>%s</user>\n' % sql_user);f.write('        <pass>%s</pass>\n' % sql_pass);f.write('    </videodatabase>\n')
                    f.write('    <tvdatabase>\n');f.write('        <type>mysql</type>\n');f.write('        <host>%s</host>\n' % sql_host);f.write('        <user>%s</user>\n' % sql_user);f.write('        <pass>%s</pass>\n' % sql_pass);f.write('    </tvdatabase>\n')
                    f.write('    <epgdatabase>\n');f.write('        <type>mysql</type>\n');f.write('        <host>%s</host>\n' % sql_host);f.write('        <user>%s</user>\n' % sql_user);f.write('        <pass>%s</pass>\n' % sql_pass);f.write('    </epgdatabase>\n')
                    f.write('    <videolibrary>\n');f.write('        <importwatchedstate>true</importwatchedstate>\n');f.write('        <importresumepoint>true</importresumepoint>\n');f.write('    </videolibrary>\n')
                f.write('</advancedsettings>\n')
                f.close()
            self.CloseWindow()
        def onControl(self, control):
            if   control==self.buttonWrite: self.doWrite()
            elif control==self.buttonCancel:  self.doExit()
        def onAction(self, action):
            try: F=self.getFocus()
            except: F=False
            if   F      == self.videoCacheSize:   self.updateCurrent(self.videoCacheSize)
            elif F      == self.CURLTimeout:      self.updateCurrent(self.CURLTimeout)
            elif F      == self.readBufferFactor: self.updateCurrent(self.readBufferFactor)
            elif F      in [self.Button0, self.Button1, self.Button2, self.Button3] and action in [ACTION_MOUSE_LEFT_CLICK, ACTION_SELECT_ITEM]: self.updateCurrent(F)
            elif action == ACTION_PREVIOUS_MENU:  self.doExit()
            elif action == ACTION_NAV_BACK:       self.doExit()
        def CloseWindow(self): self.close()
    maxW=1280; maxH=720; W=int(900); H=int(650); L=int((maxW-W)/2); T=int((maxH-H)/2); 
    TempWindow=MyWindow(L=L,T=T,W=W,H=H,TxtColor=TxtColor,Font=Font,BorderWidth=BorderWidth); 
    TempWindow.doModal() 
    del TempWindow
def _getInfo(label):
    try: return xbmc.getInfoLabel(label)
    except: return False
def _percentage(part, whole):
    return 100 * float(part)/float(whole)
def _writeplayerfactorycore():
    PLAYERCORE = xbmc.translatePath('special://home/userdata/playercorefactory.xml')
    if os.path.isfile(PLAYERCORE):
        choice = dialog.yesno('Delete Current?', "[COLOR yellow]There is currently an active [COLOR white]playerfactorycore.xml[/COLOR], would you like to remove it and continue?[/COLOR]", yeslabel="[B][COLOR green]Remove Settings[/COLOR][/B]", nolabel="[B][COLOR red]Cancel Write[/COLOR][/B]")
        if choice == 0: return
        if os.path.isfile(PLAYERCORE):
            xbmcvfs.copy(PLAYERCORE, PLAYERCORE+'.last')
            delete_file(PLAYERCORE)
    with open(PLAYERCORE, 'w+') as f:
        f.write('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n')
        f.write('<!-- http://kodi.wiki/view/HOW-TO:Use_external_players_on_Android  -->\n')
        f.write('<!-- http://kodi.wiki/view/External_players  -->\n')
        f.write('<playercorefactory>\n')
        f.write('    <players>\n')
        ##################
        #'''
        if xbmc.getCondVisibility('system.platform.android'):
            PLAYERCFFILE1     = wiz.getS('PLAYERCFFILE1')
            PLAYERCFNAME1     = wiz.getS('PLAYERCFNAME1')
            f.write('         <player name="'+PLAYERCFNAME1+'" type="ExternalPlayer" audio="false" video="true">\n')
            f.write('            <filename>'+PLAYERCFFILE1+'</filename>\n')
            f.write('            <hidexbmc>true</hidexbmc>\n')
            f.write('            <playcountminimumtime>120</playcountminimumtime>\n')
            f.write('         </player>\n')
            PLAYERCFFILE2     = wiz.getS('PLAYERCFFILE2')
            PLAYERCFNAME2     = wiz.getS('PLAYERCFNAME2')
            f.write('         <player name="'+PLAYERCFNAME2+'" type="ExternalPlayer" audio="false" video="true">\n')
            f.write('            <filename>'+playercorefactory2+'</filename>\n')
            f.write('            <hidexbmc>true</hidexbmc>\n')
            f.write('            <playcountminimumtime>120</playcountminimumtime>\n')
            f.write('         </player>\n')
            PLAYERCFFILE3     = wiz.getS('PLAYERCFFILE3')
            PLAYERCFNAME3     = wiz.getS('PLAYERCFNAME3')
            f.write('         <player name="'+PLAYERCFNAME3+'" type="ExternalPlayer" audio="false" video="true">\n')
            f.write('            <filename>'+PLAYERCFFILE3+'</filename>\n')
            f.write('            <hidexbmc>true</hidexbmc>\n')
            f.write('            <playcountminimumtime>120</playcountminimumtime>\n')
            f.write('         </player>\n')
            PLAYERCFFILE4     = wiz.getS('PLAYERCFFILE4')
            PLAYERCFNAME4     = wiz.getS('PLAYERCFNAME4')
            f.write('         <player name="'+PLAYERCFNAME4+'" type="ExternalPlayer" audio="false" video="true">\n')
            f.write('            <filename>'+PLAYERCFFILE4+'</filename>\n')
            f.write('            <hidexbmc>true</hidexbmc>\n')
            f.write('            <playcountminimumtime>120</playcountminimumtime>\n')
            f.write('         </player>\n')
            PLAYERCFFILE5     = wiz.getS('PLAYERCFFILE5')
            PLAYERCFNAME5     = wiz.getS('PLAYERCFNAME5')
            f.write('         <player name="'+PLAYERCFNAME5+'" type="ExternalPlayer" audio="false" video="true">\n')
            f.write('            <filename>'+PLAYERCFFILE5+'</filename>\n')
            f.write('            <hidexbmc>true</hidexbmc>\n')
            f.write('            <playcountminimumtime>120</playcountminimumtime>\n')
            f.write('         </player>\n')
            PLAYERCFFILE6     = wiz.getS('PLAYERCFFILE6')
            PLAYERCFNAME6     = wiz.getS('PLAYERCFNAME6')
            f.write('         <player name="'+PLAYERCFNAME6+'" type="ExternalPlayer" audio="false" video="true">\n')
            f.write('            <filename>'+PLAYERCFFILE6+'</filename>\n')
            f.write('            <hidexbmc>true</hidexbmc>\n')
            f.write('            <playcountminimumtime>120</playcountminimumtime>\n')
            f.write('         </player>\n')
            PLAYERCFFILE7     = wiz.getS('PLAYERCFFILE7')
            PLAYERCFNAME7     = wiz.getS('PLAYERCFNAME7')
            f.write('         <player name="'+PLAYERCFNAME7+'" type="ExternalPlayer" audio="false" video="true">\n')
            f.write('            <filename>'+PLAYERCFFILE7+'</filename>\n')
            f.write('            <hidexbmc>true</hidexbmc>\n')
            f.write('            <playcountminimumtime>120</playcountminimumtime>\n')
            f.write('         </player>\n')
            PLAYERCFFILE8     = wiz.getS('PLAYERCFFILE8')
            PLAYERCFNAME8     = wiz.getS('PLAYERCFNAME8')
            f.write('         <player name="'+PLAYERCFNAME8+'" type="ExternalPlayer" audio="false" video="true">\n')
            f.write('            <filename>'+PLAYERCFFILE8+'</filename>\n')
            f.write('            <hidexbmc>true</hidexbmc>\n')
            f.write('            <playcountminimumtime>120</playcountminimumtime>\n')
            f.write('         </player>\n')
        ##################
        #'''
        if xbmc.getCondVisibility('system.platform.windows'): 
            # vlc x64 
            if os.path.isfile(xbmc.translatePath('C:/Program Files/VideoLAN/VLC/vlc.exe')):
                f.write('         <player name="VLC" type="ExternalPlayer" audio="false" video="true">\n')
                f.write('            <filename>C:\Program Files\VideoLAN\VLC\vlc.exe</filename>\n')
                f.write('            <args>--play-and-exit --video-on-top --fullscreen "{1}"</args>\n')
                f.write('            <hidexbmc>false</hidexbmc>\n')
                f.write('            <hideconsole>false</hideconsole>\n')
                f.write('            <hidecursor>false</hidecursor>\n')
                f.write('            <warpcursor>none</warpcursor>\n')
                f.write('         </player>\n')
            # vlc x86
            if os.path.isfile(xbmc.translatePath('C:/Program Files (x86)/VideoLAN/VLC/vlc.exe')):
                f.write('         <player name="VLC" type="ExternalPlayer" audio="false" video="true">\n')
                f.write('            <filename>C:\Program Files (x86)\VideoLAN\VLC\vlc.exe</filename>\n')
                f.write('            <args>--play-and-exit --video-on-top --fullscreen "{1}"</args>\n')
                f.write('            <hidexbmc>false</hidexbmc>\n')
                f.write('            <hideconsole>false</hideconsole>\n')
                f.write('            <hidecursor>false</hidecursor>\n')
                f.write('            <warpcursor>none</warpcursor>\n')
                f.write('         </player>\n')
            # MPC x64
            if os.path.isfile(xbmc.translatePath('C:/Program Files/MPC-HC64/mpc-hc64.exe')):
                f.write('         <player name="Media Player Classic x64" type="ExternalPlayer" audio="false" video="true">\n')
                f.write('            <filename>C:\Program Files\MPC-HC64\mpc-hc64.exe</filename>\n')
                f.write('            <args>"{1}" /fullscreen /close</args>\n')
                f.write('            <hidexbmc>true</hidexbmc>\n')
                f.write('            <hideconsole>true</hideconsole>\n')
                f.write('            <hidecursor>false</hidecursor>\n')
                f.write('            <warpcursor>none</warpcursor>\n')
                f.write('         </player>\n')
            # MPC x86
            if os.path.isfile(xbmc.translatePath('C:/Program Files/MPC-HC/mpc-hc.exe')):
                f.write('         <player name="Media Player Classic" type="ExternalPlayer" audio="false" video="true">\n')
                f.write('            <filename>C:\Program Files\MPC-HC\mpc-hc.exe</filename>\n')
                f.write('            <args>"{1}" /fullscreen /close</args>\n')
                f.write('            <hidexbmc>true</hidexbmc>\n')
                f.write('            <hideconsole>true</hideconsole>\n')
                f.write('            <hidecursor>false</hidecursor>\n')
                f.write('            <warpcursor>none</warpcursor>\n')
                f.write('         </player>\n')
            # MPC-KLite x64
            if os.path.isfile(xbmc.translatePath('C:/Program Files (x86)/K-Lite Codec Pack/MPC-HC64/mpc-hc64.exe')):
                f.write('         <player name="MPC-KLite x64" type="ExternalPlayer" audio="false" video="true">\n')
                f.write('            <filename>C:\Program Files (x86)\K-Lite Codec Pack\MPC-HC64\mpc-hc64.exe</filename>\n')
                f.write('            <args>"{1}" /fullscreen /close</args>\n')
                f.write('            <hidexbmc>true</hidexbmc>\n')
                f.write('            <hideconsole>true</hideconsole>\n')
                f.write('            <hidecursor>false</hidecursor>\n')
                f.write('            <warpcursor>none</warpcursor>\n')
                f.write('         </player>\n')
            # MPC-KLite x86
            if os.path.isfile(xbmc.translatePath('C:/Program Files/K-Lite Codec Pack/MPC-HC/mpc-hc.exe')): 
                f.write('         <player name="MPC-KLite" type="ExternalPlayer" audio="false" video="true">\n')
                f.write('            <filename>C:\Program Files\K-Lite Codec Pack\MPC-HC\mpc-hc.exe</filename>\n')
                f.write('            <args>"{1}" /fullscreen /close</args>\n')
                f.write('            <hidexbmc>true</hidexbmc>\n')
                f.write('            <hideconsole>true</hideconsole>\n')
                f.write('            <hidecursor>false</hidecursor>\n')
                f.write('            <warpcursor>none</warpcursor>\n')
                f.write('         </player>\n')
            # ffmpeg
            #'''
            if os.path.isfile(xbmc.translatePath('C:/utils/ffmpeg.exe')): 
                f.write('         <player name="Record ffmpeg" type="ExternalPlayer" audio="false" video="true">\n')
                f.write('            <filename>C:\\utils\\ffmpeg.exe</filename> \n')
                f.write('            <args>-i "{1}" -y -c copy -t 4:00:00 c:\pvr_ffmpeg.ts</args>\n')
                f.write('            <hidexbmc>false</hidexbmc>\n')
                f.write('            <hideconsole>true</hideconsole>\n')
                f.write('            <hidecursor>false</hidecursor>\n')
                f.write('            <warpcursor>none</warpcursor>\n')
                f.write('            <playonestackitem>true</playonestackitem>\n')
                f.write('         </player>\n')
                f.write('         <player name="Play with ffmpeg" type="ExternalPlayer" audio="false" video="true">\n')
                f.write('            <filename>C:\\utils\\ffmpeg.exe</filename>\n')
                f.write('            <args>"{1}" /fullscreen /close</args>\n')
                f.write('            <hidexbmc>false</hidexbmc>\n')
                f.write('            <hideconsole>false</hideconsole>\n')
                f.write('            <hidecursor>false</hidecursor>\n')
                f.write('            <warpcursor>none</warpcursor>\n')
                f.write('            <playonestackitem>true</playonestackitem>\n')
                f.write('         </player>\n')
            #'''
        #
        f.write('    </players>\n')
        f.write('    \n')
        '''
        f.write('    <rules action="overwrite">\n')
        f.write('<!--<rule protocols="nfs|smb" player="dvdplayer"></rule>-->\n')
        f.write('<!-- change the default player below -->\n')
        f.write('<!-- uncomment to make play the default player-->\n')
        f.write('<!--<rule video="true" player="play"></rule>-->\n')
        f.write('<!-- uncomment to make record the default player-->\n')
        f.write('<!-- <rule video="true" player="record"></rule>-->\n')
        f.write('<!--uncomment to make external player the default player -->\n')
        f.write('<!--<rule video="true" player="external player"></rule>-->\n')
        f.write('<!--uncomment to make stream the default player-->\n')
        f.write('<!--<rule video="true" player="stream"></rule>-->\n')
        f.write('    </rules>\n')
        '''
        f.write('</playercorefactory>\n')
        f.write('\n')
    f.close()
################################################################################
# browse  play url directly from ini - search is wip cant filter results.  would like to view folder.list too.
################################################################################
def ini_search():
    dialog = xbmcgui.Dialog()
    what = dialog.input("Search")
    if what:
        #return searchthistitle(what)
        return ini_browse(what)
def ini_rename():
    f = xbmcvfs.File(addonini_tvgfs,"rb")
    data = f.read()
    f.close()
    name_sub = re.findall('(.*?)=(.*)',data)
    name_sub = sorted(name_sub, key=lambda x: x[0].lower())
    name_sub = [list(i) for i in name_sub]
    while True:
        actions = ["Rename Channel Below"] + ["%s [COLOR dimgrey]%s[/COLOR]" % (x[0],x[1]) for x in name_sub]
        #actions = ["Add","Remove"] + ["%s [COLOR dimgrey]%s[/COLOR]" % (x[0],x[1]) for x in name_sub]
        d = xbmcgui.Dialog()
        action = d.select("Rename Channel",actions)
        if action == -1: # close
            break
        elif action == 0: # add channel
            break
        elif action == 1: # add channel
            f = xbmcvfs.File(addonini_tvgfs,"rb")
            data = f.read()
            f.close()
            name_sub = re.findall('(.*?)=(.*)',data)
            name_sub = sorted(name_sub, key=lambda x: x[0].lower())
            name_sub = [list(i) for i in name_sub]
            new_name = d.input("Name (%s)" % actions[action],name_sub[action-2][0])
            if new_name:
                name_sub[action-2][0] = new_name
            new_url = d.input("Url (%s)" % actions[action],name_sub[action-2][1])
            if new_url:
                name_sub[action-2][1] = new_url
def ini_browse(what=None):
    #if not what: what =''
    f = xbmcvfs.File(addonini_tvgfs,"rb")
    data = f.read()
    f.close()
    name_sub = re.findall('(.*?)=(.*)',data)
    name_sub = sorted(name_sub, key=lambda x: x[0].lower())
    name_sub = [list(i) for i in name_sub]
    while True:
        #actions = ["Add","Remove","Rename","Search"] + ["%s [COLOR dimgrey]%s[/COLOR]" % (x[0],x[1]) for x in name_sub]
        actions = ["Add","Remove"] + ["%s [COLOR dimgrey]%s[/COLOR]" % (x[0],x[1]) for x in name_sub]
        d = xbmcgui.Dialog()
        action = d.select("Play from ini",actions)
        if action == -1: # close
            break
        elif action == 0: # add channel
            name = d.input("Name")
            if not name:
                break
            url = d.input("Url")
            if not url:
                break
            name_sub.append((name,url))
            f = xbmcvfs.File(addonini_tvgfs,"wb")
            for (name,url) in name_sub:
                s = "%s=%s\n" % (name,url)
                f.write(s)
            f.close()
        elif action == 1: #remove
            names = ["%s [COLOR dimgrey]%s[/COLOR]" % (x[0],x[1]) for x in name_sub]
            which = d.multiselect("Remove",names)
            name_sub = [v for i, v in enumerate(name_sub) if i not in which]
            f = xbmcvfs.File(addonini_tvgfs,"wb")
            for (name,url) in name_sub:
                s = "%s=%s\n" % (name,url)
                f.write(s)
            f.close()
        else: # Play
            xbmc.Player().stop
            url = name_sub[action-2][1]
            xbmc.Player().play(item=url)
            return True
        '''
        elif action == 2:# rename
            ini_rename()
            # or
            f = xbmcvfs.File(addonini_tvgfs,"rb")
            data = f.read()
            f.close()
            name_sub = re.findall('(.*?)=(.*)',data)
            name_sub = sorted(name_sub, key=lambda x: x[0].lower())
            name_sub = [list(i) for i in name_sub]
            new_name = d.input("Name (%s)" % actions[action],name_sub[action-2][0])
            if new_name:
                name_sub[action-2][0] = new_name
            new_url = d.input("Url (%s)" % actions[action],name_sub[action-2][1])
            if new_url:
                name_sub[action-2][1] = new_url
        elif action == 3:# search
            ini_search()
        '''



################################################################################
# copy data backup failsafes - restore backups of your pre set tvgfs files if absent
################################################################################
def copy_failsafes():
    if not os.path.exists(basePath): os.mkdir(basePath)
    if not os.path.exists(basePath_tvgfs): os.mkdir(basePath_tvgfs)
    DP.create(skin,'[COLOR green][B]COPY:[/B][/COLOR] %s' % copysrc, '', '[COLOR blue]Please Wait[/COLOR]')
    # copy the main root to user_data but if directory already exists we need failsafes
    copy_addondata(xbmc.translatePath(os.path.join(copysrc,'copy_tvgfs')),xbmc.translatePath(os.path.join('special://profile', 'addon_data', ADDONID_TVGFS)))
    copy_addondata(xbmc.translatePath(os.path.join(copysrc,'copy_tvgfs_skin')),xbmc.translatePath(os.path.join('special://profile', 'addon_data', ADDONID)))
    #os.mkdir(xbmc.translatePath(os.path.join('special://profile', 'addon_data', ADDONID,'resources')))
    copy_addondata(xbmc.translatePath(os.path.join(copysrc,'logos')),xbmc.translatePath(os.path.join('special://profile', 'addon_data', ADDONID,'resources','logos')))
    copy_addondata(xbmc.translatePath(os.path.join(copysrc,'playlists')),xbmc.translatePath(os.path.join('special://profile', 'addon_data', ADDONID,'resources','playlists')))
    if not skinfolder == addonPath:
        if not os.path.exists(xbmc.translatePath(os.path.join(skinfolder,'resources','skins'))):
            copy_addondata(xbmc.translatePath(os.path.join(copysrc,'skins')),xbmc.translatePath(os.path.join(skinfolder,'resources','skins')))
            copy_addondata(xbmc.translatePath(os.path.join(copysrc,'skins',skin)),xbmc.translatePath(os.path.join(skinfolder,'resources','skins',skin)))
            #copy_addondata(xbmc.translatePath(os.path.join(copysrc,'skins')),xbmc.translatePath(os.path.join('special://profile', 'addon_data', ADDONID,'resources','skins')))
            #copy_addondata(xbmc.translatePath(os.path.join(copysrc,'skins',skin)),xbmc.translatePath(os.path.join('special://profile', 'addon_data', ADDONID,'resources','skins',skin)))
    DP.close()
################################################################################
# copy data backup failsafes - restore backups of your pre set tvgfs files if absent
################################################################################
def copy_addondata(src,dest):
    if os.path.exists(src):
        thissrc = os.path.split(src[:-1])[1]
        DP.update(0, skin, '[COLOR green][B]COPYING:[/B][/COLOR]  '+thissrc)
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dest, item)
            if os.path.isdir(s):
                if not os.path.exists(d): 
                    if not d.startswith('_'):
                        shutil.copytree(s, d, symlinks=False, ignore=None)
            else: # file
                if not os.path.exists(d):
                    #if not '_' in d:
                    if not item.startswith('_'): 
                        shutil.copy2(s, d)
################################################################################
##### Run
################################################################################
# extra for skins
ACTION_PREVIOUS_MENU            =  900    ## ESC action
ACTION_NAV_BACK                 =  901    ## Backspace action
ACTION_SELECT_ITEM              =  902    ## Number Pad Enter
ACTION_MOUSE_LEFT_CLICK         =  903    ## Mouse left click
if __name__ == '__main__':
    if len(sys.argv) > 1:
        mode = sys.argv[1]
        ###########################################
        #### TOGGLE ADDON SETTINGS
        ###########################################
        if mode   == 'set_skin_vars':          set_skin_vars()
        elif mode == 'ini_search':             ini_search()
        elif mode == 'ini_browse':             ini_browse(what=None)
        elif mode == 'gui_run_custom_skinxml': gui_run_custom_skinxml('script-tvguide-vod-tv.xml')# VOD OR OPEN A GUI XML
        elif mode == 'refresh_ini':            refresh_ini()#; _reopen()# refresh inis
        elif mode == 'gui_run_extras':         gui_run_extras()# open various settings gui
        elif mode == 'gui_toggle_settings':    gui_toggle_settings()# toggle TVGFS settings on the fly
        elif mode == 'gui_tvgfsmaintenence':   gui_tvgfsmaintenence()
        ###########################################
        #### TOGGLE ADDON SETTINGS
        ###########################################
        elif mode == 'reopen_guide':           _reopen()# Reopen Guide failsafe button if crash
        elif mode == 'open_cake_settings':     _open_setting(ADDONID)# Open cake settings
        elif mode == 'open_tvgfs_settings':    _open_setting(ADDONID_TVGFS)# Open core settings
        elif mode == 'run_skin_addon':         _open_addon(ADDONID)# Run cake addon
        elif mode == 'run_tvgfs_addon':        _open_addon(ADDONID_TVGFS)# Run core addon
        ###########################################
        #### TOGGLE SKIN SETTINGS VIA WRITING TO XML
        ###########################################
        elif mode == 'toggle_vertical':          toggle_vertical();_reopen()  # Horizontal Reverse the description area with the epg columns
        elif mode == 'toggle_horizontal':        toggle_horizontal();_reopen() # Vertical Reverse the description area with videowindow
        elif mode == 'toggle_fade':              gui_fade_toggle()
        elif mode == 'toggle_1080':              toggle_1080() # toggle 1080p
        elif mode == 'toggle_jarvis_strings':    toggle_jarvis_strings()# 16 to 17 toggle
        ###########################################
        #### RESET DATABASE
        ###########################################
        elif mode == 'gui_resetdatabase':         gui_resetdatabase() # Reset Database
        elif mode == 'resetdatabase_epgdata':     xbmc.executebuiltin('RunScript('+refreshdatabase+', 1)');_reopen()# Reset Database Reset EPG Data
        elif mode == 'resetdatabase_everything':  xbmc.executebuiltin('RunScript('+refreshdatabase+', 2)');_reopen()# Reset Database Everything
        elif mode == 'resetdatabase_imagecache':  xbmc.executebuiltin('RunScript('+refreshdatabase+', 3)');_reopen()# Reset Database  Image cache
        elif mode == 'resetdatabase_logodbcache': xbmc.executebuiltin('RunScript('+refreshdatabase+', 4)');_reopen()# Delete TheLogoDB.com Cache
        ###########################################
        #### EXTRA XML GUIS
        ###########################################
        elif mode == 'gui_set_tvgfs_settings':    gui_set_tvgfs_settings()# Set skin settings (installer)
        elif mode == 'gui_LogViewer':             gui_LogViewer()# VIEW LOG AND XML FILES
        elif mode == 'gui_autoConfig':            gui_autoConfig()# advancedsettings.xml gui
        elif mode == 'help':                      gui_helpMenu()# read help files
        elif mode == 'writeplayerfactorycore':    _writeplayerfactorycore()
        elif mode == 'playm3u':                   gui_playm3u(playlistFile=None)
        elif mode == '_enable':                   _enable()
        elif mode == '_run_exe':                  _run_exe(name=None, url=None)
        #else:  set_skin_vars();gui_set_tvgfs_settings()
    elif len(sys.argv) > 0:
        #set_skin_vars()
        gui_set_tvgfs_settings()
    #xbmcplugin.endOfDirectory(int(sys.argv[1]))
    
