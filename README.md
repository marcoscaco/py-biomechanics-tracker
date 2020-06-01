# py-biomechanics-tracker

Step 11: Install tf-slim library.
pip install git+https://github.com/adrianc-a/tf-slim.git@remove_contrib
Step 8: Install SWIG
conda install swig
Step 9: Build C++ library for post-processing.
cd tf_pose/pafprocess
swig -python -c++ pafprocess.i && python3 setup.py build_ext --inplace