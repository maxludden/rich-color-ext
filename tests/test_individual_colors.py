from rich_color_ext import _extended_parse

def test_parse_color_aliceblue():
    color = _extended_parse('aliceblue')
    assert color.name == 'aliceblue'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (240, 248, 255)

def test_parse_color_antiquewhite():
    color = _extended_parse('antiquewhite')
    assert color.name == 'antiquewhite'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (250, 235, 215)

def test_parse_color_aqua():
    color = _extended_parse('aqua')
    assert color.name == 'aqua'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (0, 255, 255)

def test_parse_color_aquamarine():
    color = _extended_parse('aquamarine')
    assert color.name == 'aquamarine'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (127, 255, 212)

def test_parse_color_azure():
    color = _extended_parse('azure')
    assert color.name == 'azure'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (240, 255, 255)

def test_parse_color_beige():
    color = _extended_parse('beige')
    assert color.name == 'beige'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (245, 245, 220)

def test_parse_color_bisque():
    color = _extended_parse('bisque')
    assert color.name == 'bisque'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (255, 228, 196)

def test_parse_color_black():
    color = _extended_parse('black')
    assert color.name == 'black'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (0, 0, 0)

def test_parse_color_blanchedalmond():
    color = _extended_parse('blanchedalmond')
    assert color.name == 'blanchedalmond'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (255, 235, 205)

def test_parse_color_blue():
    color = _extended_parse('blue')
    assert color.name == 'blue'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (0, 0, 128)

def test_parse_color_blueviolet():
    color = _extended_parse('blueviolet')
    assert color.name == 'blueviolet'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (138, 43, 226)

def test_parse_color_brown():
    color = _extended_parse('brown')
    assert color.name == 'brown'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (165, 42, 42)

def test_parse_color_burlywood():
    color = _extended_parse('burlywood')
    assert color.name == 'burlywood'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (222, 184, 135)

def test_parse_color_cadetblue():
    color = _extended_parse('cadetblue')
    assert color.name == 'cadetblue'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (95, 158, 160)

def test_parse_color_chartreuse():
    color = _extended_parse('chartreuse')
    assert color.name == 'chartreuse'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (127, 255, 0)

def test_parse_color_chocolate():
    color = _extended_parse('chocolate')
    assert color.name == 'chocolate'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (210, 105, 30)

def test_parse_color_coral():
    color = _extended_parse('coral')
    assert color.name == 'coral'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (255, 127, 80)

def test_parse_color_cornflowerblue():
    color = _extended_parse('cornflowerblue')
    assert color.name == 'cornflowerblue'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (100, 149, 237)

def test_parse_color_cornsilk():
    color = _extended_parse('cornsilk')
    assert color.name == 'cornsilk'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (255, 248, 220)

def test_parse_color_crimson():
    color = _extended_parse('crimson')
    assert color.name == 'crimson'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (220, 20, 60)

def test_parse_color_cyan():
    color = _extended_parse('cyan')
    assert color.name == 'cyan'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (0, 128, 128)

def test_parse_color_darkblue():
    color = _extended_parse('darkblue')
    assert color.name == 'darkblue'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (0, 0, 139)

def test_parse_color_darkcyan():
    color = _extended_parse('darkcyan')
    assert color.name == 'darkcyan'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (0, 139, 139)

def test_parse_color_darkgoldenrod():
    color = _extended_parse('darkgoldenrod')
    assert color.name == 'darkgoldenrod'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (184, 134, 11)

def test_parse_color_darkgray():
    color = _extended_parse('darkgray')
    assert color.name == 'darkgray'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (169, 169, 169)

def test_parse_color_darkgreen():
    color = _extended_parse('darkgreen')
    assert color.name == 'darkgreen'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (0, 100, 0)

def test_parse_color_darkgrey():
    color = _extended_parse('darkgrey')
    assert color.name == 'darkgrey'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (169, 169, 169)

def test_parse_color_darkkhaki():
    color = _extended_parse('darkkhaki')
    assert color.name == 'darkkhaki'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (189, 183, 107)

def test_parse_color_darkmagenta():
    color = _extended_parse('darkmagenta')
    assert color.name == 'darkmagenta'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (139, 0, 139)

def test_parse_color_darkolivegreen():
    color = _extended_parse('darkolivegreen')
    assert color.name == 'darkolivegreen'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (85, 107, 47)

def test_parse_color_darkorange():
    color = _extended_parse('darkorange')
    assert color.name == 'darkorange'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (255, 140, 0)

def test_parse_color_darkorchid():
    color = _extended_parse('darkorchid')
    assert color.name == 'darkorchid'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (153, 50, 204)

def test_parse_color_darkred():
    color = _extended_parse('darkred')
    assert color.name == 'darkred'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (139, 0, 0)

def test_parse_color_darksalmon():
    color = _extended_parse('darksalmon')
    assert color.name == 'darksalmon'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (233, 150, 122)

def test_parse_color_darkseagreen():
    color = _extended_parse('darkseagreen')
    assert color.name == 'darkseagreen'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (143, 188, 143)

def test_parse_color_darkslateblue():
    color = _extended_parse('darkslateblue')
    assert color.name == 'darkslateblue'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (72, 61, 139)

def test_parse_color_darkslategray():
    color = _extended_parse('darkslategray')
    assert color.name == 'darkslategray'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (47, 79, 79)

def test_parse_color_darkslategrey():
    color = _extended_parse('darkslategrey')
    assert color.name == 'darkslategrey'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (47, 79, 79)

def test_parse_color_darkturquoise():
    color = _extended_parse('darkturquoise')
    assert color.name == 'darkturquoise'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (0, 206, 209)

def test_parse_color_darkviolet():
    color = _extended_parse('darkviolet')
    assert color.name == 'darkviolet'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (148, 0, 211)

def test_parse_color_deeppink():
    color = _extended_parse('deeppink')
    assert color.name == 'deeppink'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (255, 20, 147)

def test_parse_color_deepskyblue():
    color = _extended_parse('deepskyblue')
    assert color.name == 'deepskyblue'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (0, 191, 255)

def test_parse_color_dimgray():
    color = _extended_parse('dimgray')
    assert color.name == 'dimgray'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (105, 105, 105)

def test_parse_color_dimgrey():
    color = _extended_parse('dimgrey')
    assert color.name == 'dimgrey'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (105, 105, 105)

def test_parse_color_dodgerblue():
    color = _extended_parse('dodgerblue')
    assert color.name == 'dodgerblue'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (30, 144, 255)

def test_parse_color_firebrick():
    color = _extended_parse('firebrick')
    assert color.name == 'firebrick'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (178, 34, 34)

def test_parse_color_floralwhite():
    color = _extended_parse('floralwhite')
    assert color.name == 'floralwhite'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (255, 250, 240)

def test_parse_color_forestgreen():
    color = _extended_parse('forestgreen')
    assert color.name == 'forestgreen'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (34, 139, 34)

def test_parse_color_fuchsia():
    color = _extended_parse('fuchsia')
    assert color.name == 'fuchsia'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (255, 0, 255)

def test_parse_color_gainsboro():
    color = _extended_parse('gainsboro')
    assert color.name == 'gainsboro'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (220, 220, 220)

def test_parse_color_ghostwhite():
    color = _extended_parse('ghostwhite')
    assert color.name == 'ghostwhite'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (248, 248, 255)

def test_parse_color_gold():
    color = _extended_parse('gold')
    assert color.name == 'gold'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (255, 215, 0)

def test_parse_color_goldenrod():
    color = _extended_parse('goldenrod')
    assert color.name == 'goldenrod'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (218, 165, 32)

def test_parse_color_gray():
    color = _extended_parse('gray')
    assert color.name == 'gray'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (128, 128, 128)

def test_parse_color_green():
    color = _extended_parse('green')
    assert color.name == 'green'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (0, 128, 0)

def test_parse_color_greenyellow():
    color = _extended_parse('greenyellow')
    assert color.name == 'greenyellow'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (173, 255, 47)

def test_parse_color_grey():
    color = _extended_parse('grey')
    assert color.name == 'grey'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (128, 128, 128)

def test_parse_color_honeydew():
    color = _extended_parse('honeydew')
    assert color.name == 'honeydew'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (240, 255, 240)

def test_parse_color_hotpink():
    color = _extended_parse('hotpink')
    assert color.name == 'hotpink'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (255, 105, 180)

def test_parse_color_indianred():
    color = _extended_parse('indianred')
    assert color.name == 'indianred'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (205, 92, 92)

def test_parse_color_indigo():
    color = _extended_parse('indigo')
    assert color.name == 'indigo'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (75, 0, 130)

def test_parse_color_ivory():
    color = _extended_parse('ivory')
    assert color.name == 'ivory'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (255, 255, 240)

def test_parse_color_khaki():
    color = _extended_parse('khaki')
    assert color.name == 'khaki'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (240, 230, 140)

def test_parse_color_lavender():
    color = _extended_parse('lavender')
    assert color.name == 'lavender'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (230, 230, 250)

def test_parse_color_lavenderblush():
    color = _extended_parse('lavenderblush')
    assert color.name == 'lavenderblush'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (255, 240, 245)

def test_parse_color_lawngreen():
    color = _extended_parse('lawngreen')
    assert color.name == 'lawngreen'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (124, 252, 0)

def test_parse_color_lemonchiffon():
    color = _extended_parse('lemonchiffon')
    assert color.name == 'lemonchiffon'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (255, 250, 205)

def test_parse_color_lightblue():
    color = _extended_parse('lightblue')
    assert color.name == 'lightblue'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (173, 216, 230)

def test_parse_color_lightcoral():
    color = _extended_parse('lightcoral')
    assert color.name == 'lightcoral'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (240, 128, 128)

def test_parse_color_lightcyan():
    color = _extended_parse('lightcyan')
    assert color.name == 'lightcyan'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (224, 255, 255)

def test_parse_color_lightgoldenrodyellow():
    color = _extended_parse('lightgoldenrodyellow')
    assert color.name == 'lightgoldenrodyellow'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (250, 250, 210)

def test_parse_color_lightgray():
    color = _extended_parse('lightgray')
    assert color.name == 'lightgray'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (211, 211, 211)

def test_parse_color_lightgreen():
    color = _extended_parse('lightgreen')
    assert color.name == 'lightgreen'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (144, 238, 144)

def test_parse_color_lightgrey():
    color = _extended_parse('lightgrey')
    assert color.name == 'lightgrey'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (211, 211, 211)

def test_parse_color_lightpink():
    color = _extended_parse('lightpink')
    assert color.name == 'lightpink'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (255, 182, 193)

def test_parse_color_lightsalmon():
    color = _extended_parse('lightsalmon')
    assert color.name == 'lightsalmon'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (255, 160, 122)

def test_parse_color_lightseagreen():
    color = _extended_parse('lightseagreen')
    assert color.name == 'lightseagreen'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (32, 178, 170)

def test_parse_color_lightskyblue():
    color = _extended_parse('lightskyblue')
    assert color.name == 'lightskyblue'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (135, 206, 250)

def test_parse_color_lightslategray():
    color = _extended_parse('lightslategray')
    assert color.name == 'lightslategray'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (119, 136, 153)

def test_parse_color_lightslategrey():
    color = _extended_parse('lightslategrey')
    assert color.name == 'lightslategrey'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (119, 136, 153)

def test_parse_color_lightsteelblue():
    color = _extended_parse('lightsteelblue')
    assert color.name == 'lightsteelblue'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (176, 196, 222)

def test_parse_color_lightyellow():
    color = _extended_parse('lightyellow')
    assert color.name == 'lightyellow'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (255, 255, 224)

def test_parse_color_lime():
    color = _extended_parse('lime')
    assert color.name == 'lime'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (0, 255, 0)

def test_parse_color_limegreen():
    color = _extended_parse('limegreen')
    assert color.name == 'limegreen'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (50, 205, 50)

def test_parse_color_linen():
    color = _extended_parse('linen')
    assert color.name == 'linen'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (250, 240, 230)

def test_parse_color_magenta():
    color = _extended_parse('magenta')
    assert color.name == 'magenta'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (128, 0, 128)

def test_parse_color_maroon():
    color = _extended_parse('maroon')
    assert color.name == 'maroon'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (128, 0, 0)

def test_parse_color_mediumaquamarine():
    color = _extended_parse('mediumaquamarine')
    assert color.name == 'mediumaquamarine'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (102, 205, 170)

def test_parse_color_mediumblue():
    color = _extended_parse('mediumblue')
    assert color.name == 'mediumblue'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (0, 0, 205)

def test_parse_color_mediumorchid():
    color = _extended_parse('mediumorchid')
    assert color.name == 'mediumorchid'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (186, 85, 211)

def test_parse_color_mediumpurple():
    color = _extended_parse('mediumpurple')
    assert color.name == 'mediumpurple'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (147, 112, 219)

def test_parse_color_mediumseagreen():
    color = _extended_parse('mediumseagreen')
    assert color.name == 'mediumseagreen'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (60, 179, 113)

def test_parse_color_mediumslateblue():
    color = _extended_parse('mediumslateblue')
    assert color.name == 'mediumslateblue'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (123, 104, 238)

def test_parse_color_mediumspringgreen():
    color = _extended_parse('mediumspringgreen')
    assert color.name == 'mediumspringgreen'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (0, 250, 154)

def test_parse_color_mediumturquoise():
    color = _extended_parse('mediumturquoise')
    assert color.name == 'mediumturquoise'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (72, 209, 204)

def test_parse_color_mediumvioletred():
    color = _extended_parse('mediumvioletred')
    assert color.name == 'mediumvioletred'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (199, 21, 133)

def test_parse_color_midnightblue():
    color = _extended_parse('midnightblue')
    assert color.name == 'midnightblue'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (25, 25, 112)

def test_parse_color_mintcream():
    color = _extended_parse('mintcream')
    assert color.name == 'mintcream'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (245, 255, 250)

def test_parse_color_mistyrose():
    color = _extended_parse('mistyrose')
    assert color.name == 'mistyrose'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (255, 228, 225)

def test_parse_color_moccasin():
    color = _extended_parse('moccasin')
    assert color.name == 'moccasin'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (255, 228, 181)

def test_parse_color_navajowhite():
    color = _extended_parse('navajowhite')
    assert color.name == 'navajowhite'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (255, 222, 173)

def test_parse_color_navy():
    color = _extended_parse('navy')
    assert color.name == 'navy'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (0, 0, 128)

def test_parse_color_oldlace():
    color = _extended_parse('oldlace')
    assert color.name == 'oldlace'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (253, 245, 230)

def test_parse_color_olive():
    color = _extended_parse('olive')
    assert color.name == 'olive'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (128, 128, 0)

def test_parse_color_olivedrab():
    color = _extended_parse('olivedrab')
    assert color.name == 'olivedrab'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (107, 142, 35)

def test_parse_color_orange():
    color = _extended_parse('orange')
    assert color.name == 'orange'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (255, 165, 0)

def test_parse_color_orangered():
    color = _extended_parse('orangered')
    assert color.name == 'orangered'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (255, 69, 0)

def test_parse_color_orchid():
    color = _extended_parse('orchid')
    assert color.name == 'orchid'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (215, 95, 215)

def test_parse_color_palegoldenrod():
    color = _extended_parse('palegoldenrod')
    assert color.name == 'palegoldenrod'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (238, 232, 170)

def test_parse_color_palegreen():
    color = _extended_parse('palegreen')
    assert color.name == 'palegreen'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (152, 251, 152)

def test_parse_color_paleturquoise():
    color = _extended_parse('paleturquoise')
    assert color.name == 'paleturquoise'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (175, 238, 238)

def test_parse_color_palevioletred():
    color = _extended_parse('palevioletred')
    assert color.name == 'palevioletred'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (219, 112, 147)

def test_parse_color_papayawhip():
    color = _extended_parse('papayawhip')
    assert color.name == 'papayawhip'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (255, 239, 213)

def test_parse_color_peachpuff():
    color = _extended_parse('peachpuff')
    assert color.name == 'peachpuff'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (255, 218, 185)

def test_parse_color_peru():
    color = _extended_parse('peru')
    assert color.name == 'peru'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (205, 133, 63)

def test_parse_color_pink():
    color = _extended_parse('pink')
    assert color.name == 'pink'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (255, 192, 203)

def test_parse_color_plum():
    color = _extended_parse('plum')
    assert color.name == 'plum'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (221, 160, 221)

def test_parse_color_powderblue():
    color = _extended_parse('powderblue')
    assert color.name == 'powderblue'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (176, 224, 230)

def test_parse_color_purple():
    color = _extended_parse('purple')
    assert color.name == 'purple'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (175, 0, 255)

def test_parse_color_rebeccapurple():
    color = _extended_parse('rebeccapurple')
    assert color.name == 'rebeccapurple'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (102, 51, 153)

def test_parse_color_red():
    color = _extended_parse('red')
    assert color.name == 'red'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (128, 0, 0)

def test_parse_color_rosybrown():
    color = _extended_parse('rosybrown')
    assert color.name == 'rosybrown'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (188, 143, 143)

def test_parse_color_royalblue():
    color = _extended_parse('royalblue')
    assert color.name == 'royalblue'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (65, 105, 225)

def test_parse_color_saddlebrown():
    color = _extended_parse('saddlebrown')
    assert color.name == 'saddlebrown'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (139, 69, 19)

def test_parse_color_salmon():
    color = _extended_parse('salmon')
    assert color.name == 'salmon'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (250, 128, 114)

def test_parse_color_sandybrown():
    color = _extended_parse('sandybrown')
    assert color.name == 'sandybrown'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (244, 164, 96)

def test_parse_color_seagreen():
    color = _extended_parse('seagreen')
    assert color.name == 'seagreen'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (46, 139, 87)

def test_parse_color_seashell():
    color = _extended_parse('seashell')
    assert color.name == 'seashell'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (255, 245, 238)

def test_parse_color_sienna():
    color = _extended_parse('sienna')
    assert color.name == 'sienna'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (160, 82, 45)

def test_parse_color_silver():
    color = _extended_parse('silver')
    assert color.name == 'silver'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (192, 192, 192)

def test_parse_color_skyblue():
    color = _extended_parse('skyblue')
    assert color.name == 'skyblue'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (135, 206, 235)

def test_parse_color_slateblue():
    color = _extended_parse('slateblue')
    assert color.name == 'slateblue'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (106, 90, 205)

def test_parse_color_slategray():
    color = _extended_parse('slategray')
    assert color.name == 'slategray'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (112, 128, 144)

def test_parse_color_slategrey():
    color = _extended_parse('slategrey')
    assert color.name == 'slategrey'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (112, 128, 144)

def test_parse_color_snow():
    color = _extended_parse('snow')
    assert color.name == 'snow'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (255, 250, 250)

def test_parse_color_springgreen():
    color = _extended_parse('springgreen')
    assert color.name == 'springgreen'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (0, 255, 127)

def test_parse_color_steelblue():
    color = _extended_parse('steelblue')
    assert color.name == 'steelblue'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (70, 130, 180)

def test_parse_color_tan():
    color = _extended_parse('tan')
    assert color.name == 'tan'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (215, 175, 135)

def test_parse_color_teal():
    color = _extended_parse('teal')
    assert color.name == 'teal'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (0, 128, 128)

def test_parse_color_thistle():
    color = _extended_parse('thistle')
    assert color.name == 'thistle'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (216, 191, 216)

def test_parse_color_tomato():
    color = _extended_parse('tomato')
    assert color.name == 'tomato'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (255, 99, 71)

def test_parse_color_turquoise():
    color = _extended_parse('turquoise')
    assert color.name == 'turquoise'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (64, 224, 208)

def test_parse_color_violet():
    color = _extended_parse('violet')
    assert color.name == 'violet'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (215, 135, 255)

def test_parse_color_wheat():
    color = _extended_parse('wheat')
    assert color.name == 'wheat'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (245, 222, 179)

def test_parse_color_white():
    color = _extended_parse('white')
    assert color.name == 'white'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (192, 192, 192)

def test_parse_color_whitesmoke():
    color = _extended_parse('whitesmoke')
    assert color.name == 'whitesmoke'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (245, 245, 245)

def test_parse_color_yellow():
    color = _extended_parse('yellow')
    assert color.name == 'yellow'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (128, 128, 0)

def test_parse_color_yellowgreen():
    color = _extended_parse('yellowgreen')
    assert color.name == 'yellowgreen'
    rgb = color.get_truecolor()
    assert (rgb.red, rgb.green, rgb.blue) == (154, 205, 50)
