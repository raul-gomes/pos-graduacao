Sistema de recomendação

Neo4j

- Nós são os registros
- Labels são conjuntos agrupado de nós
- Relacionamentos são as conexões entre os nós
- Propriedades são definições de um nós (Direção, Agrupamento, etc)

Linguagem 
- Cypher query. Exemplo {(a) - [:LIKES] -> (b)}
    - MATCH (p:pessoa{idade:25}) RETURN p
        - MATHC - Comando de seleção
        - p: - pessoa é o nosso conjunto de dados
        - {idade:25} - é o nosso where
        - return p - registros que eu quero que retorne.
        
        obs: paralelo com o SQL: SELECT * FROM Pessoa WHERE idade = 25


- Otimização de query CYPHER
    1. Usar índices: índices são estruturas de dados que permitem que o Neo4j encontre os nós e relacionamentos relevantes de maneira mais rápida. Você pode criar índices para os atributos que são usados frequentemente em suas consultas para aumentar a velocidade das consultas.
    2. Usar o cache de consulta: o Neo4j mantém um cache de consulta para armazenar os resultados de consultas freqüentemente usadas. Isso pode ajudar a aumentar a velocidade das consultas se elas são executadas várias vezes.
    3. Otimizar as consultas: é importante escrever consultas Cypher eficientes para garantir que elas executem rapidamente. Isso inclui evitar a aninhar demais as consultas, usar o MATCH corretamente e evitar usar o WHERE de maneira ineficiente.
    4. Usar o profiler de consulta: o profiler de consulta é uma ferramenta que ajuda a identificar as partes de uma consulta que estão consumindo mais tempo de execução. Isso pode ajudar a identificar áreas da consulta que precisam ser otimizadas.
    5. Usar clusters: o Neo4j suporta o uso de clusters para distribuir os dados em vários nós e aumentar a escalabilidade do sistema. Isso pode ajudar a aumentar a performance do sistema de recomendação quando ele está lidando com grandes quantidades de dados.


Fontes:
- https://www.youtube.com/watch?v=XJkKRoUeOVc
