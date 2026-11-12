# VLC and IPTV setup from a streaming site

## When to use

- Use this skill when the user has a TV streaming site that will not play in the browser and wants to watch its channels in VLC.

- Use it for Android VLC first. The same links work in desktop VLC, but the steps here are the Android ones.

## Find the real links

- Find the three link types behind the site: the full playlist, the guide, and the direct per-channel stream.

- Look for a playlist file, a guide file, and a direct stream link for the channel the user wants.

- Treat an "Open in app" control as a dropdown, not as a vlc link. It may not hand VLC anything usable.

- Remember the site may not relay streams at all. The device fetches the stream direct from the source, so the direct link is the thing that matters.

- Give the user the exact links, copied verbatim, not a description of where to find them.

## Give copy-paste VLC Android steps

- Give short copy-paste steps for VLC on Android: open VLC, tap More, tap New stream, paste the link.

- Start with the single-channel direct link as the fast test. One channel playing proves the setup works.

- Warn the user before they load the full playlist. A full playlist can be heavy, with thousands of channels, and it loads slowly.

- Add the full playlist only after the single-channel test plays.

## Name the guide limitation and the alternatives

- Tell the user VLC has no guide support, so the guide file will not show a programme guide inside VLC.

- Name the alternatives for a guide: TiviMate, Kodi, or Jellyfin.

- Keep the VLC setup as the fast route to watching, and offer the guide alternatives only if the user wants a guide.

## Tune playback when it stutters

- Raise the network-caching value in VLC if playback stutters or buffers.

- Offer the gesture, background-playback, and subtitle options as small extras once the stream plays.

## Available connectors

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Alternatives for better results

- Offer TiviMate, Kodi, or Jellyfin when the user wants a programme guide, since VLC cannot show one.

- Offer the single-channel link first even when the user asked for the whole playlist, so they get a working stream before the heavy load.
