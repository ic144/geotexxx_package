from pathlib import Path
import requests

from src.geotexxx.gefxml_reader import Bore, Cpt


def test_borehole_string_parsing():
    # Get path to test boreholes
    boreholes_path = Path(__file__).parent / "borehole-files"

    # Test parsing .xml file as string
    with open(boreholes_path / "test_borehole.xml") as f:
        xml = f.read()
        bh_xml = Bore()
        bh_xml.load_xml(xml, from_file=False)

    # # Test loading .gef file as string
    with open(boreholes_path / "test_borehole.gef") as f:
        gef = f.read()
        bh_gef = Bore()
        bh_gef.load_gef(gef, from_file=False)


def test_cpt_incl_interpretation():
    cpt = Cpt()
    xml_string = requests.get('https://publiek.broservices.nl/sr/cpt/v1/objects/CPT000000183472').text
    cpt.load_xml(xml_string, from_file=False)
    cpt.interpret()


def test_borehole_incl_complex_analyses():
    bore = Bore()
    xml_string = requests.get('https://publiek.broservices.nl/sr/bhrgt/v2/objects/BHR000000374586').text
    bore.load_xml(xml_string, from_file=False)
    print(bore.soillayers)
    print(bore.analyses)
    print(bore.complex_analyses)