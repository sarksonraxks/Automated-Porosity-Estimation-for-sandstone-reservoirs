import pandas as pd
import lasio 
well=lasio.read(r'C:\Users\Sark\VSCODE\Beginner\.venv\PROJECTS\Porosity_estimation\VOLVE Dataset\15_9-F-1A.LAS')
well_df=well.df().reset_index()

well_df=well_df[['DEPTH','GR','RHOB','NPHI']]
well_df=well_df.dropna(axis=0)
# print(well_df)
# Run this only to check for your matrix density
# import matplotlib.pyplot as plt
# plt.style.use('bmh')
# plt.scatter(x=well_df['NPHI'],y=well_df['RHOB'],c=well_df['GR'],vmin=0,vmax=100,cmap='rainbow')
# plt.xlim(-0.05,0.45)
# plt.ylim(3.0,1.9)
# plt.ylabel('Bulk Density(g/cc)', fontsize=14)
# plt.xlabel('Neutron Porosity(v/v)', fontsize=14)
# plt.grid(True)
# plt.title('Neutron-Density Crossplot')
# plt.colorbar(label='Gamma Ray - API')
# plt.show()
import numpy as np
# formula for density porosity
rho_matrix = 2.65  
rho_fluid  = 1.0   
well_df['PHID'] = (rho_matrix - well_df['RHOB']) / (rho_matrix - rho_fluid)  
well_df.loc[well_df['PHID'] < 0, 'PHID'] = 0
well_df.loc[well_df['PHID'] > 1, 'PHID'] = np.nan
gr_cutoff = 60
well_df.loc[well_df['GR'] > gr_cutoff, 'PHID'] = float('nan')
well_df['PHI_TOTAL']=(well_df['NPHI']+well_df['PHID'])/2
print(well_df)
