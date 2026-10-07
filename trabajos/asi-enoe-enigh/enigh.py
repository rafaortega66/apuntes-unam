import pandas as pd, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'figure.dpi':130,'axes.spines.top':False,'axes.spines.right':False,'font.size':10})
v=pd.read_csv('viviendas.csv',dtype={'folioviv':str},low_memory=False)
print(v.shape); print(list(v.columns))
ent={'01':'Aguascalientes','02':'Baja California','03':'Baja California Sur','04':'Campeche','05':'Coahuila','06':'Colima','07':'Chiapas','08':'Chihuahua','09':'CDMX','10':'Durango','11':'Guanajuato','12':'Guerrero','13':'Hidalgo','14':'Jalisco','15':'Edo. de México','16':'Michoacán','17':'Morelos','18':'Nayarit','19':'Nuevo León','20':'Oaxaca','21':'Puebla','22':'Querétaro','23':'Quintana Roo','24':'San Luis Potosí','25':'Sinaloa','26':'Sonora','27':'Tabasco','28':'Tamaulipas','29':'Tlaxcala','30':'Veracruz','31':'Yucatán','32':'Zacatecas'}
v['entidad']=v.folioviv.str[:2].map(ent)
print(v.entidad.isna().sum())
v['renta']=pd.to_numeric(v.renta,errors='coerce')
v['tenencia']=pd.to_numeric(v.tenencia,errors='coerce')
print(v.tenencia.value_counts().to_dict()); print(v.renta.describe().to_dict())
ten={1:'Rentada',2:'Prestada',3:'Propia (la están pagando)',4:'Propia',5:'Intestada / litigio',6:'Otra situación'}
# útil 1: renta promedio por entidad
r=v[(v.tenencia==1)&(v.renta>0)].groupby('entidad').renta.agg(['mean','count']).sort_values('mean',ascending=False)
print(r.head(5)); 
fig,ax=plt.subplots(figsize=(8,6));r['mean'][::-1].plot.barh(ax=ax,color='#7C9CD6');ax.set_title('ENIGH · Renta mensual promedio de viviendas rentadas, por entidad');ax.set_ylabel('');plt.tight_layout();plt.savefig('enigh_util1_renta_entidad.png');plt.close()
# útil 2: tenencia
t=v.tenencia.map(ten).value_counts();print(t)
fig,ax=plt.subplots(figsize=(7,4));t[::-1].plot.barh(ax=ax,color='#45B8A8');ax.set_title('ENIGH · Viviendas según tenencia');ax.set_ylabel('');plt.tight_layout();plt.savefig('enigh_util2_tenencia.png');plt.close()
# útil 3: cuartos y dormitorios
v['num_cuarto']=pd.to_numeric(v.num_cuarto,errors='coerce')
c=v.num_cuarto.clip(upper=8).value_counts().sort_index();print(c.to_dict())
fig,ax=plt.subplots(figsize=(7,4));c.plot.bar(ax=ax,color='#A98BD1',rot=0);ax.set_title('ENIGH · Viviendas por número de cuartos (8 = 8 o más)');ax.set_xlabel('cuartos');plt.tight_layout();plt.savefig('enigh_util3_cuartos.png');plt.close()
# innecesarios
fig,ax=plt.subplots(figsize=(5,5));v.tipo_viv.astype(str).value_counts().head(6).plot.pie(ax=ax,autopct='%1.0f%%');ax.set_ylabel('');ax.set_title('Innecesario 1 · Pastel de tipo de vivienda (códigos)');plt.tight_layout();plt.savefig('enigh_inutil1_pastel_tipo.png');plt.close()
fig,ax=plt.subplots(figsize=(6,4));ax.scatter(range(len(v.sample(2000,random_state=1))),v.sample(2000,random_state=1).focos.apply(pd.to_numeric,errors='coerce'),s=3);ax.set_title('Innecesario 2 · Focos por vivienda (dispersión sin sentido)');plt.tight_layout();plt.savefig('enigh_inutil2_focos.png');plt.close()
