import datetime
import xml.etree.cElementTree as ET
import os

from xml.dom import minidom


def timestamp():
    return str(datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"))


def create_core_xml(filename,
                    path,
                    task_id,
                    material_id,
                    series_id,
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
                    segment_1,
                    segment_2,
                    segment_3,
                    segment_4,
                    conform_profile,
                    transcode_profile,
                    target_path,
                    segment_start,
                    segment_dur):

    core_xml_base = os.path.splitext(os.path.basename(filename))[0]
    manifest = ET.Element('manifest')
    manifest.set('task_id', task_id)
    asset_metadata = ET.SubElement(manifest, 'asset_metadata')
    file_info = ET.SubElement(manifest, 'file_info')

    ET.SubElement(asset_metadata, 'material_id',).text = str(material_id)
    ET.SubElement(asset_metadata, 'series_title',).text = str(series_id)
    ET.SubElement(asset_metadata, 'season_title',).text = str(season_title)
    ET.SubElement(asset_metadata, 'season_number',).text = str(season_number)
    ET.SubElement(asset_metadata, 'episode_title',).text = str(episode_title)
    ET.SubElement(asset_metadata, 'episode_number',).text = str(episode_number)
    ET.SubElement(asset_metadata, 'start_date',).text = str(start_date)
    ET.SubElement(asset_metadata, 'end_date',).text = str(end_date)
    ET.SubElement(asset_metadata, 'synopsis',).text = str(synopsis)
    ET.SubElement(asset_metadata, 'ratings',).text = str(ratings)

    ET.SubElement(file_info, 'source_filename',).text = str(source_filename)
    ET.SubElement(file_info, 'number_of_segments',).text = str(number_of_segments)

    # TODO: Create dynamic segment creation.

    for i in range(int(number_of_segments)):
        seg = ET.SubElement(file_info, 'segment_%d' % i)
        i -= 1
        seg.set('seg_%d_start' % i, segment_start[int('%d' % i)])
        seg.set('seg_%d_end' % i, segment_dur[int('%d' % i)])
    """
    if number_of_segments == '1':
        ET.SubElement(file_info, 'segment_1',).text = str(segment_1)
    elif number_of_segments == '2':
        ET.SubElement(file_info, 'segment_1', ).text = str(segment_1)
        ET.SubElement(file_info, 'segment_2', ).text = str(segment_2)
    elif number_of_segments == '3':
        ET.SubElement(file_info, 'segment_1', ).text = str(segment_1)
        ET.SubElement(file_info, 'segment_2', ).text = str(segment_2)
        ET.SubElement(file_info, 'segment_3', ).text = str(segment_3)
    elif number_of_segments == '4':
        ET.SubElement(file_info, 'segment_1', ).text = str(segment_1)
        ET.SubElement(file_info, 'segment_2', ).text = str(segment_2)
        ET.SubElement(file_info, 'segment_2', ).text = str(segment_3)
        ET.SubElement(file_info, 'segment_2', ).text = str(segment_4)
    """
    ET.SubElement(file_info, 'conform_profile', ).text = str(conform_profile)
    ET.SubElement(file_info, 'transcode_profile', ).text = str(transcode_profile)
    ET.SubElement(file_info, 'target_path', ).text = str(target_path)

    xmlstr = minidom.parseString(ET.tostring(manifest)).toprettyxml(indent="   ")
    with open(path + core_xml_base + '.xml', "w") as f:
        f.write(xmlstr)
