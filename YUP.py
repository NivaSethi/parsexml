import os
import csv
import xml.etree.ElementTree as ET

def parse_xml(search_result):
    tree = ET.parse(search_result)
    root = tree.getroot()

    data = {
        'nct_id': root.findtext('nct_id'),
        'brief_title': root.findtext('brief_title'),
        'brief_summary': root.findtext('brief_summary'),
        'detailed_description': root.findtext('detailed_description'),
        'study_type': root.findtext('study_type'),
        'eligibility_criteria': root.findtext('eligibility_criteria'),
        'conditions': root.findtext('conditions'),
        'interventions': root.findtext('interventions'),
        'lead_sponsor_name': root.findtext('lead_sponsor_name'),
        'site_names': root.findtext('site_names'),
        'site_addresses': root.findtext('site_addresses')
    }

    return data

def write_to_csv(data, csv_file):
    with open(csv_file, 'a') as f:
        writer = csv.DictWriter(f, fieldnames=data.keys())
        writer.writerow(data)

def main():
    xml_folder = 'Downloads/search_result' 
    csv_file = 'output.csv'

    # Write headers to the CSV file
    with open(csv_file, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=['nct_id', 'brief_title', 'brief_summary', 'detailed_description', 'study_type',
              'eligibility_criteria', 'conditions', 'interventions', 'lead_sponsor_name',
              'site_names', 'site_addresses'])
        writer.writeheader()

    # Parse 
    for xml_file in os.listdir(xml_folder):
        if xml_file.endswith('.xml'):
            data = parse_xml(os.path.join(xml_folder, xml_file))
            write_to_csv(data, csv_file)

if __name__ == '__main__':
    main()

