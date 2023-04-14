import pytest


@pytest.fixture()
def klines_batch():
    """Return a batch of klines."""
    return [
        [1658102400000, 0.602, 0.602, 0.602, 0.602, 0.0],
        [1658102460000, 0.602, 0.602, 0.602, 0.602, 0.0],
        [1658102520000, 0.603, 0.603, 0.601, 0.601, 428.11],
        [1658102580000, 0.601, 0.601, 0.601, 0.601, 53.58],
        [1658102640000, 0.601, 0.601, 0.601, 0.601, 0.0],
        [1658102700000, 0.601, 0.601, 0.601, 0.601, 0.0],
        [1658102760000, 0.601, 0.601, 0.601, 0.601, 0.0],
        [1658102820000, 0.603, 0.603, 0.603, 0.603, 1920.22],
        [1658102880000, 0.603, 0.603, 0.603, 0.603, 0.0],
        [1658102940000, 0.603, 0.603, 0.603, 0.603, 0.0],
        [1658103000000, 0.601, 0.602, 0.601, 0.602, 3351.59],
        [1658103060000, 0.602, 0.603, 0.602, 0.603, 969.66],
        [1658103120000, 0.603, 0.603, 0.603, 0.603, 126.07],
        [1658103180000, 0.603, 0.603, 0.603, 0.603, 371.22],
        [1658103240000, 0.603, 0.603, 0.603, 0.603, 83.55],
        [1658103300000, 0.603, 0.603, 0.603, 0.603, 0.0],
        [1658103360000, 0.603, 0.603, 0.603, 0.603, 0.0],
        [1658103420000, 0.603, 0.603, 0.603, 0.603, 0.0],
        [1658103480000, 0.603, 0.603, 0.603, 0.603, 107.79],
        [1658103540000, 0.603, 0.603, 0.603, 0.603, 0.0],
        [1658103600000, 0.603, 0.603, 0.603, 0.603, 0.0],
        [1658103660000, 0.603, 0.603, 0.603, 0.603, 0.0],
        [1658103720000, 0.602, 0.602, 0.601, 0.601, 528.2],
        [1658103780000, 0.602, 0.602, 0.602, 0.602, 1665.18],
        [1658103840000, 0.602, 0.602, 0.602, 0.602, 0.0],
        [1658103900000, 0.602, 0.603, 0.601, 0.603, 2490.66],
        [1658103960000, 0.603, 0.603, 0.603, 0.603, 33.67],
        [1658104020000, 0.603, 0.603, 0.603, 0.603, 0.0],
        [1658104080000, 0.601, 0.601, 0.601, 0.601, 317.5],
        [1658104140000, 0.601, 0.601, 0.601, 0.601, 0.0],
        [1658104200000, 0.603, 0.603, 0.603, 0.603, 19.53],
        [1658104260000, 0.603, 0.603, 0.603, 0.603, 1749.08],
        [1658104320000, 0.603, 0.603, 0.603, 0.603, 0.0],
        [1658104380000, 0.603, 0.603, 0.603, 0.603, 40.71],
        [1658104440000, 0.603, 0.603, 0.603, 0.603, 21.13],
        [1658104500000, 0.603, 0.603, 0.603, 0.603, 1121.84],
        [1658104560000, 0.602, 0.602, 0.602, 0.602, 194.22],
        [1658104620000, 0.602, 0.602, 0.602, 0.602, 0.0],
        [1658104680000, 0.602, 0.602, 0.602, 0.602, 0.0],
        [1658104740000, 0.601, 0.601, 0.599, 0.599, 12076.23],
        [1658104800000, 0.599, 0.599, 0.599, 0.599, 0.0],
        [1658104860000, 0.6, 0.6, 0.6, 0.6, 53.58],
        [1658104920000, 0.601, 0.601, 0.601, 0.601, 63.13],
        [1658104980000, 0.601, 0.601, 0.601, 0.601, 231.34],
        [1658105040000, 0.601, 0.601, 0.601, 0.601, 0.0],
        [1658105100000, 0.601, 0.601, 0.601, 0.601, 0.0],
        [1658105160000, 0.601, 0.601, 0.601, 0.601, 0.0],
        [1658105220000, 0.601, 0.601, 0.601, 0.601, 0.0],
        [1658105280000, 0.601, 0.601, 0.601, 0.601, 0.0],
        [1658105340000, 0.601, 0.601, 0.601, 0.601, 31.62],
        [1658105400000, 0.599, 0.599, 0.596, 0.596, 7097.94],
        [1658105460000, 0.596, 0.597, 0.596, 0.597, 117.28],
        [1658105520000, 0.596, 0.597, 0.596, 0.597, 809.82],
        [1658105580000, 0.597, 0.597, 0.597, 0.597, 0.0],
        [1658105640000, 0.596, 0.596, 0.596, 0.596, 121.94],
        [1658105700000, 0.596, 0.596, 0.596, 0.596, 20.99],
        [1658105760000, 0.596, 0.596, 0.596, 0.596, 0.0],
        [1658105820000, 0.596, 0.596, 0.596, 0.596, 0.0],
        [1658105880000, 0.596, 0.596, 0.596, 0.596, 686.02],
        [1658105940000, 0.596, 0.596, 0.596, 0.596, 0.0],
        [1658106000000, 0.596, 0.596, 0.596, 0.596, 0.0],
        [1658106060000, 0.598, 0.601, 0.598, 0.601, 7517.78],
        [1658106120000, 0.601, 0.601, 0.601, 0.601, 0.0],
        [1658106180000, 0.6, 0.6, 0.6, 0.6, 21.87],
        [1658106240000, 0.598, 0.598, 0.598, 0.598, 644.59],
        [1658106300000, 0.598, 0.598, 0.598, 0.598, 0.0],
        [1658106360000, 0.598, 0.598, 0.598, 0.598, 0.0],
        [1658106420000, 0.598, 0.598, 0.598, 0.598, 0.0],
        [1658106480000, 0.598, 0.598, 0.598, 0.598, 0.0],
        [1658106540000, 0.598, 0.598, 0.598, 0.598, 0.0],
        [1658106600000, 0.598, 0.598, 0.598, 0.598, 0.0],
        [1658106660000, 0.6, 0.6, 0.6, 0.6, 799.2],
        [1658106720000, 0.6, 0.6, 0.6, 0.6, 189.17],
        [1658106780000, 0.601, 0.601, 0.601, 0.601, 854.81],
        [1658106840000, 0.601, 0.601, 0.601, 0.601, 118.0],
        [1658106900000, 0.601, 0.601, 0.601, 0.601, 0.0],
        [1658106960000, 0.599, 0.599, 0.599, 0.599, 1274.33],
        [1658107020000, 0.599, 0.599, 0.599, 0.599, 0.0],
        [1658107080000, 0.599, 0.599, 0.599, 0.599, 0.0],
        [1658107140000, 0.599, 0.599, 0.599, 0.599, 0.0],
        [1658107200000, 0.601, 0.601, 0.601, 0.601, 20.25],
        [1658107260000, 0.601, 0.601, 0.601, 0.601, 0.0],
        [1658107320000, 0.601, 0.601, 0.601, 0.601, 0.0],
        [1658107380000, 0.601, 0.602, 0.601, 0.602, 534.26],
        [1658107440000, 0.602, 0.602, 0.602, 0.602, 83.68],
        [1658107500000, 0.602, 0.602, 0.602, 0.602, 0.0],
        [1658107560000, 0.602, 0.602, 0.602, 0.602, 0.0],
        [1658107620000, 0.602, 0.602, 0.602, 0.602, 0.0],
        [1658107680000, 0.602, 0.602, 0.602, 0.602, 128.63],
        [1658107740000, 0.602, 0.602, 0.602, 0.602, 0.0],
        [1658107800000, 0.602, 0.602, 0.602, 0.602, 0.0],
        [1658107860000, 0.602, 0.602, 0.602, 0.602, 363.86],
        [1658107920000, 0.601, 0.601, 0.6, 0.6, 3582.81],
        [1658107980000, 0.6, 0.6, 0.6, 0.6, 0.0],
        [1658108040000, 0.6, 0.601, 0.599, 0.601, 2850.09],
        [1658108100000, 0.6, 0.6, 0.597, 0.597, 12488.07],
        [1658108160000, 0.596, 0.596, 0.592, 0.593, 24941.87],
        [1658108220000, 0.593, 0.593, 0.593, 0.593, 0.0],
        [1658108280000, 0.592, 0.592, 0.592, 0.592, 86.05],
        [1658108340000, 0.592, 0.592, 0.592, 0.592, 0.0],
        [1658108400000, 0.592, 0.592, 0.592, 0.592, 104.44],
        [1658108460000, 0.592, 0.592, 0.592, 0.592, 0.0],
        [1658108520000, 0.592, 0.592, 0.592, 0.592, 0.0],
        [1658108580000, 0.593, 0.594, 0.593, 0.593, 3139.47],
        [1658108640000, 0.593, 0.593, 0.593, 0.593, 0.0],
        [1658108700000, 0.593, 0.593, 0.593, 0.593, 0.0],
        [1658108760000, 0.593, 0.593, 0.593, 0.593, 842.02],
        [1658108820000, 0.593, 0.593, 0.589, 0.591, 17187.43],
        [1658108880000, 0.592, 0.593, 0.592, 0.593, 72.84],
        [1658108940000, 0.593, 0.593, 0.593, 0.593, 0.0],
        [1658109000000, 0.593, 0.593, 0.593, 0.593, 0.0],
        [1658109060000, 0.592, 0.592, 0.59, 0.591, 3334.02],
        [1658109120000, 0.591, 0.591, 0.591, 0.591, 135.87],
        [1658109180000, 0.591, 0.591, 0.591, 0.591, 0.0],
        [1658109240000, 0.59, 0.59, 0.59, 0.59, 56.49],
        [1658109300000, 0.59, 0.591, 0.59, 0.591, 1006.32],
        [1658109360000, 0.591, 0.591, 0.591, 0.591, 0.0],
        [1658109420000, 0.592, 0.592, 0.592, 0.592, 25.33],
        [1658109480000, 0.59, 0.59, 0.59, 0.59, 2796.38],
        [1658109540000, 0.59, 0.59, 0.59, 0.59, 0.0],
        [1658109600000, 0.591, 0.591, 0.591, 0.591, 4725.32],
        [1658109660000, 0.59, 0.591, 0.59, 0.591, 1008.67],
        [1658109720000, 0.591, 0.591, 0.591, 0.591, 0.0],
        [1658109780000, 0.591, 0.591, 0.591, 0.591, 0.0],
        [1658109840000, 0.592, 0.592, 0.59, 0.592, 155.64],
        [1658109900000, 0.592, 0.592, 0.592, 0.592, 20.92],
        [1658109960000, 0.591, 0.591, 0.591, 0.591, 465.0],
        [1658110020000, 0.591, 0.591, 0.591, 0.591, 0.0],
        [1658110080000, 0.591, 0.591, 0.591, 0.591, 0.0],
        [1658110140000, 0.591, 0.591, 0.591, 0.591, 0.0],
        [1658110200000, 0.591, 0.591, 0.591, 0.591, 0.0],
        [1658110260000, 0.591, 0.591, 0.591, 0.591, 0.0],
        [1658110320000, 0.591, 0.591, 0.591, 0.591, 0.0],
        [1658110380000, 0.591, 0.591, 0.591, 0.591, 0.0],
        [1658110440000, 0.591, 0.591, 0.591, 0.591, 0.0],
        [1658110500000, 0.591, 0.591, 0.591, 0.591, 0.0],
        [1658110560000, 0.592, 0.592, 0.592, 0.592, 168.91],
        [1658110620000, 0.592, 0.592, 0.592, 0.592, 823.91],
        [1658110680000, 0.592, 0.592, 0.592, 0.592, 0.0],
        [1658110740000, 0.592, 0.592, 0.592, 0.592, 0.0],
        [1658110800000, 0.592, 0.592, 0.592, 0.592, 0.0],
        [1658110860000, 0.592, 0.593, 0.592, 0.593, 1095.1],
        [1658110920000, 0.593, 0.593, 0.593, 0.593, 0.0],
        [1658110980000, 0.593, 0.593, 0.593, 0.593, 0.0],
        [1658111040000, 0.593, 0.593, 0.593, 0.593, 0.0],
        [1658111100000, 0.593, 0.593, 0.593, 0.593, 0.0],
        [1658111160000, 0.593, 0.593, 0.593, 0.593, 0.0],
        [1658111220000, 0.593, 0.593, 0.593, 0.593, 0.0],
        [1658111280000, 0.593, 0.593, 0.593, 0.593, 0.0],
        [1658111340000, 0.593, 0.593, 0.593, 0.593, 0.0],
        [1658111400000, 0.593, 0.593, 0.593, 0.593, 0.0],
        [1658111460000, 0.593, 0.593, 0.593, 0.593, 0.0],
        [1658111520000, 0.593, 0.593, 0.593, 0.593, 0.0],
        [1658111580000, 0.593, 0.593, 0.593, 0.593, 0.0],
        [1658111640000, 0.593, 0.593, 0.593, 0.593, 0.0],
        [1658111700000, 0.593, 0.593, 0.593, 0.593, 0.0],
        [1658111760000, 0.593, 0.593, 0.593, 0.593, 0.0],
        [1658111820000, 0.593, 0.593, 0.593, 0.593, 0.0],
        [1658111880000, 0.592, 0.592, 0.592, 0.592, 175.86],
        [1658111940000, 0.592, 0.592, 0.592, 0.592, 0.0],
        [1658112000000, 0.592, 0.592, 0.592, 0.592, 0.0],
        [1658112060000, 0.592, 0.592, 0.592, 0.592, 0.0],
        [1658112120000, 0.592, 0.592, 0.592, 0.592, 0.0],
        [1658112180000, 0.594, 0.596, 0.594, 0.596, 4585.96],
        [1658112240000, 0.596, 0.596, 0.596, 0.596, 0.0],
        [1658112300000, 0.596, 0.596, 0.596, 0.596, 46.9],
        [1658112360000, 0.596, 0.596, 0.596, 0.596, 0.0],
        [1658112420000, 0.597, 0.597, 0.597, 0.597, 914.13],
        [1658112480000, 0.597, 0.597, 0.597, 0.597, 536.13],
        [1658112540000, 0.596, 0.596, 0.595, 0.595, 129.29],
        [1658112600000, 0.595, 0.595, 0.595, 0.595, 0.0],
        [1658112660000, 0.595, 0.595, 0.595, 0.595, 0.0],
        [1658112720000, 0.597, 0.597, 0.597, 0.597, 83.61],
        [1658112780000, 0.597, 0.598, 0.596, 0.598, 6775.24],
        [1658112840000, 0.598, 0.599, 0.598, 0.599, 775.07],
        [1658112900000, 0.599, 0.599, 0.599, 0.599, 32.87],
        [1658112960000, 0.599, 0.599, 0.599, 0.599, 0.0],
        [1658113020000, 0.599, 0.599, 0.599, 0.599, 0.0],
        [1658113080000, 0.599, 0.599, 0.599, 0.599, 0.0],
        [1658113140000, 0.599, 0.599, 0.599, 0.599, 0.0],
        [1658113200000, 0.597, 0.597, 0.597, 0.597, 1241.28],
        [1658113260000, 0.597, 0.597, 0.597, 0.597, 0.0],
        [1658113320000, 0.599, 0.599, 0.597, 0.597, 511.42],
        [1658113380000, 0.597, 0.597, 0.597, 0.597, 0.0],
        [1658113440000, 0.597, 0.597, 0.597, 0.597, 99.07],
        [1658113500000, 0.599, 0.599, 0.598, 0.598, 490.04],
        [1658113560000, 0.598, 0.598, 0.598, 0.598, 0.0],
        [1658113620000, 0.598, 0.598, 0.597, 0.597, 2194.1],
        [1658113680000, 0.598, 0.598, 0.598, 0.598, 167.57],
        [1658113740000, 0.598, 0.598, 0.598, 0.598, 0.0],
        [1658113800000, 0.597, 0.597, 0.596, 0.596, 2914.12],
        [1658113860000, 0.596, 0.596, 0.596, 0.596, 0.0],
        [1658113920000, 0.596, 0.596, 0.596, 0.596, 0.0],
        [1658113980000, 0.595, 0.596, 0.595, 0.596, 4257.51],
        [1658114040000, 0.594, 0.594, 0.594, 0.594, 3653.35],
        [1658114100000, 0.594, 0.594, 0.594, 0.594, 0.0],
        [1658114160000, 0.594, 0.594, 0.594, 0.594, 24.75],
        [1658114220000, 0.594, 0.594, 0.594, 0.594, 0.0],
        [1658114280000, 0.595, 0.595, 0.595, 0.595, 465.0],
        [1658114340000, 0.595, 0.595, 0.595, 0.595, 196.33],
        [1658114400000, 0.595, 0.595, 0.595, 0.595, 0.0],
        [1658114460000, 0.595, 0.595, 0.595, 0.595, 0.0],
        [1658114520000, 0.596, 0.596, 0.596, 0.596, 1000.52],
        [1658114580000, 0.596, 0.596, 0.596, 0.596, 954.65],
        [1658114640000, 0.596, 0.596, 0.596, 0.596, 0.0],
        [1658114700000, 0.596, 0.596, 0.596, 0.596, 0.0],
        [1658114760000, 0.596, 0.596, 0.596, 0.596, 6588.0],
        [1658114820000, 0.596, 0.596, 0.596, 0.596, 273.68],
        [1658114880000, 0.596, 0.596, 0.596, 0.596, 0.0],
        [1658114940000, 0.596, 0.596, 0.596, 0.596, 0.0],
        [1658115000000, 0.596, 0.596, 0.596, 0.596, 0.0],
        [1658115060000, 0.596, 0.596, 0.596, 0.596, 341.88],
        [1658115120000, 0.596, 0.596, 0.596, 0.596, 0.0],
        [1658115180000, 0.596, 0.596, 0.596, 0.596, 0.0],
        [1658115240000, 0.596, 0.596, 0.596, 0.596, 0.0],
        [1658115300000, 0.596, 0.596, 0.596, 0.596, 285.53],
        [1658115360000, 0.596, 0.596, 0.596, 0.596, 0.0],
        [1658115420000, 0.596, 0.596, 0.596, 0.596, 0.0],
        [1658115480000, 0.596, 0.596, 0.596, 0.596, 0.0],
        [1658115540000, 0.596, 0.596, 0.596, 0.596, 0.0],
        [1658115600000, 0.596, 0.596, 0.596, 0.596, 0.0],
        [1658115660000, 0.596, 0.596, 0.596, 0.596, 0.0],
        [1658115720000, 0.596, 0.596, 0.596, 0.596, 585.57],
        [1658115780000, 0.597, 0.597, 0.596, 0.596, 2549.72],
        [1658115840000, 0.596, 0.596, 0.596, 0.596, 527.94],
        [1658115900000, 0.596, 0.596, 0.596, 0.596, 0.0],
        [1658115960000, 0.596, 0.596, 0.596, 0.596, 0.0],
        [1658116020000, 0.596, 0.596, 0.596, 0.596, 0.0],
        [1658116080000, 0.596, 0.596, 0.596, 0.596, 0.0],
        [1658116140000, 0.596, 0.596, 0.596, 0.596, 0.0],
        [1658116200000, 0.596, 0.596, 0.596, 0.596, 0.0],
        [1658116260000, 0.596, 0.596, 0.596, 0.596, 0.0],
        [1658116320000, 0.596, 0.596, 0.596, 0.596, 0.0],
        [1658116380000, 0.597, 0.597, 0.597, 0.597, 28.01],
        [1658116440000, 0.597, 0.597, 0.597, 0.597, 0.0],
        [1658116500000, 0.597, 0.597, 0.597, 0.597, 0.0],
        [1658116560000, 0.595, 0.596, 0.594, 0.596, 4368.3],
        [1658116620000, 0.596, 0.596, 0.596, 0.596, 84.57],
        [1658116680000, 0.596, 0.596, 0.596, 0.596, 0.0],
        [1658116740000, 0.595, 0.595, 0.595, 0.595, 394.03],
        [1658116800000, 0.595, 0.595, 0.594, 0.594, 178.9],
        [1658116860000, 0.594, 0.594, 0.594, 0.594, 0.0],
        [1658116920000, 0.594, 0.594, 0.594, 0.594, 0.0],
        [1658116980000, 0.594, 0.594, 0.594, 0.594, 0.0],
        [1658117040000, 0.594, 0.594, 0.594, 0.594, 2612.71],
        [1658117100000, 0.595, 0.595, 0.595, 0.595, 393.63],
        [1658117160000, 0.595, 0.595, 0.595, 0.595, 0.0],
        [1658117220000, 0.595, 0.595, 0.595, 0.595, 0.0],
        [1658117280000, 0.595, 0.595, 0.595, 0.595, 0.0],
        [1658117340000, 0.595, 0.595, 0.595, 0.595, 0.0],
        [1658117400000, 0.595, 0.595, 0.595, 0.595, 0.0],
        [1658117460000, 0.595, 0.595, 0.595, 0.595, 0.0],
        [1658117520000, 0.594, 0.594, 0.594, 0.594, 24.87],
        [1658117580000, 0.594, 0.594, 0.594, 0.594, 0.0],
        [1658117640000, 0.594, 0.594, 0.594, 0.594, 0.0],
        [1658117700000, 0.594, 0.594, 0.594, 0.594, 0.0],
        [1658117760000, 0.594, 0.594, 0.594, 0.594, 0.0],
        [1658117820000, 0.594, 0.594, 0.594, 0.594, 0.0],
        [1658117880000, 0.594, 0.594, 0.594, 0.594, 0.0],
        [1658117940000, 0.594, 0.594, 0.594, 0.594, 0.0],
        [1658118000000, 0.594, 0.594, 0.594, 0.594, 0.0],
        [1658118060000, 0.594, 0.594, 0.594, 0.594, 0.0],
        [1658118120000, 0.594, 0.594, 0.592, 0.592, 6489.86],
        [1658118180000, 0.592, 0.592, 0.592, 0.592, 0.0],
        [1658118240000, 0.592, 0.592, 0.592, 0.592, 0.0],
        [1658118300000, 0.592, 0.592, 0.592, 0.592, 0.0],
        [1658118360000, 0.592, 0.592, 0.592, 0.592, 0.0],
        [1658118420000, 0.594, 0.597, 0.594, 0.596, 11041.51],
        [1658118480000, 0.596, 0.596, 0.596, 0.596, 465.0],
        [1658118540000, 0.597, 0.597, 0.597, 0.597, 3029.99],
        [1658118600000, 0.597, 0.597, 0.597, 0.597, 167.5],
        [1658118660000, 0.595, 0.595, 0.594, 0.594, 2976.67],
        [1658118720000, 0.594, 0.595, 0.594, 0.595, 284.21],
        [1658118780000, 0.595, 0.595, 0.595, 0.595, 0.0],
        [1658118840000, 0.594, 0.594, 0.594, 0.594, 173.97],
        [1658118900000, 0.594, 0.594, 0.594, 0.594, 3460.57],
        [1658118960000, 0.594, 0.594, 0.594, 0.594, 0.0],
        [1658119020000, 0.596, 0.596, 0.596, 0.596, 16.78],
        [1658119080000, 0.596, 0.596, 0.596, 0.596, 0.0],
        [1658119140000, 0.596, 0.596, 0.596, 0.596, 0.0],
        [1658119200000, 0.596, 0.596, 0.596, 0.596, 0.0],
        [1658119260000, 0.596, 0.596, 0.596, 0.596, 0.0],
        [1658119320000, 0.596, 0.596, 0.596, 0.596, 0.0],
        [1658119380000, 0.596, 0.596, 0.596, 0.596, 121.75],
        [1658119440000, 0.596, 0.596, 0.596, 0.596, 0.0],
        [1658119500000, 0.596, 0.596, 0.596, 0.596, 0.0],
        [1658119560000, 0.596, 0.596, 0.596, 0.596, 3526.09],
        [1658119620000, 0.596, 0.596, 0.596, 0.596, 0.0],
        [1658119680000, 0.596, 0.596, 0.596, 0.596, 615.29],
        [1658119740000, 0.596, 0.596, 0.596, 0.596, 0.0],
        [1658119800000, 0.596, 0.598, 0.596, 0.598, 2443.96],
        [1658119860000, 0.598, 0.598, 0.598, 0.598, 0.0],
        [1658119920000, 0.598, 0.598, 0.598, 0.598, 21.84],
        [1658119980000, 0.598, 0.598, 0.598, 0.598, 0.0],
        [1658120040000, 0.598, 0.598, 0.598, 0.598, 0.0],
        [1658120100000, 0.598, 0.598, 0.598, 0.598, 0.0],
        [1658120160000, 0.596, 0.596, 0.596, 0.596, 64.06],
        [1658120220000, 0.596, 0.596, 0.596, 0.596, 0.0],
        [1658120280000, 0.596, 0.596, 0.596, 0.596, 0.0],
        [1658120340000, 0.596, 0.596, 0.596, 0.596, 0.0],
        [1658120400000, 0.599, 0.599, 0.599, 0.599, 98.25],
        [1658120460000, 0.599, 0.599, 0.599, 0.599, 0.0],
        [1658120520000, 0.599, 0.599, 0.599, 0.599, 390.88],
        [1658120580000, 0.599, 0.599, 0.599, 0.599, 0.0],
        [1658120640000, 0.599, 0.599, 0.599, 0.599, 0.0],
        [1658120700000, 0.599, 0.599, 0.599, 0.599, 2661.55],
        [1658120760000, 0.599, 0.599, 0.599, 0.599, 531.73],
        [1658120820000, 0.599, 0.599, 0.598, 0.598, 94.89],
        [1658120880000, 0.599, 0.6, 0.599, 0.599, 892.7],
        [1658120940000, 0.6, 0.601, 0.6, 0.601, 9099.87],
        [1658121000000, 0.602, 0.602, 0.6, 0.6, 1505.06],
        [1658121060000, 0.602, 0.602, 0.601, 0.601, 2288.0],
        [1658121120000, 0.601, 0.601, 0.601, 0.601, 0.0],
        [1658121180000, 0.602, 0.602, 0.602, 0.602, 1019.63],
        [1658121240000, 0.6, 0.602, 0.6, 0.602, 1139.97],
        [1658121300000, 0.602, 0.602, 0.602, 0.602, 21.7],
        [1658121360000, 0.602, 0.602, 0.602, 0.602, 0.0],
        [1658121420000, 0.602, 0.602, 0.602, 0.602, 1765.16],
        [1658121480000, 0.603, 0.603, 0.603, 0.603, 1105.19],
        [1658121540000, 0.603, 0.603, 0.603, 0.603, 425.0],
        [1658121600000, 0.603, 0.603, 0.603, 0.603, 2012.38],
        [1658121660000, 0.604, 0.604, 0.604, 0.604, 680.64],
        [1658121720000, 0.604, 0.607, 0.604, 0.607, 6267.03],
        [1658121780000, 0.606, 0.608, 0.604, 0.604, 6337.97],
        [1658121840000, 0.606, 0.607, 0.606, 0.607, 142.37],
        [1658121900000, 0.605, 0.605, 0.605, 0.605, 154.47],
        [1658121960000, 0.606, 0.607, 0.606, 0.607, 2565.71],
        [1658122020000, 0.607, 0.607, 0.607, 0.607, 264.36],
        [1658122080000, 0.607, 0.607, 0.605, 0.605, 404.89],
        [1658122140000, 0.607, 0.615, 0.607, 0.61, 9869.27],
        [1658122200000, 0.611, 0.612, 0.611, 0.612, 1745.27],
        [1658122260000, 0.61, 0.611, 0.61, 0.611, 180.84],
        [1658122320000, 0.611, 0.611, 0.609, 0.609, 283.25],
        [1658122380000, 0.608, 0.608, 0.608, 0.608, 132.71],
        [1658122440000, 0.608, 0.608, 0.608, 0.608, 0.0],
        [1658122500000, 0.608, 0.609, 0.608, 0.609, 440.58],
        [1658122560000, 0.609, 0.609, 0.609, 0.609, 1782.52],
        [1658122620000, 0.608, 0.608, 0.608, 0.608, 402.98],
        [1658122680000, 0.608, 0.608, 0.608, 0.608, 0.0],
        [1658122740000, 0.609, 0.611, 0.609, 0.611, 1003.68],
        [1658122800000, 0.611, 0.611, 0.61, 0.611, 421.69],
        [1658122860000, 0.61, 0.61, 0.61, 0.61, 1639.34],
        [1658122920000, 0.61, 0.611, 0.61, 0.611, 356.29],
        [1658122980000, 0.611, 0.612, 0.61, 0.61, 3073.8],
        [1658123040000, 0.61, 0.61, 0.61, 0.61, 0.0],
        [1658123100000, 0.61, 0.613, 0.61, 0.61, 3719.09],
        [1658123160000, 0.61, 0.61, 0.609, 0.609, 4376.68],
        [1658123220000, 0.609, 0.609, 0.609, 0.609, 47.17],
        [1658123280000, 0.61, 0.611, 0.61, 0.611, 116.23],
        [1658123340000, 0.611, 0.613, 0.611, 0.613, 1619.36],
        [1658123400000, 0.612, 0.612, 0.612, 0.612, 1321.72],
        [1658123460000, 0.611, 0.613, 0.61, 0.613, 1492.2],
        [1658123520000, 0.613, 0.613, 0.613, 0.613, 0.0],
        [1658123580000, 0.613, 0.613, 0.613, 0.613, 0.0],
        [1658123640000, 0.612, 0.612, 0.612, 0.612, 326.24],
        [1658123700000, 0.612, 0.612, 0.612, 0.612, 0.0],
        [1658123760000, 0.612, 0.612, 0.612, 0.612, 315.76],
        [1658123820000, 0.612, 0.614, 0.612, 0.614, 1092.23],
        [1658123880000, 0.612, 0.612, 0.612, 0.612, 93.56],
        [1658123940000, 0.612, 0.612, 0.612, 0.612, 32.67],
        [1658124000000, 0.613, 0.613, 0.613, 0.613, 74.84],
        [1658124060000, 0.613, 0.613, 0.613, 0.613, 0.0],
        [1658124120000, 0.612, 0.612, 0.612, 0.612, 1403.3],
        [1658124180000, 0.612, 0.612, 0.612, 0.612, 340.1],
        [1658124240000, 0.612, 0.612, 0.612, 0.612, 0.0],
        [1658124300000, 0.611, 0.611, 0.61, 0.61, 4485.65],
        [1658124360000, 0.61, 0.61, 0.61, 0.61, 0.0],
        [1658124420000, 0.61, 0.613, 0.61, 0.613, 4793.47],
        [1658124480000, 0.611, 0.611, 0.611, 0.611, 416.24],
        [1658124540000, 0.612, 0.612, 0.612, 0.612, 17.62],
        [1658124600000, 0.612, 0.612, 0.612, 0.612, 0.0],
        [1658124660000, 0.612, 0.613, 0.612, 0.612, 1378.82],
        [1658124720000, 0.612, 0.613, 0.612, 0.613, 120.31],
        [1658124780000, 0.613, 0.613, 0.613, 0.613, 0.0],
        [1658124840000, 0.612, 0.613, 0.612, 0.612, 505.28],
        [1658124900000, 0.613, 0.613, 0.612, 0.612, 663.63],
        [1658124960000, 0.613, 0.613, 0.613, 0.613, 719.91],
        [1658125020000, 0.613, 0.617, 0.613, 0.615, 5681.35],
        [1658125080000, 0.615, 0.616, 0.615, 0.616, 1283.43],
        [1658125140000, 0.616, 0.616, 0.616, 0.616, 0.0],
        [1658125200000, 0.614, 0.615, 0.614, 0.615, 377.58],
        [1658125260000, 0.614, 0.615, 0.613, 0.615, 5812.27],
        [1658125320000, 0.615, 0.615, 0.615, 0.615, 210.91],
        [1658125380000, 0.614, 0.616, 0.614, 0.616, 1378.8],
        [1658125440000, 0.617, 0.617, 0.614, 0.617, 3615.22],
        [1658125500000, 0.616, 0.616, 0.616, 0.616, 98.9],
        [1658125560000, 0.617, 0.619, 0.616, 0.619, 11355.25],
        [1658125620000, 0.619, 0.619, 0.619, 0.619, 154.98],
        [1658125680000, 0.619, 0.621, 0.619, 0.621, 3389.25],
        [1658125740000, 0.621, 0.621, 0.621, 0.621, 0.0],
        [1658125800000, 0.62, 0.62, 0.616, 0.618, 10104.52],
        [1658125860000, 0.618, 0.62, 0.618, 0.62, 1459.87],
        [1658125920000, 0.621, 0.621, 0.621, 0.621, 1602.51],
        [1658125980000, 0.622, 0.622, 0.622, 0.622, 27.99],
        [1658126040000, 0.621, 0.621, 0.62, 0.621, 2255.1],
        [1658126100000, 0.621, 0.621, 0.621, 0.621, 0.0],
        [1658126160000, 0.621, 0.622, 0.62, 0.622, 2338.58],
        [1658126220000, 0.623, 0.623, 0.621, 0.623, 3856.49],
        [1658126280000, 0.623, 0.63, 0.623, 0.626, 38971.33],
        [1658126340000, 0.626, 0.631, 0.626, 0.628, 11240.64],
        [1658126400000, 0.626, 0.626, 0.626, 0.626, 346.73],
        [1658126460000, 0.626, 0.629, 0.626, 0.629, 945.84],
        [1658126520000, 0.629, 0.629, 0.629, 0.629, 35.68],
        [1658126580000, 0.629, 0.629, 0.629, 0.629, 1526.58],
        [1658126640000, 0.628, 0.628, 0.627, 0.627, 366.94],
        [1658126700000, 0.627, 0.627, 0.627, 0.627, 0.0],
        [1658126760000, 0.626, 0.626, 0.626, 0.626, 35.91],
        [1658126820000, 0.625, 0.625, 0.623, 0.623, 3118.22],
        [1658126880000, 0.624, 0.624, 0.622, 0.622, 9780.87],
        [1658126940000, 0.623, 0.623, 0.621, 0.621, 3680.02],
        [1658127000000, 0.623, 0.623, 0.623, 0.623, 823.94],
        [1658127060000, 0.624, 0.624, 0.624, 0.624, 36.14],
        [1658127120000, 0.625, 0.625, 0.623, 0.625, 2252.25],
        [1658127180000, 0.625, 0.625, 0.625, 0.625, 0.0],
        [1658127240000, 0.625, 0.625, 0.625, 0.625, 0.0],
        [1658127300000, 0.623, 0.623, 0.623, 0.623, 783.67],
        [1658127360000, 0.623, 0.623, 0.623, 0.623, 0.0],
        [1658127420000, 0.623, 0.623, 0.623, 0.623, 0.0],
        [1658127480000, 0.623, 0.625, 0.623, 0.625, 1300.87],
        [1658127540000, 0.625, 0.625, 0.625, 0.625, 0.0],
        [1658127600000, 0.623, 0.626, 0.621, 0.626, 5644.49],
        [1658127660000, 0.626, 0.626, 0.626, 0.626, 0.0],
        [1658127720000, 0.626, 0.626, 0.626, 0.626, 465.0],
        [1658127780000, 0.626, 0.626, 0.626, 0.626, 0.0],
        [1658127840000, 0.626, 0.626, 0.626, 0.626, 0.0],
        [1658127900000, 0.626, 0.626, 0.626, 0.626, 0.0],
        [1658127960000, 0.626, 0.626, 0.626, 0.626, 38.19],
        [1658128020000, 0.626, 0.627, 0.626, 0.626, 2018.41],
        [1658128080000, 0.626, 0.627, 0.626, 0.627, 3574.99],
        [1658128140000, 0.627, 0.628, 0.627, 0.628, 2271.5],
        [1658128200000, 0.629, 0.63, 0.629, 0.63, 1801.39],
        [1658128260000, 0.628, 0.628, 0.625, 0.625, 1967.91],
        [1658128320000, 0.625, 0.625, 0.624, 0.625, 2486.33],
        [1658128380000, 0.625, 0.625, 0.625, 0.625, 0.0],
        [1658128440000, 0.625, 0.625, 0.625, 0.625, 156.09],
        [1658128500000, 0.625, 0.625, 0.625, 0.625, 0.0],
        [1658128560000, 0.625, 0.625, 0.625, 0.625, 2188.94],
        [1658128620000, 0.625, 0.625, 0.625, 0.625, 0.0],
        [1658128680000, 0.624, 0.624, 0.624, 0.624, 861.21],
        [1658128740000, 0.623, 0.623, 0.623, 0.623, 169.77],
        [1658128800000, 0.623, 0.625, 0.623, 0.625, 2497.56],
        [1658128860000, 0.625, 0.625, 0.625, 0.625, 48.39],
        [1658128920000, 0.622, 0.624, 0.618, 0.621, 12740.18],
        [1658128980000, 0.62, 0.62, 0.609, 0.613, 86091.81],
        [1658129040000, 0.612, 0.613, 0.612, 0.613, 2422.56],
        [1658129100000, 0.614, 0.62, 0.614, 0.62, 8322.54],
        [1658129160000, 0.619, 0.619, 0.617, 0.617, 1892.87],
        [1658129220000, 0.617, 0.617, 0.617, 0.617, 1591.87],
        [1658129280000, 0.617, 0.617, 0.617, 0.617, 126.3],
        [1658129340000, 0.617, 0.617, 0.617, 0.617, 0.0],
        [1658129400000, 0.619, 0.621, 0.619, 0.621, 24032.21],
        [1658129460000, 0.621, 0.625, 0.621, 0.622, 21549.07],
        [1658129520000, 0.623, 0.625, 0.622, 0.622, 8458.56],
        [1658129580000, 0.622, 0.622, 0.622, 0.622, 0.0],
        [1658129640000, 0.624, 0.629, 0.623, 0.629, 7026.89],
        [1658129700000, 0.629, 0.639, 0.628, 0.639, 95378.25],
        [1658129760000, 0.638, 0.64, 0.636, 0.64, 19036.55],
        [1658129820000, 0.639, 0.64, 0.638, 0.639, 2462.09],
        [1658129880000, 0.639, 0.645, 0.639, 0.643, 43312.59],
        [1658129940000, 0.642, 0.644, 0.638, 0.638, 6306.38],
        [1658130000000, 0.638, 0.643, 0.638, 0.64, 11036.74],
        [1658130060000, 0.639, 0.643, 0.639, 0.639, 5770.02],
        [1658130120000, 0.639, 0.641, 0.639, 0.639, 1049.63],
        [1658130180000, 0.639, 0.639, 0.638, 0.639, 1310.73],
        [1658130240000, 0.64, 0.642, 0.639, 0.64, 4111.45],
        [1658130300000, 0.641, 0.642, 0.641, 0.642, 7533.76],
        [1658130360000, 0.643, 0.644, 0.642, 0.644, 2917.64],
        [1658130420000, 0.644, 0.647, 0.644, 0.646, 17324.9],
        [1658130480000, 0.647, 0.648, 0.647, 0.647, 4462.51],
        [1658130540000, 0.648, 0.648, 0.647, 0.647, 3037.12],
        [1658130600000, 0.647, 0.648, 0.647, 0.647, 11993.02],
        [1658130660000, 0.648, 0.648, 0.647, 0.647, 838.78],
        [1658130720000, 0.648, 0.649, 0.647, 0.649, 19082.01],
        [1658130780000, 0.648, 0.649, 0.646, 0.646, 6916.7],
        [1658130840000, 0.644, 0.647, 0.642, 0.643, 6844.2],
        [1658130900000, 0.645, 0.645, 0.644, 0.644, 1129.42],
        [1658130960000, 0.645, 0.645, 0.642, 0.642, 32358.92],
        [1658131020000, 0.642, 0.644, 0.642, 0.644, 142.8],
        [1658131080000, 0.644, 0.645, 0.638, 0.638, 38757.53],
        [1658131140000, 0.64, 0.64, 0.639, 0.639, 428.16],
        [1658131200000, 0.64, 0.64, 0.638, 0.639, 18216.15],
        [1658131260000, 0.639, 0.639, 0.638, 0.638, 5818.16],
        [1658131320000, 0.64, 0.641, 0.64, 0.64, 1610.95],
        [1658131380000, 0.639, 0.639, 0.638, 0.639, 1485.61],
        [1658131440000, 0.639, 0.643, 0.639, 0.643, 3457.42],
        [1658131500000, 0.642, 0.644, 0.642, 0.642, 1265.68],
        [1658131560000, 0.644, 0.645, 0.643, 0.645, 1185.91],
        [1658131620000, 0.645, 0.649, 0.642, 0.643, 16726.52],
        [1658131680000, 0.643, 0.643, 0.642, 0.642, 1788.61],
        [1658131740000, 0.642, 0.642, 0.642, 0.642, 0.0],
        [1658131800000, 0.642, 0.646, 0.642, 0.646, 868.65],
        [1658131860000, 0.644, 0.645, 0.642, 0.642, 785.94],
        [1658131920000, 0.644, 0.648, 0.644, 0.644, 7801.03],
        [1658131980000, 0.645, 0.646, 0.643, 0.645, 1821.88],
        [1658132040000, 0.645, 0.645, 0.642, 0.645, 1075.15],
        [1658132100000, 0.642, 0.642, 0.641, 0.642, 2678.8],
        [1658132160000, 0.64, 0.64, 0.64, 0.64, 398.05],
        [1658132220000, 0.642, 0.642, 0.641, 0.641, 669.63],
        [1658132280000, 0.641, 0.641, 0.639, 0.639, 10264.65],
        [1658132340000, 0.642, 0.642, 0.642, 0.642, 161.01],
    ]