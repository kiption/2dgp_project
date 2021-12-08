; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{2C097C5B-DF44-40F6-8B6C-CA3572C3DD9D}
AppName=2dgp_project
AppVersion=1.0
;AppVerName=2dgp_project 1.0
AppPublisher=KPU
AppPublisherURL=https://www.kpu.ac.kr/
AppSupportURL=https://www.kpu.ac.kr/
AppUpdatesURL=https://www.kpu.ac.kr/
DefaultDirName={autopf}\2dgp_project_2018180033
DisableProgramGroupPage=yes
; Uncomment the following line to run in non administrative install mode (install for current user only.)
;PrivilegesRequired=lowest
OutputDir=D:\pratice\2dgp_project\dist
OutputBaseFilename=my2dsetup
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "D:\pratice\2dgp_project\dist\mygame.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\pratice\2dgp_project\dist\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{autoprograms}\2dgp_project"; Filename: "{app}\mygame.exe"
Name: "{autodesktop}\2dgp_project"; Filename: "{app}\mygame.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\mygame.exe"; Description: "{cm:LaunchProgram,2dgp_project}"; Flags: nowait postinstall skipifsilent
