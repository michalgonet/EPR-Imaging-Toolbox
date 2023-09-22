linear_algebra_intro: str = 'These functions pertain to linear coordinate transformations, which are essential ' \
                            'for understanding the connection between the initial and primary coordinates ' \
                            'of a 3D point. They employ a 4-element vector notation that encompasses coordinate ' \
                            'rotation, translation, and scaling operations. These transformations play a pivotal ' \
                            'role in various fields, including computer graphics and computer vision, enabling ' \
                            'precise manipulation and positioning of objects in a 3D space.'

scaling: str = 'Matrix transformation for scaling'
translation: str = 'Matrix transformation for translation'
rotation_x: str = 'Matrix transformation for rotation about X'
rotation_y: str = 'Matrix transformation for rotation about Y'
rotation_z: str = 'Matrix transformation for rotation about Z'

sample_data_3d: str = 'Dataset contains sinogram for 3D image collected using Bruker EPR Tomograph ' \
                      'Elexsys L-band E540. Sinogram contains 400 projections (20x20) and reference spectrum ' \
                      'acquired without gradient magnetic field. The other EPR imaging parameters are as follow: ' \
                      'G=1.5G/cm, SW = 6G, CF = 388.5G'

deconvolution: str = 'In EPR imaging, spatial resolution is obtained by superimposing a magnetic field gradient ' \
                     'to the main field. Because of this each projection represents the convolution between ' \
                     'the spatial spin distribution along the gradient direction and the undistorted shape ' \
                     'of the resonance line. In EPRI where linewidths are much wider than in NMR particularly ' \
                     'in biomedical applications where nitroxides are used, simplification in the form ' \
                     'of direct reconstruction from obtained projections cannot be adopted. ' \
                     'To obtain projections which contained only spatial ' \
                     'distribution of paramagnetic probe deconvolution procedure must be involved before ' \
                     'reconstruction. Deconvolution is usually performed in the Fourier space with low-pass ' \
                     'filtering. The choice of filter cutoff frequency is crucial and must be a compromise ' \
                     'between two opposite needs: suppression the high-frequency noise and maintaining ' \
                     'the high-frequency signal components.'
