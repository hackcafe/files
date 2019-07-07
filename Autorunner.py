import shutil, os, sys


windows = "%APPDATA%/Microsoft/Windows/Start Menu/Programs/Startup"

mac = "/Library/LaunchDaemons/"

linux = "/etc/init.d/"

def windowsAuto(loc, startup):
    shutil.copy2(loc, startup)



def macAuto(loc, plist, startDir):
    root = os.getcwd()

    os.chdir(loc)

    os.system("sudo vim " + plist)

    with open(plist, "w") as plistFile:
        plistFile.write('''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "
http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
  <dict>
    <key>EnvironmentVariables</key>
    <dict>
      <key>PATH</key>
      <string>/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:</string>
    </dict>
    <key>Label</key>
    <string>com.startup</string>
    <key>Program</key>
    <string>/Users/admin/Scripts/startup/startup.sh</string>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <false/>
    <key>LaunchOnlyOnce</key>        
    <true/>
    <key>StandardOutPath</key>
    <string>/tmp/startup.stdout</string>
    <key>StandardErrorPath</key>
    <string>/tmp/startup.stderr</string>
    <key>UserName</key>
    <string>admin</string>
    <key>GroupName</key>
    <string>admin</string>
    <key>InitGroups</key>
    <true/>
  </dict>
</plist>''')

    os.system("sudo launchctl load -w /Library/LaunchDaemons/com.startup.plist")

    shutil.copy2(loc, startDir)


def linuxAuto(loc, startDir, name):
    shutil.copy2(loc, startDir)
    os.system("chmod 755 " + startDir + "/" + name)

    
    


    
