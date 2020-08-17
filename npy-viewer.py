
if __name__=='__main__':
    
    import argparse

    parser = argparse.ArgumentParser(description='view npy file in blender3D')
    parser.add_argument('npys', type=str, nargs='+',
                    help='paths to npy files')

    args = parser.parse_args()

    import os
    import sys

    npy_viewer_folder = os.path.dirname(__file__)

    if len(args.npys)==0:
        raise ValueError('no files to open')
        sys.exit()

    import glob

    import numpy as np

    import pyopenvdb as vdb

    import subprocess

    import tempfile

    for f in [fn for glb in args.npys for fn in glob.glob(glb)]:
        print(f)
        array = np.load(f).get('arr_0')
        if len(array.shape)==3: # 3d data
            vecgrid = vdb.FloatGrid()
            vecgrid.name = 'density'
        if len(array.shape)==4:
            if array.shape[3]==3: # might be color data
                vecgrid = vdb.Vec3SGrid()
                vecgrid.name = 'color'
            else:
                print('4D data not yet supported, skipping:', f)
                continue
        vecgrid.copyFromArray(array)
        with tempfile.TemporaryDirectory() as tmpdir:
            dr = os.path.join(tmpdir, os.path.basename(f))
            subprocess.run(['mkdir', '-p', dr])
            fn = os.path.join(dr, os.path.basename(f)+'.vdb')
            vdb.write(fn, grids=[vecgrid])
            print(os.system(' '.join(['blender', f'{npy_viewer_folder}/vdb-viewer.blend', '--python-expr', f'"import bpy;bpy.ops.object.volume_import(filepath=\'{fn}\', relative_path=False, align=\'WORLD\', location=(0, 0, 0))"'])))
            #print(os.system(' '.join(['blender', 'vdb-viewer.blend', '--python-expr', '"print(\'hello\')"'])))
    
