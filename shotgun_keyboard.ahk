#NoEnv
#SingleInstance Force
SendMode Input
SetWorkingDir %A_ScriptDir%

SoundsDir := A_ScriptDir "\Sounds"
SoundFiles := []

Loop, Files, %SoundsDir%\*.mp3
    SoundFiles.Push(A_LoopFileFullPath)

if (SoundFiles.Length() = 0) {
    MsgBox, No sound files found in %SoundsDir%
    ExitApp
}

PlayRandomSound() {
    global SoundFiles
    Random, idx, 1, % SoundFiles.Length()
    SoundPlay, % SoundFiles[idx]
    return
}

~*a::PlayRandomSound()
~*b::PlayRandomSound()
~*c::PlayRandomSound()
~*d::PlayRandomSound()
~*e::PlayRandomSound()
~*f::PlayRandomSound()
~*g::PlayRandomSound()
~*h::PlayRandomSound()
~*i::PlayRandomSound()
~*j::PlayRandomSound()
~*k::PlayRandomSound()
~*l::PlayRandomSound()
~*m::PlayRandomSound()
~*n::PlayRandomSound()
~*o::PlayRandomSound()
~*p::PlayRandomSound()
~*q::PlayRandomSound()
~*r::PlayRandomSound()
~*s::PlayRandomSound()
~*t::PlayRandomSound()
~*u::PlayRandomSound()
~*v::PlayRandomSound()
~*w::PlayRandomSound()
~*x::PlayRandomSound()
~*y::PlayRandomSound()
~*z::PlayRandomSound()

~*1::PlayRandomSound()
~*2::PlayRandomSound()
~*3::PlayRandomSound()
~*4::PlayRandomSound()
~*5::PlayRandomSound()
~*6::PlayRandomSound()
~*7::PlayRandomSound()
~*8::PlayRandomSound()
~*9::PlayRandomSound()
~*0::PlayRandomSound()

~*Space::PlayRandomSound()
~*Enter::PlayRandomSound()
~*Tab::PlayRandomSound()
~*Backspace::PlayRandomSound()
~*Escape::ExitApp

~*F1::PlayRandomSound()
~*F2::PlayRandomSound()
~*F3::PlayRandomSound()
~*F4::PlayRandomSound()
~*F5::PlayRandomSound()
~*F6::PlayRandomSound()
~*F7::PlayRandomSound()
~*F8::PlayRandomSound()
~*F9::PlayRandomSound()
~*F10::PlayRandomSound()
~*F11::PlayRandomSound()
~*F12::PlayRandomSound()

~*Up::PlayRandomSound()
~*Down::PlayRandomSound()
~*Left::PlayRandomSound()
~*Right::PlayRandomSound()

~*LShift::PlayRandomSound()
~*RShift::PlayRandomSound()
~*LControl::PlayRandomSound()
~*RControl::PlayRandomSound()
~*LAlt::PlayRandomSound()
~*RAlt::PlayRandomSound()

~*LWin::PlayRandomSound()
~*RWin::PlayRandomSound()

~*AppsKey::PlayRandomSound()

~*Insert::PlayRandomSound()
~*Delete::PlayRandomSound()
~*Home::PlayRandomSound()
~*End::PlayRandomSound()
~*PgUp::PlayRandomSound()
~*PgDn::PlayRandomSound()

~*Numpad0::PlayRandomSound()
~*Numpad1::PlayRandomSound()
~*Numpad2::PlayRandomSound()
~*Numpad3::PlayRandomSound()
~*Numpad4::PlayRandomSound()
~*Numpad5::PlayRandomSound()
~*Numpad6::PlayRandomSound()
~*Numpad7::PlayRandomSound()
~*Numpad8::PlayRandomSound()
~*Numpad9::PlayRandomSound()
~*NumpadDot::PlayRandomSound()
~*NumpadDiv::PlayRandomSound()
~*NumpadMult::PlayRandomSound()
~*NumpadSub::PlayRandomSound()
~*NumpadAdd::PlayRandomSound()
~*NumpadEnter::PlayRandomSound()

~*PrintScreen::PlayRandomSound()
~*ScrollLock::PlayRandomSound()
~*Pause::PlayRandomSound()

~*CapsLock::PlayRandomSound()
~*NumLock::PlayRandomSound()

~*Browser_Back::PlayRandomSound()
~*Browser_Forward::PlayRandomSound()
~*Browser_Refresh::PlayRandomSound()
~*Browser_Stop::PlayRandomSound()
~*Browser_Search::PlayRandomSound()
~*Browser_Favorites::PlayRandomSound()
~*Browser_Home::PlayRandomSound()
~*Volume_Mute::PlayRandomSound()
~*Volume_Down::PlayRandomSound()
~*Volume_Up::PlayRandomSound()
~*Media_Next::PlayRandomSound()
~*Media_Prev::PlayRandomSound()
~*Media_Stop::PlayRandomSound()
~*Media_Play_Pause::PlayRandomSound()
~*Launch_Mail::PlayRandomSound()
~*Launch_Media::PlayRandomSound()
~*Launch_App1::PlayRandomSound()
~*Launch_App2::PlayRandomSound()

~*;::PlayRandomSound()
~*=::PlayRandomSound()
~*Comma::PlayRandomSound()
~*-::PlayRandomSound()
~*.::PlayRandomSound()
~/::PlayRandomSound()
~*Accent::PlayRandomSound()
~*[::PlayRandomSound()
~*]::PlayRandomSound()
~*Backslash::PlayRandomSound()
~*Quote::PlayRandomSound()

Return