# Music Feature Setup Guide

## Prerequisites

Untuk menggunakan fitur music bot, Anda memerlukan:

### 1. FFmpeg
FFmpeg adalah dependency utama untuk audio streaming.

**Windows - Install via WinGet:**
```bash
winget install Gyan.FFmpeg
```

**Windows - Download Manual:**
1. Download dari: https://ffmpeg.org/download.html
2. Extract ke folder, contohnya: `C:\ffmpeg`
3. Add ke PATH atau gunakan full path

**Windows - Verify Installation:**
```bash
ffmpeg -version
```

**macOS:**
```bash
brew install ffmpeg
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install ffmpeg
```

**Linux (Fedora):**
```bash
sudo dnf install ffmpeg
```

### 2. Python Dependencies
```bash
pip install -r requirements.txt
```

Atau install secara manual:
```bash
pip install discord.py[voice]==2.3.2
pip install PyNaCl==1.5.0
pip install yt-dlp>=2024.03.10
```

## Troubleshooting

### Error: "FFmpeg not installed"
- Pastikan FFmpeg sudah di-install dan di-PATH
- Atau ubah path di `music_commands.py` ke full path FFmpeg

### Error: "No module named 'voice'"
```bash
pip install discord.py[voice]==2.3.2
pip install PyNaCl
```

### Bot tidak bisa connect ke voice channel
- Pastikan bot punya permission: `CONNECT` dan `SPEAK` di voice channel
- Pastikan user yang call command sudah di voice channel

## Testing

Untuk test music feature:
1. Join voice channel
2. Run `/play <song name>`
3. Bot akan search di YouTube dan play

## Fitur yang tersedia

| Command | Deskripsi |
|---------|-----------|
| `/play <query>` | Play lagu dari YouTube |
| `/pause` | Pause musik |
| `/resume` | Resume musik |
| `/stop` | Stop dan disconnect |
| `/skip` | Skip ke lagu berikutnya |
| `/queue` | Lihat daftar queue |

## Notes

- Bot butuh ~500MB+ untuk streaming quality baik
- Connection ke YouTube harus stable
- yt-dlp akan di-update otomatis untuk compatibility
