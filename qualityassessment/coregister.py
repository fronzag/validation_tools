# 3rd party
from arosics import COREG_LOCAL


def run_arosics(ref_geoArr, targ_geoArr, grid_res, window_size, path_out, projectDir, shp_output= None):
    """
        Coregister two images using Arosics package.

        Parameters:
            ref_geoArr (GeoArray): reference image.
            targ_geoArr (GeoArray): target image (to be registered).
            grid_res (int): arosics parameter: grid resolution.
            window_size ((int, int)): arosics parameter: moving window size.
            path_out (str): output path of registered image.
            projectDir (str): project directory.
            shp_output (str): output .shp directory.
    """
    kwargs = {
        'grid_res'     : grid_res,
        'window_size'  : window_size,
        'path_out'     : path_out,
        'projectDir'   : projectDir,
        'q'            : False,
    }

    CRL = COREG_LOCAL(ref_geoArr, targ_geoArr, **kwargs)

    CRL.correct_shifts()

    ###Visualize tie point grid with INITIAL shifts present in your input target image
    ## import matplotlib
    ## matplotlib.use("TkAgg")
    # CRL.view_CoRegPoints(figsize=(15,15), backgroundIm='ref')
    ###Visualize tie point grid with shifts present AFTER shift correction
    # CRL_after_corr = COREG_LOCAL(img_reference.format('nir'), CRL.path_out, **kwargs)
    # CRL_after_corr.view_CoRegPoints(figsize=(15,15),backgroundIm='ref')

    if shp_output is not None:
        CRL.tiepoint_grid.to_PointShapefile(path_out=shp_output)

    return
