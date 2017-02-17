import datetime
import xml.etree.cElementTree as ET
import os

from xml.dom import minidom


def timestamp():
    return str(datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"))


def create_core_xml(filename,
                    source_path,
                    task_id,
                    material_id,
                    series_title,
                    season_title,
                    season_number,
                    episode_title,
                    episode_number,
                    start_date,
                    end_date,
                    synopsis,
                    ratings,
                    source_filename,
                    number_of_segments,
                    conform_profile,
                    transcode_profile,
                    target_path,
                    con_def,
                    con_aspect_ratio,
                    profile_name,
                    package_type,
                    segment_start,
                    segment_dur,
                    video_naming_convention,
                    image_naming_convention,
                    package_naming_convention):

    core_xml_base = os.path.splitext(os.path.basename(filename))[0]
    manifest = ET.Element('manifest')
    manifest.set('task_id', str(task_id))
    asset_metadata = ET.SubElement(manifest, 'asset_metadata')
    file_info = ET.SubElement(manifest, 'file_info')

    ET.SubElement(asset_metadata, 'material_id').text = str(material_id)
    ET.SubElement(asset_metadata, 'series_title').text = str(series_title)
    ET.SubElement(asset_metadata, 'season_title').text = str(season_title)
    ET.SubElement(asset_metadata, 'season_number').text = str(season_number)
    ET.SubElement(asset_metadata, 'episode_title').text = str(episode_title)
    ET.SubElement(asset_metadata, 'episode_number').text = str(episode_number)
    ET.SubElement(asset_metadata, 'start_date').text = str(start_date)
    ET.SubElement(asset_metadata, 'end_date').text = str(end_date)
    ET.SubElement(asset_metadata, 'synopsis').text = str(synopsis)
    ET.SubElement(asset_metadata, 'ratings').text = str(ratings)

    ET.SubElement(file_info, 'source_filename').text = str(source_filename)
    ET.SubElement(file_info, 'number_of_segments').text = str(number_of_segments)

    for i in range(int(number_of_segments)):
        i += 1
        x = i - 1
        seg = ET.SubElement(file_info, 'segment_%d' % i)
        seg.set('seg_%d_in' % i, str(segment_start[int('%d' % x)]))
        seg.set('seg_%d_dur' % i, str(segment_dur[int('%d' % x)]))

    con = ET.SubElement(file_info, 'conform_profile')
    con.set('definition', str(con_def))
    con.set('aspect_ratio', str(con_aspect_ratio))
    con.text = str(conform_profile)
    tran = ET.SubElement(file_info, 'transcode_profile')
    tran.set('profile_name', str(profile_name))
    tran.set('package_type', str(package_type))
    tran.text = str(transcode_profile)
    ET.SubElement(file_info, 'target_path').text = str(target_path)
    ET.SubElement(file_info, 'video_file_naming_convention').text = str(video_naming_convention)
    ET.SubElement(file_info, 'image_file_naming_convention').text = str(image_naming_convention)
    ET.SubElement(file_info, 'package_naming_convention').text = str(package_naming_convention)

    xmlstr = minidom.parseString(ET.tostring(manifest)).toprettyxml(indent="   ")
    with open(source_path + core_xml_base + timestamp()[:10] + '.xml', "w") as f:
        f.write(xmlstr)
