from pathlib import Path

from src.geotexxx.gefxml_reader import Bore


def test_borehole_string_parsing():
    # Get path to test boreholes
    boreholes_path = Path(__file__).parent / "borehole-files"

    # Test parsing .xml file as string
    with open(boreholes_path / "test_borehole.xml") as f:
        xml = f.read()
        bh_xml = Bore()
        bh_xml.load_xml(xml, fromFile=False)

    # # Test loading .gef file as string
    with open(boreholes_path / "test_borehole.gef") as f:
        gef = f.read()
        bh_gef = Bore()
        bh_gef.load_gef(gef, from_file=False)
    


