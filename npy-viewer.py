
if __name__=='__main__':
    
    import argparse

    parser = argparse.ArgumentParser(description='view npy file in blender3D')
    parser.add_argument('npys', type=str, nargs='+',
                    help='paths to npy files')

    parser.add_argument('--min-max-norm', action='store_true')

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

    def minmax(a):
        a-=np.min(a)
        a/=np.max(a)
        return a

    for f in [fn for glb in args.npys for fn in glob.glob(glb)]:
        print(f)
        array = np.load(f).get('arr_0')
        if args.min_max_norm:
            array = minmax(array)
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
            print(os.system(' '.join(['blender', f'{npy_viewer_folder}/vdb-viewer.blend', '--python-expr', f'''"
import bpy;
bpy.ops.object.volume_import(filepath=\'{fn}\', relative_path=False, align=\'WORLD\', location=(0, 0, 0));
bpy.ops.object.select_all(action=\'SELECT\');
bpy.ops.transform.resize(
    value=(0.01, 0.01, 0.01),
    orient_type=\'GLOBAL\',
    orient_matrix=((1, 0, 0),(0, 1, 0),(0, 0, 1)),
    orient_matrix_type=\'GLOBAL\',
    mirror=True,
    use_proportional_edit=False,
    proportional_edit_falloff=\'SMOOTH\',
    proportional_size=1,
    use_proportional_connected=False,
    use_proportional_projected=False
);
bpy.context.selected_objects[0].data.materials.clear();
bpy.context.selected_objects[0].data.materials.append(bpy.data.materials[\'CT Scan Visualize Material\']);"'''.replace('\n', '')])))
            #print(os.system(' '.join(['blender', 'vdb-viewer.blend', '--python-expr', '"print(\'hello\')"'])))
    
