# SCP-079-CONFIG - Manage the settings of each bot
# Copyright (C) 2019-2020 SCP-079 <https://scp-079.org>
#
# This file is part of SCP-079-CONFIG.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import logging
from copy import deepcopy
from typing import Optional

from pyrogram import Client, InlineKeyboardButton, InlineKeyboardMarkup

from .. import glovar
from .channel import share_data
from .etc import button_data, code, general_link, get_now, lang, thread
from .file import save
from .telegram import edit_message_text, send_message

# Enable logging
logger = logging.getLogger(__name__)


def button_captcha(config: dict) -> Optional[InlineKeyboardMarkup]:
    # Get inline markup for CAPTCHA
    markup = None
    try:
        markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=lang("default_config"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('default'))}",
                        callback_data=button_data(
                            action=(lambda x: "default" if not x else "none")(config.get("default")),
                            action_type=None,
                            data=not config.get("default")
                        )
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("delete"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('delete'))}",
                        callback_data=button_data("delete", None, not config.get("delete"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("restrict"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('restrict'))}",
                        callback_data=button_data("restrict", None, not config.get("restrict"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("ban"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('ban'))}",
                        callback_data=button_data("ban", None, not config.get("ban"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("forgive"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('forgive'))}",
                        callback_data=button_data("forgive", None, not config.get("forgive"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("hint"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('hint'))}",
                        callback_data=button_data("hint", None, not config.get("hint"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("pass"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('pass'))}",
                        callback_data=button_data("pass", None, not config.get("pass"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("pin"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('pin'))}",
                        callback_data=button_data("pin", None, not config.get("pin"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("qns"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('qns'))}",
                        callback_data=button_data("qns", None, not config.get("qns"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("manual"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('manual'))}",
                        callback_data=button_data("manual", None, not config.get("manual"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("commit"),
                        callback_data=button_data("commit")
                    )
                ]
            ]
        )
    except Exception as e:
        logger.warning(f"Button captcha error: {e}", exc_info=True)

    return markup


def button_clean(config: dict) -> Optional[InlineKeyboardMarkup]:
    # Get inline markup for CLEAN
    markup = None
    try:
        markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=lang("default_config"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('default'))}",
                        callback_data=button_data(
                            action=(lambda x: "default" if not x else "none")(config.get("default")),
                            action_type=None,
                            data=not config.get("default")
                        )
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("delete"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('delete'))}",
                        callback_data=button_data("delete", None, not config.get("delete"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("restrict"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('restrict'))}",
                        callback_data=button_data("restrict", None, not config.get("restrict"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("friend"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('friend'))}",
                        callback_data=button_data("friend", None, not config.get("friend"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("clean"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('clean'))}",
                        callback_data=button_data("clean", None, not config.get("clean"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=f"{lang('con')} {(lambda x: '■' if x else '□️')(config.get('con'))}",
                        callback_data=button_data("con", None, not config.get("con"))
                    ),
                    InlineKeyboardButton(
                        text=f"{lang('loc')} {(lambda x: '■' if x else '□️')(config.get('loc'))}",
                        callback_data=button_data("loc", None, not config.get("loc"))
                    ),
                    InlineKeyboardButton(
                        text=f"{lang('vdn')} {(lambda x: '■' if x else '□️')(config.get('vdn'))}",
                        callback_data=button_data("vdn", None, not config.get("vdn"))
                    ),
                    InlineKeyboardButton(
                        text=f"{lang('voi')} {(lambda x: '■' if x else '□️')(config.get('voi'))}",
                        callback_data=button_data("voi", None, not config.get("voi"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=f"{lang('ast')} {(lambda x: '■' if x else '□️')(config.get('ast'))}",
                        callback_data=button_data("ast", None, not config.get("ast"))
                    ),
                    InlineKeyboardButton(
                        text=f"{lang('aud')} {(lambda x: '■' if x else '□️')(config.get('aud'))}",
                        callback_data=button_data("aud", None, not config.get("aud"))
                    ),
                    InlineKeyboardButton(
                        text=f"{lang('bmd')} {(lambda x: '■' if x else '□️')(config.get('bmd'))}",
                        callback_data=button_data("bmd", None, not config.get("bmd"))
                    ),
                    InlineKeyboardButton(
                        text=f"{lang('doc')} {(lambda x: '■' if x else '□️')(config.get('doc'))}",
                        callback_data=button_data("doc", None, not config.get("doc"))
                    )
                ],
                [


                    InlineKeyboardButton(
                        text=f"{lang('gam')} {(lambda x: '■' if x else '□️')(config.get('gam'))}",
                        callback_data=button_data("gam", None, not config.get("gam"))
                    ),
                    InlineKeyboardButton(
                        text=f"{lang('gif')} {(lambda x: '■' if x else '□️')(config.get('gif'))}",
                        callback_data=button_data("gif", None, not config.get("gif"))
                    ),
                    InlineKeyboardButton(
                        text=f"{lang('via')} {(lambda x: '■' if x else '□️')(config.get('via'))}",
                        callback_data=button_data("via", None, not config.get("via"))
                    ),
                    InlineKeyboardButton(
                        text=f"{lang('vid')} {(lambda x: '■' if x else '□️')(config.get('vid'))}",
                        callback_data=button_data("vid", None, not config.get("vid"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=f"{lang('ser')} {(lambda x: '■' if x else '□️')(config.get('ser'))}",
                        callback_data=button_data("ser", None, not config.get("ser"))
                    ),
                    InlineKeyboardButton(
                        text=f"{lang('sti')} {(lambda x: '■' if x else '□️')(config.get('sti'))}",
                        callback_data=button_data("sti", None, not config.get("sti"))
                    ),
                    InlineKeyboardButton(
                        text=f"{lang('aff')} {(lambda x: '■' if x else '□️')(config.get('aff'))}",
                        callback_data=button_data("aff", None, not config.get("aff"))
                    ),
                    InlineKeyboardButton(
                        text=f"{lang('emo')} {(lambda x: '■' if x else '□️')(config.get('emo'))}",
                        callback_data=button_data("emo", None, not config.get("emo"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=f"{lang('exe')} {(lambda x: '■' if x else '□️')(config.get('exe'))}",
                        callback_data=button_data("exe", None, not config.get("exe"))
                    ),
                    InlineKeyboardButton(
                        text=f"{lang('iml')} {(lambda x: '■' if x else '□️')(config.get('iml'))}",
                        callback_data=button_data("iml", None, not config.get("iml"))
                    ),
                    InlineKeyboardButton(
                        text=f"{lang('pho')} {(lambda x: '■' if x else '□️')(config.get('pho'))}",
                        callback_data=button_data("pho", None, not config.get("pho"))
                    ),
                    InlineKeyboardButton(
                        text=f"{lang('sho')} {(lambda x: '■' if x else '□️')(config.get('sho'))}",
                        callback_data=button_data("sho", None, not config.get("sho"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=f"{lang('tgl')} {(lambda x: '■' if x else '□️')(config.get('tgl'))}",
                        callback_data=button_data("tgl", None, not config.get("tgl"))
                    ),
                    InlineKeyboardButton(
                        text=f"{lang('tgp')} {(lambda x: '■' if x else '□️')(config.get('tgp'))}",
                        callback_data=button_data("tgp", None, not config.get("tgp"))
                    ),
                    InlineKeyboardButton(
                        text=f"{lang('qrc')} {(lambda x: '■' if x else '□️')(config.get('qrc'))}",
                        callback_data=button_data("qrc", None, not config.get("qrc"))
                    ),
                    InlineKeyboardButton(
                        text=f"{lang('sde')} {(lambda x: '■' if x else '□️')(config.get('sde'))}",
                        callback_data=button_data("sde", None, not config.get("sde"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=f"{lang('tcl')} {(lambda x: '■' if x else '□️')(config.get('tcl'))}",
                        callback_data=button_data("tcl", None, not config.get("tcl"))
                    ),
                    InlineKeyboardButton(
                        text=f"{lang('ttd')} {(lambda x: '■' if x else '□️')(config.get('ttd'))}",
                        callback_data=button_data("ttd", None, not config.get("ttd"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("commit"),
                        callback_data=button_data("commit")
                    )
                ]
            ]
        )
    except Exception as e:
        logger.warning(f"Button clean error: {e}", exc_info=True)

    return markup


def button_lang(config: dict) -> Optional[InlineKeyboardMarkup]:
    # Get inline markup for LANG
    markup = None
    try:
        name_default = config.get("name") and config["name"].get("default")
        name_enable = config.get("name") and config["name"].get("enable")
        text_default = config.get("text") and config["text"].get("default")
        text_enable = config.get("text") and config["text"].get("enable")
        sticker_default = config.get("sticker") and config["sticker"].get("default")
        sticker_enable = config.get("sticker") and config["sticker"].get("enable")
        bio_default = config.get("bio") and config["bio"].get("default")
        bio_enable = config.get("bio") and config["bio"].get("enable")
        markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=lang("default_config"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('default'))}",
                        callback_data=button_data(
                            action=(lambda x: "default" if not x else "none")(config.get("default")),
                            action_type=None,
                            data=not config.get("default")
                        )
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("delete"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('delete'))}",
                        callback_data=button_data("delete", None, not config.get("delete"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("restrict"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('restrict'))}",
                        callback_data=button_data("restrict", None, not config.get("restrict"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("name_default"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(name_default)}",
                        callback_data=button_data("name", "default", name_default)
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("name_enable"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(name_enable)}",
                        callback_data=button_data("name", "enable", not name_enable)
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("text_default"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(text_default)}",
                        callback_data=button_data("text", "default", not text_default)
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("text_enable"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(text_enable)}",
                        callback_data=button_data("text", "enable", not text_enable)
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("sticker_default"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(sticker_default)}",
                        callback_data=button_data("sticker", "default", not sticker_default)
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("sticker_enable"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(sticker_enable)}",
                        callback_data=button_data("sticker", "enable", not sticker_enable)
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("bio_default"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(bio_default)}",
                        callback_data=button_data("bio", "default", not bio_default)
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("bio_enable"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(bio_enable)}",
                        callback_data=button_data("bio", "enable", not bio_enable)
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("spc"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('spc'))}",
                        callback_data=button_data("spc", None, not config.get("spc"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("spe"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('spe'))}",
                        callback_data=button_data("spe", None, not config.get("spe"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("commit"),
                        callback_data=button_data("commit")
                    )
                ]
            ]
        )
    except Exception as e:
        logger.warning(f"Button lang error: {e}", exc_info=True)

    return markup


def button_long(config: dict) -> Optional[InlineKeyboardMarkup]:
    # Get inline markup for LONG
    markup = None
    try:
        markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=lang("default_config"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('default'))}",
                        callback_data=button_data(
                            action=(lambda x: "default" if not x else "none")(config.get("default")),
                            action_type=None,
                            data=not config.get("default")
                        )
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("delete"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('delete'))}",
                        callback_data=button_data("delete", None, not config.get("delete"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("restrict"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('restrict'))}",
                        callback_data=button_data("restrict", None, not config.get("restrict"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("long_limit"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{config.get('limit', 1500)}",
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '-️' if x > 500 else '*')(config.get('limit', 1500))}",
                        callback_data=button_data(
                            action=(lambda x: "limit" if x > 500 else "none")(config.get("limit", 1500)),
                            action_type=None,
                            data=config.get("limit", 1500) - 500
                        )
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '+️' if x < 10000 else '*')(config.get('limit', 1500))}",
                        callback_data=button_data(
                            action=(lambda x: "limit" if x < 10000 else "none")(config.get("limit", 1500)),
                            action_type=None,
                            data=config.get("limit", 1500) + 500
                        )
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("commit"),
                        callback_data=button_data("commit")
                    )
                ]
            ]
        )
    except Exception as e:
        logger.warning(f"Button long error: {e}", exc_info=True)

    return markup


def button_noflood(config: dict) -> Optional[InlineKeyboardMarkup]:
    # Get inline markup for NOFLOOD
    markup = None
    try:
        markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=lang("default_config"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('default'))}",
                        callback_data=button_data(
                            action=(lambda x: "default" if not x else "none")(config.get("default")),
                            action_type=None,
                            data=not config.get("default")
                        )
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("delete"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('delete'))}",
                        callback_data=button_data("delete", None, not config.get("delete"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("restrict"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('restrict'))}",
                        callback_data=button_data("restrict", None, not config.get("restrict"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("noflood_time"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{config.get('time', 10)}",
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '-️' if x > 5 else '*')(config.get('time', 10))}",
                        callback_data=button_data(
                            action=(lambda x: "time" if x > 5 else "none")(config.get("time", 10)),
                            action_type=None,
                            data=config.get("time", 10) - 5
                        )
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '+️' if x < 60 else '*')(config.get('time', 10))}",
                        callback_data=button_data(
                            action=(lambda x: "time" if x < 60 else "none")(config.get("time", 10)),
                            action_type=None,
                            data=config.get("time", 10) + 5
                        )
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("noflood_limit"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{config.get('limit', 5)}",
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '-️' if x > 2 else '*')(config.get('limit', 5))}",
                        callback_data=button_data(
                            action=(lambda x: "limit" if x > 2 else "none")(config.get("limit", 5)),
                            action_type=None,
                            data=config.get("limit", 5) - 1
                        )
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '+️' if x < 20 else '*')(config.get('limit', 5))}",
                        callback_data=button_data(
                            action=(lambda x: "limit" if x < 20 else "none")(config.get("limit", 5)),
                            action_type=None,
                            data=config.get("limit", 5) + 1
                        )
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("noflood_purge"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('purge'))}",
                        callback_data=button_data("purge", None, not config.get("purge"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("commit"),
                        callback_data=button_data("commit")
                    )
                ]
            ]
        )
    except Exception as e:
        logger.warning(f"Button noflood error: {e}", exc_info=True)

    return markup


def button_noporn(config: dict) -> Optional[InlineKeyboardMarkup]:
    # Get inline markup for NOPORN
    markup = None
    try:
        markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=lang("default_config"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('default'))}",
                        callback_data=button_data(
                            action=(lambda x: "default" if not x else "none")(config.get("default")),
                            action_type=None,
                            data=not config.get("default")
                        )
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("delete"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('delete'))}",
                        callback_data=button_data("delete", None, not config.get("delete"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("restrict"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('restrict'))}",
                        callback_data=button_data("restrict", None, not config.get("restrict"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("noporn_channel"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('channel'))}",
                        callback_data=button_data("channel", None, not config.get("channel"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("commit"),
                        callback_data=button_data("commit")
                    )
                ]
            ]
        )
    except Exception as e:
        logger.warning(f"Button noporn error: {e}", exc_info=True)

    return markup


def button_nospam(config: dict) -> Optional[InlineKeyboardMarkup]:
    # Get inline markup for NOSPAM
    markup = None
    try:
        markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=lang("default_config"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('default'))}",
                        callback_data=button_data(
                            action=(lambda x: "default" if not x else "none")(config.get("default")),
                            action_type=None,
                            data=not config.get("default")
                        )
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("delete"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('delete'))}",
                        callback_data=button_data("delete", None, not config.get("delete"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("restrict"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('restrict'))}",
                        callback_data=button_data("restrict", None, not config.get("restrict"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("nick"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('nick'))}",
                        callback_data=button_data("nick", None, not config.get("nick"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("bio"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('bio'))}",
                        callback_data=button_data("bio", None, not config.get("bio"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("avatar"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('avatar'))}",
                        callback_data=button_data("avatar", None, not config.get("avatar"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("message"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('message'))}",
                        callback_data=button_data("message", None, not config.get("message"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("ocr"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('ocr'))}",
                        callback_data=button_data("ocr", None, not config.get("ocr"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("sticker"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('sticker'))}",
                        callback_data=button_data("sticker", None, not config.get("sticker"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("bot"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('bot'))}",
                        callback_data=button_data("bot", None, not config.get("bot"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("new"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('new'))}",
                        callback_data=button_data("new", None, not config.get("new"))
                    )
                ],
                # [
                #     InlineKeyboardButton(
                #         text=lang("deleter"),
                #         callback_data=button_data("none")
                #     ),
                #     InlineKeyboardButton(
                #         text=f"{(lambda x: '■' if x else '□️')(config.get('deleter'))}",
                #         callback_data=button_data("deleter", None, not config.get("deleter"))
                #     )
                # ],
                # [
                #     InlineKeyboardButton(
                #         text=lang("reporter"),
                #         callback_data=button_data("none")
                #     ),
                #     InlineKeyboardButton(
                #         text=f"{(lambda x: '■' if x else '□️')(config.get('reporter'))}",
                #         callback_data=button_data("reporter", None, not config.get("reporter"))
                #     )
                # ],
                # [
                #     InlineKeyboardButton(
                #         text=lang("scorer"),
                #         callback_data=button_data("none")
                #     ),
                #     InlineKeyboardButton(
                #         text=f"{(lambda x: '■' if x else '□️')(config.get('scorer'))}",
                #         callback_data=button_data("scorer", None, not config.get("scorer"))
                #     )
                # ],
                # [
                #     InlineKeyboardButton(
                #         text=lang("ml"),
                #         callback_data=button_data("none")
                #     ),
                #     InlineKeyboardButton(
                #         text=f"{(lambda x: '■' if x else '□️')(config.get('ml'))}",
                #         callback_data=button_data("ml", None, not config.get("ml"))
                #     )
                # ],
                [
                    InlineKeyboardButton(
                        text=lang("commit"),
                        callback_data=button_data("commit")
                    )
                ]
            ]
        )
    except Exception as e:
        logger.warning(f"Button nospam error: {e}", exc_info=True)

    return markup


def button_recheck(config: dict) -> Optional[InlineKeyboardMarkup]:
    # Get inline markup for RECHECK
    markup = None
    try:
        markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=lang("default_config"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('default'))}",
                        callback_data=button_data(
                            action=(lambda x: "default" if not x else "none")(config.get("default")),
                            action_type=None,
                            data=not config.get("default")
                        )
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("delete"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('delete'))}",
                        callback_data=button_data("delete", None, not config.get("delete"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("restrict"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('restrict'))}",
                        callback_data=button_data("restrict", None, not config.get("restrict"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("commit"),
                        callback_data=button_data("commit")
                    )
                ]
            ]
        )
    except Exception as e:
        logger.warning(f"Button recheck error: {e}", exc_info=True)

    return markup


def button_tip(config: dict) -> Optional[InlineKeyboardMarkup]:
    # Get inline markup for TIP
    markup = None
    try:
        markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=lang("default_config"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('default'))}",
                        callback_data=button_data(
                            action=(lambda x: "default" if not x else "none")(config.get("default")),
                            action_type=None,
                            data=not config.get("default")
                        )
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("captcha"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('captcha'))}",
                        callback_data=button_data("captcha", None, not config.get("captcha"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("alone"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('alone'))}",
                        callback_data=button_data("alone", None, not config.get("alone"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("clean"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('clean'))}",
                        callback_data=button_data("clean", None, not config.get("clean"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("ot"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('ot'))}",
                        callback_data=button_data("ot", None, not config.get("ot"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("rm"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('rm'))}",
                        callback_data=button_data("rm", None, not config.get("rm"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("welcome"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('welcome'))}",
                        callback_data=button_data("welcome", None, not config.get("welcome"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("keyword"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('keyword'))}",
                        callback_data=button_data("keyword", None, not config.get("keyword"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("white"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('white'))}",
                        callback_data=button_data("white", None, not config.get("white"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("cancel"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('cancel'))}",
                        callback_data=button_data("cancel", None, not config.get("cancel"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("hold"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('hold'))}",
                        callback_data=button_data("hold", None, not config.get("hold"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("channel"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('channel'))}",
                        callback_data=button_data("channel", None, not config.get("channel"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("resend"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('resend'))}",
                        callback_data=button_data("resend", None, not config.get("resend"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("commit"),
                        callback_data=button_data("commit")
                    )
                ]
            ]
        )
    except Exception as e:
        logger.warning(f"Button tip error: {e}", exc_info=True)

    return markup


def button_user(config: dict) -> Optional[InlineKeyboardMarkup]:
    # Get inline markup for USER
    markup = None
    try:
        markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=lang("default_config"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('default'))}",
                        callback_data=button_data(
                            action=(lambda x: "default" if not x else "none")(config.get("default")),
                            action_type=None,
                            data=not config.get("default")
                        )
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("delete"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('delete'))}",
                        callback_data=button_data("delete", None, not config.get("delete"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("gb"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('gb'))}",
                        callback_data=button_data("gb", None, not config.get("gb"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("gr"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('gr'))}",
                        callback_data=button_data("gr", None, not config.get("gr"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("gd"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('gd'))}",
                        callback_data=button_data("gd", None, not config.get("gd"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("sb"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('sb'))}",
                        callback_data=button_data("sb", None, not config.get("sb"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("sr"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('sr'))}",
                        callback_data=button_data("sr", None, not config.get("sr"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("sd"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('sd'))}",
                        callback_data=button_data("sd", None, not config.get("sd"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("commit"),
                        callback_data=button_data("commit")
                    )
                ]
            ]
        )
    except Exception as e:
        logger.warning(f"Button user error: {e}", exc_info=True)

    return markup


def button_warn(config: dict) -> Optional[InlineKeyboardMarkup]:
    # Get inline markup for WARN
    markup = None
    try:
        report_auto = config.get("report") and config["report"].get("auto")
        report_manual = config.get("report") and config["report"].get("manual")
        markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=lang("default_config"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('default'))}",
                        callback_data=button_data(
                            action=(lambda x: "default" if not x else "none")(config.get("default")),
                            action_type=None,
                            data=not config.get("default")
                        )
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("delete"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('delete'))}",
                        callback_data=button_data("delete", None, not config.get("delete"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("warn_limit"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{config.get('limit', 3)}",
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '-️' if x > 2 else '*')(config.get('limit', 3))}",
                        callback_data=button_data(
                            action=(lambda x: "limit" if x > 2 else "none")(config.get("limit", 3)),
                            action_type=None,
                            data=config.get("limit", 3) - 1
                        )
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '+️' if x < 5 else '*')(config.get('limit', 3))}",
                        callback_data=button_data(
                            action=(lambda x: "limit" if x < 5 else "none")(config.get("limit", 3)),
                            action_type=None,
                            data=config.get("limit", 3) + 1
                        )
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("warn_admin"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(config.get('mention'))}",
                        callback_data=button_data("mention", None, not config.get("mention"))
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("report_auto"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(report_auto)}",
                        callback_data=button_data("report", "auto", not report_auto)
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("report_manual"),
                        callback_data=button_data("none")
                    ),
                    InlineKeyboardButton(
                        text=f"{(lambda x: '■' if x else '□️')(report_manual)}",
                        callback_data=button_data("report", "manual", not report_manual)
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=lang("commit"),
                        callback_data=button_data("commit")
                    )
                ]
            ]
        )
    except Exception as e:
        logger.warning(f"Button warn error: {e}", exc_info=True)

    return markup


def commit_change(client: Client, key: str) -> bool:
    # Commit the new configuration
    try:
        if not glovar.configs.get(key):
            return True

        # Change commit status
        glovar.configs[key]["commit"] = True

        # Use config type to get the right receiver
        config_type = glovar.configs[key]["type"]
        group_id = glovar.configs[key]["group_id"]

        # The config session message id
        message_id = glovar.configs[key]["message_id"]
        config_data = glovar.configs[key]["config"]

        # Edit config session message
        text = get_config_text(key)
        text += f"{lang('status')}{lang('colon')}{code(lang('committed'))}\n"
        thread(edit_message_text, (client, glovar.config_channel_id, message_id, text))

        # Commit changes to exchange channel
        receivers = [config_type.upper()]
        share_data(
            client=client,
            receivers=receivers,
            action="config",
            action_type="commit",
            data={
                "group_id": group_id,
                "config": config_data
            }
        )

        # Send debug message
        group_name = glovar.configs[key]["group_name"]
        group_link = glovar.configs[key]["group_link"]
        user_id = glovar.configs[key]["user_id"]
        debug_text = (f"{lang('project')}{lang('colon')}{general_link(glovar.project_name, glovar.project_link)}\n"
                      f"{lang('group_name')}{lang('colon')}{general_link(group_name, group_link)}\n"
                      f"{lang('group_id')}{lang('colon')}{code(group_id)}\n"
                      f"{lang('admin_group')}{lang('colon')}{code(user_id)}\n"
                      f"{lang('action')}{lang('colon')}{code(lang('commit_change'))}\n"
                      f"{lang('target')}{lang('colon')}{code(config_type.upper())}\n")
        thread(send_message, (client, glovar.debug_channel_id, debug_text))

        return True
    except Exception as e:
        logger.warning(f"Commit change error: {e}", exc_info=True)

    return False


def get_config_message(key: str) -> (str, Optional[InlineKeyboardMarkup]):
    # Get a config session message (text + reply markup)
    text = ""
    markup = None
    try:
        if not glovar.configs.get(key):
            return "", None

        config_type = glovar.configs[key]["type"]
        config_data = glovar.configs[key]["config"]

        # For each config type, use different function to generate reply markup buttons
        markup = eval(f"button_{config_type}")(config_data)
        text = get_config_text(key)
        text += (f"{lang('description')}{lang('colon')}{code(lang('config_description'))}\n"
                 f"{lang('button_enabled')}{lang('colon')}■\n"
                 f"{lang('button_disabled')}{lang('colon')}□\n")
    except Exception as e:
        logger.warning(f"Get config message error: {e}", exc_info=True)

    return text, markup


def get_config_text(key: str) -> str:
    # Get a config session message text prefix
    text = ""
    try:
        project_name = glovar.configs[key]["project_name"]
        project_link = glovar.configs[key]["project_link"]

        group_id = glovar.configs[key]["group_id"]
        group_name = glovar.configs[key]["group_name"]
        group_link = glovar.configs[key]["group_link"]

        user_id = glovar.configs[key]["user_id"]

        text = (f"{lang('config_code')}{lang('colon')}{code(key)}\n"
                f"{lang('project')}{lang('colon')}{general_link(project_name, project_link)}\n"
                f"{lang('group_name')}{lang('colon')}{general_link(group_name, group_link)}\n"
                f"{lang('group_id')}{lang('colon')}{code(group_id)}\n"
                f"{lang('admin_group')}{lang('colon')}{code(user_id)}\n")
    except Exception as e:
        logger.warning(f"Get config text error: {e}", exc_info=True)

    return text


def remove_old(client: Client, key: str) -> bool:
    # Remove old config session data
    try:
        if not glovar.configs.get(key):
            return True

        if glovar.configs[key]["lock"]:
            return True

        if not glovar.configs[key]["commit"]:
            # If it is not committed, edit the session message to update the status (invalid)
            text = get_config_text(key)
            text += f"{lang('status')}{lang('colon')}{code(lang('expired'))}\n"
            mid = glovar.configs[key]["message_id"]
            thread(edit_message_text, (client, glovar.config_channel_id, mid, text))

        # Pop this config data
        glovar.configs.pop(key, {})
        save("configs")

        return True
    except Exception as e:
        logger.warning(f"Remove old error: {e}", exc_info=True)

    return False


def set_default(key: str) -> bool:
    # Set the config to the default one
    try:
        glovar.configs[key]["config"] = deepcopy(glovar.configs[key]["default"])
        glovar.configs[key]["config"]["lock"] = get_now()
        save("configs")

        return True
    except Exception as e:
        logger.warning(f"Set default error: {e}", exc_info=True)

    return False
