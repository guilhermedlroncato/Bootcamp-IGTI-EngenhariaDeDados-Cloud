select * from year_2019 limit 10;

--Questão 06
select avg(e.NU_NOTA_MT) 
  from year_2019 e
 where e.tp_sexo = 'F';
 
--Questão 07
select avg(e.NU_NOTA_CH) 
  from year_2019 e
 where e.tp_sexo = 'M'
   and e.SG_UF_RESIDENCIA = 'SP';
   
--Quetão 08
  select e.no_municipio_residencia, max(e.NU_NOTA_CN)
    from year_2019 e
   where e.no_municipio_residencia in ('Governador Valadares', 'Ouro Preto', 'Ipatinga', 'Montes Claros')
group by e.no_municipio_residencia
order by 2 desc;

 
--Questão 09
select avg(e.NU_IDADE)
  from year_2019 e
 where e.no_municipio_nascimento = 'Natal';
 
--Questão 10
  select e.co_escola,  avg(e.NU_NOTA_MT)
    from year_2019 e
group by e.co_escola
order by 2 desc;

--Questão 11
select count(*)
  from year_2019 e
 where e.sg_uf_residencia = 'RJ'
   and e.NU_NOTA_MT > 600
   and e.tp_sexo = 'M';
   
--Questão 12
select count(*)
  from year_2019 e
 where e.no_municipio_nascimento = 'Recife'
   and e.no_municipio_nascimento = e.no_municipio_prova;
   
   
--Questão 13
select count(*)
  from year_2019 e
 where e.SG_UF_RESIDENCIA = 'SP'
   and e.tp_sexo = 'F'
   and e.in_gestante = 1
   and e.tp_presenca_ch = 1;
   
--Questão 14
select avg(e.NU_NOTA_CH) 
  from year_2019 e
 where e.sg_uf_residencia = 'SC'
   and e.in_deficiencia_fisica = 1;
   
--Questão 15
select avg(e.NU_NOTA_MT)
  from year_2019 e
 where e.no_municipio_residencia = 'Belo Horizonte'
   and e.tp_sexo = 'F'
   and e.in_cegueira = 1;