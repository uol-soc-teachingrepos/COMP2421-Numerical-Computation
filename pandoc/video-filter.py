#!/usr/bin/env python
from pandocfilters import toJSONFilter, RawInline, Image, Para
import os
import subprocess
import sys


def htmlblock(code):
    return RawInline('html', code)


def prefixed(fn):
    d = os.path.dirname(fn)
    b = os.path.basename(fn)
    return os.path.join(d, '.' + b)


def convert_to_webm(src):
    src_filename, src_ext = os.path.splitext(src)
    out_webm = prefixed(src_filename) + '.webm'

    # if file exists pass
    if os.path.isfile(out_webm):
        return out_webm

    # generate formatted video
    cmd_line = ['ffmpeg', '-hide_banner',
                '-i', src,
                '-vcodec', 'libvpx',
                '-an', out_webm]
    subprocess.call(cmd_line, stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE)
    if os.path.isfile(out_webm):
        return out_webm
    return None


def convert_to_h264_mp4(src):
    src_filename, src_ext = os.path.splitext(src)
    out_h264_mp4 = prefixed(src_filename) + '.h264.mp4'

    # if video exists pass
    if os.path.isfile(out_h264_mp4):
        return out_h264_mp4

    # generate video
    cmd_line = ['ffmpeg', '-hide_banner',
                '-i', src,
                '-vcodec', 'h264',
                '-an',
                '-strict', '-2',
                out_h264_mp4]
    subprocess.call(cmd_line)
    if os.path.isfile(out_h264_mp4):
        return out_h264_mp4
    return None


def convert_to_yuv420p_mp4(src):
    src_filename, src_ext = os.path.splitext(src)
    out_yuv420p_mp4 = prefixed(src_filename) + '.yuv420p.mp4'
    if os.path.isfile(out_yuv420p_mp4):
        return out_yuv420p_mp4

    cmd_line = ['ffmpeg', '-hide_banner',
                '-i', src,
                '-vcodec', 'libx264',
                '-pix_fmt', 'yuv420p',
                '-profile:v',
                'baseline', '-level', '3',
                out_yuv420p_mp4]
    subprocess.call(cmd_line)
    if os.path.isfile(out_yuv420p_mp4):
        return out_yuv420p_mp4
    return None


def attrs_to_string(attrs):
    ret = ''

    for a in attrs:
        if isinstance(a, str):
            o = a.strip()
            if o != '':
                ret = ret + f'class="{o}"' + ' '
        elif isinstance(a, list):
            if len(a) == 2:
                ret = ret + f'{a[0]}="{a[1]}"' + ' '
            else:
                ret = ret + attrs_to_string(a) + ' '

    return ret.strip()


def video_filter(key, value, format, meta):
    if key == 'Image':
        if len(value) == 2:
            alt, [src, title] = value
            attrs = None
        else:
            attrs, alt, [src, title] = value

        if format in ('html', 'html5', 'revealjs'):
            src_filename, src_ext = os.path.splitext(src)
            if src_ext in ['.mp4', '.avi', '.webm', '.ogv']:  # we have a video
                out_list = [src]
                for convert in [convert_to_webm,
                                convert_to_h264_mp4,
                                convert_to_yuv420p_mp4]:
                    try:
                        out = convert(src)
                        if out is not None:
                            out_list.append(out)
                    except:
                        pass

                attr_str = attrs_to_string(attrs)
                return htmlblock('<video autoplay loop muted {}>\n'.format(attr_str) +
                                 '\n'.join(['<source data-src="{}" />'.format(out) for out in out_list]) +
                                 '\n' +
                                 '<a href="{}">Video</a>\n'.format(src) +
                                 '</video>')
        else:
            if(attrs):
                return Image(attrs, alt, [src, title])
            else:
                return Image(alt, [src, title])


if __name__ == "__main__":
    toJSONFilter(video_filter)
