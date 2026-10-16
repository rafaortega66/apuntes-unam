import pandas as pd, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'figure.dpi':130,'axes.spines.top':False,'axes.spines.right':False,'font.size':10})
df=pd.read_excel('enoe.xlsx')
df['niv']=df.niv_edu.replace({'Prrimaria completa':'Primaria completa'})
out=[]
def p(*a): out.append(' '.join(str(x) for x in a))

# 2 estado con mayor ingreso y formal
g=df.groupby('estado').ingreso_mensual.sum().sort_values(ascending=False)
top=g.index[0]
gf=df[df.estado==top].groupby('tipo_empleo').ingreso_mensual.sum()
p('P2 estado con mayor suma de ingreso:',top,int(g.iloc[0]),'| formal:',int(gf.get('Formal',0)),'(%.1f%%)'%(100*gf.get('Formal',0)/gf.sum()),'informal:',int(gf.get('Informal',0)))
pm=df.groupby('estado').ingreso_mensual.mean().sort_values(ascending=False)
p('   mayor promedio:',pm.index[0],round(pm.iloc[0],0),'| CDMX posición promedio:',list(pm.index).index('Ciudad de México')+1 if 'Ciudad de México' in pm.index else 'n/a')
p('   estados:',sorted(df.estado.unique())[:40])
fig,ax=plt.subplots(1,2,figsize=(11,5))
g.head(10)[::-1].plot.barh(ax=ax[0],color='#7C9CD6');ax[0].set_title('Suma de ingreso mensual (top 10 estados)');ax[0].set_ylabel('')
t=df[df.estado.isin(g.head(10).index)].pivot_table(index='estado',columns='tipo_empleo',values='ingreso_mensual',aggfunc='sum').loc[g.head(10).index][::-1]
t.plot.barh(stacked=True,ax=ax[1],color={'Formal':'#45B8A8','Informal':'#E8735C'});ax[1].set_title('Ese ingreso, formal vs informal');ax[1].set_ylabel('')
plt.tight_layout();plt.savefig('p2_estado_formal.png');plt.close()

# 3 brecha
s=df.groupby('sex').ingreso_mensual.agg(['sum','mean','median','count'])
p('P3 por sexo:\n',s.round(0).to_string())
fig,ax=plt.subplots(1,3,figsize=(12,4))
for a,(c,tt) in zip(ax,[('sum','Suma'),('count','Recuento'),('mean','Promedio')]):
    s[c].plot.bar(ax=a,color=['#E8735C','#7C9CD6'] if s.index[0]=='Hombre' else ['#7C9CD6','#E8735C'],rot=0);a.set_title(tt+' de ingreso mensual' if c!='count' else 'Personas (recuento)');a.set_xlabel('')
plt.tight_layout();plt.savefig('p3_brecha_sexo.png');plt.close()
# brecha por escolaridad
b=df.pivot_table(index='niv',columns='sex',values='ingreso_mensual',aggfunc='mean')
p('   promedio por sexo y escolaridad:\n',b.round(0).to_string())
# brecha controlando horas: ingreso por hora
df['por_hora']=df.ingreso_mensual/(df.hrsocup*4.345)
p('   ingreso/hora promedio por sexo:',df.groupby('sex').por_hora.mean().round(1).to_dict())

# 4 horas
h=df.sort_values('hrsocup',ascending=False).head(5)[['estado','sex','edad','hrsocup','ingreso_mensual','tipo_empleo']]
p('P4 máximo de horas:',int(df.hrsocup.max()),'| top5:\n',h.to_string(),'\n   personas con >=70h:',int((df.hrsocup>=70).sum()),'promedio general:',round(df.hrsocup.mean(),1))
q=df.hrsocup.quantile([.5,.9,.99]).to_dict();p('   mediana/p90/p99:',q)
fig,ax=plt.subplots(figsize=(7,4));df.hrsocup.plot.hist(bins=40,ax=ax,color='#A98BD1');ax.set_title('Horas trabajadas a la semana');ax.set_xlabel('horas');plt.tight_layout();plt.savefig('p4_horas.png');plt.close()

# 5 horas vs ingreso
c=df.hrsocup.corr(df.ingreso_mensual);p('P5 correlación horas-ingreso (Pearson):',round(c,3))
bins=pd.cut(df.hrsocup,[0,20,35,48,60,150]);m=df.groupby(bins,observed=True).ingreso_mensual.agg(['mean','count']);p(m.round(0).to_string())
fig,ax=plt.subplots(1,2,figsize=(11,4))
ax[0].scatter(df.hrsocup,df.ingreso_mensual,s=4,alpha=.25,color='#7C9CD6');ax[0].set_title('Horas vs ingreso mensual (dispersión)');ax[0].set_xlabel('horas a la semana');ax[0].set_ylabel('ingreso mensual')
m['mean'].plot.bar(ax=ax[1],color='#45B8A8',rot=20);ax[1].set_title('Ingreso promedio por rango de horas');ax[1].set_xlabel('')
plt.tight_layout();plt.savefig('p5_horas_ingreso.png');plt.close()

# 6 estudio vs horas
e=df.groupby('niv').hrsocup.agg(['mean','median','count']).reindex(['Primaria incompleta','Primaria completa','Secundaria completa','Medio superior y superior']);p('P6 horas por nivel:\n',e.round(1).to_string());p('   corr anios_esc-horas:',round(df.anios_esc.corr(df.hrsocup),3))
fig,ax=plt.subplots(figsize=(7,4));e['mean'].plot.bar(ax=ax,color='#E8735C',rot=15);ax.set_title('Horas promedio por nivel de estudio');ax.set_xlabel('');plt.tight_layout();plt.savefig('p6_estudio_horas.png');plt.close()

# 7 edades extremas
mn=df[df.edad==df.edad.min()];mx=df[df.edad==df.edad.max()]
p('P7 edad mínima',df.edad.min(),'n=',len(mn),'ingreso suma',int(mn.ingreso_mensual.sum()),'| máxima',df.edad.max(),'n=',len(mx),'ingreso suma',int(mx.ingreso_mensual.sum()))
p(mn[['estado','sex','hrsocup','ingreso_mensual','tipo_empleo']].to_string());p(mx[['estado','sex','hrsocup','ingreso_mensual','tipo_empleo']].to_string())
ea=df.groupby('edad').ingreso_mensual.agg(['sum','count','mean'])
fig,ax=plt.subplots(1,3,figsize=(13,3.8))
for a,c,tt in zip(ax,['sum','count','mean'],['Suma de ingreso','Recuento de personas','Promedio de ingreso']):
    ea[c].plot(ax=a,color='#7C9CD6');a.set_title(tt+' por edad');a.set_xlabel('edad')
plt.tight_layout();plt.savefig('p7_edades.png');plt.close()

# 8 combinada
cmb=df.pivot_table(index=['sex','niv'],columns='num_trabajos',values='ingreso_mensual',aggfunc='mean').reindex(['Primaria incompleta','Primaria completa','Secundaria completa','Medio superior y superior'],level=1)
p('P8 ingreso promedio por sexo, nivel y # empleos:\n',cmb.round(0).to_string())
fig,ax=plt.subplots(figsize=(10,5))
cmb.plot.bar(ax=ax,color=['#7C9CD6','#E8735C']);ax.set_title('Ingreso mensual promedio por sexo, nivel de estudio y número de empleos');ax.set_xlabel('');ax.set_xticklabels([f'{a}\n{b}' for a,b in cmb.index],fontsize=7,rotation=0)
plt.tight_layout();plt.savefig('p8_combinada.png');plt.close()
cmb.round(0).to_csv('p8_tabla.csv')

# 1 criterios: ejemplo mala vs buena
fig,ax=plt.subplots(1,3,figsize=(13,3.8))
df.groupby('niv').ingreso_mensual.mean().plot.bar(ax=ax[0],rot=15,color='#A98BD1');ax[0].set_title('BARRAS: comparar categorías');ax[0].set_xlabel('')
ea['mean'].plot(ax=ax[1],color='#7C9CD6');ax[1].set_title('LÍNEAS: tendencia (edad)');
ax[2].scatter(df.anios_esc,df.ingreso_mensual,s=4,alpha=.2,color='#45B8A8');ax[2].set_title('DISPERSIÓN: relación de 2 numéricas')
plt.tight_layout();plt.savefig('p1_criterios.png');plt.close()
open('resultados_enoe.txt','w').write('\n'.join(out));print('\n'.join(out))
