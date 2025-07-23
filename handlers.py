from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def build_quality_buttons(formats):
    """
    Builds inline keyboard with available video qualities + audio option.
    Filters out duplicate resolutions.
    """
    seen = set()
    buttons = []

    for f in formats:
        if f.get('vcodec') != 'none':
            res = f.get('format_note') or f.get('height')
            if res in seen:
                continue
            seen.add(res)
            size = f.get('filesize') or f.get('filesize_approx') or 0
            size_mb = round(size / (1024 * 1024), 1) if size else "?"
            label = f"{res} ({size_mb} MB)"
            buttons.append(
                [InlineKeyboardButton(label, callback_data=f"video|{f['format_id']}")]
            )

    # Add audio-only option
    buttons.append(
        [InlineKeyboardButton("🎵 Audio Only", callback_data="audio|bestaudio")]
    )

    return InlineKeyboardMarkup(buttons)


def build_admin_panel(allow_all: bool):
    """
    Builds inline admin panel with toggle & caption options.
    """
    toggle_label = "✅ Allow All: ON" if allow_all else "🚫 Allow All: OFF"
    buttons = [
        [InlineKeyboardButton(toggle_label, callback_data="toggle_allow_all")],
        [InlineKeyboardButton("👥 Approved Users", callback_data="approved_users")],
        [InlineKeyboardButton("📝 Set Progress Caption", callback_data="set_progress_caption")],
        [InlineKeyboardButton("📝 Set File Caption", callback_data="set_file_caption")],
        [InlineKeyboardButton("📜 View Queue", callback_data="view_queue")]
    ]
    return InlineKeyboardMarkup(buttons)
